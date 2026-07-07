from functools import lru_cache
import logging
from pathlib import Path
from typing import List
from plus254.quality_checks.exceptions import ContractViolation
import pandas as pd
import pandera.pandas as pa
import yaml

logger = logging.getLogger(__name__)

_TYPE_MAP = {
    "integer": pa.Int64,
    "float": pa.Float64,
    "string": pa.String,
    "date": pa.DateTime,
    "datetime": pa.DateTime,
}

@lru_cache(maxsize=1)
def _load_standards() -> dict[str, str]:
    """Load the global column-type standards once."""
    standards_path = Path(__file__).resolve().parent / "standards.yaml"
    if not standards_path.exists():
        logger.warning("standards.yaml not found - falling back to dataset-level types")
        return {}

    with open(standards_path) as f:
        raw = yaml.safe_load(f) or {}

    standards = raw.get("standards", {})
    logger.debug(f"Loaded {len(standards)} global type standards")
    return standards


def _resolve_type(col_name: str, spec: dict, config_name: str | None) -> str:
    """Return the effective type for a column, preferring global standards."""
    standards = _load_standards()
    yaml_type = spec.get("type")

    if col_name in standards:
        standard_type = standards[col_name]
        if yaml_type and yaml_type != standard_type:
            logger.warning(
                f"[{config_name}] Column '{col_name}' declares type '{yaml_type}' "
                f"but global standard is '{standard_type}'. Enforcing standard."
            )
        return standard_type

    return yaml_type or "string"


def _build_schema(
    columns: dict, natural_keys: List[str], config_name: str | None = None
) -> pa.DataFrameSchema:
    """Convert YAML column specs into a Pandera DataFrameSchema."""
    schema_columns = {}
    for col_name, spec in columns.items():
        type_str = _resolve_type(col_name, spec, config_name)
        dtype = _TYPE_MAP.get(type_str, pa.String)
        # Natural-key columns must be non-null
        nullable = col_name not in natural_keys
        schema_columns[col_name] = pa.Column(dtype, nullable=nullable)

    return pa.DataFrameSchema(schema_columns, strict=True)


def check_schema(df: pd.DataFrame, config_name: str, yaml_path: Path | str) -> pd.DataFrame:
    """
    Validate df against its column-type contract.

    Global standards in standards/*  take precedence over per-dataset types
    in datasets.yaml. Natural-key columns are enforced as non-nullable.
    
    Parameters
    ----------
    df : pd.DataFrame
    config_name : str
        Top-level key in the YAML file.
    yaml_path : Path or str
        Path to the collector's datasets.yaml.

    Returns
    -------
    pd.DataFrame
        The validated DataFrame (types may be coerced).

    Raises
    ------
    ContractViolation
        If schema constraints fail.
    ValueError
        If config or natural_keys are missing.
    """
    yaml_path = Path(yaml_path)
    if not yaml_path.exists():
        raise ValueError(f"datasets.yaml not found: {yaml_path}")

    with open(yaml_path) as f:
        raw = yaml.safe_load(f) or {}

    spec = raw.get(config_name)
    if not spec:
        available = sorted(raw.keys())
        raise ValueError(
            f"'{config_name}' not found in {yaml_path}. Available: {available}"
        )

    columns = spec.get("columns", {})
    natural_keys = spec.get("natural_keys", [])
    if not natural_keys:
        logger.warning(f"'{config_name}' has no natural_keys defined")

    schema = _build_schema(columns, natural_keys, config_name)

    try:
        validated = schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as exc:
        raise ContractViolation(config_name, exc.failure_cases) from exc

    logger.info(
        f"Validated '{config_name}' ({len(validated)} rows, {len(columns)} cols)"
    )
    return validated

