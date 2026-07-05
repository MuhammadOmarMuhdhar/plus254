"""Schema validation from datasets.yaml contracts using Pandera."""
import logging
from pathlib import Path
from typing import List

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

class ContractViolation(Exception):
    """Raised when a DataFrame fails validation against its datasets.yaml contract."""

    def __init__(self, config_name: str, failures: pd.DataFrame):
        self.config_name = config_name
        self.failures = failures
        super().__init__(
            f"Contract violation for '{config_name}': {len(failures)} check(s) failed.\n"
            f"{failures.head(20).to_string(index=False)}"
        )

def _build_schema(columns: dict, natural_keys: List[str]) -> pa.DataFrameSchema:
    """Convert YAML column specs into a Pandera DataFrameSchema."""
    schema_columns = {}
    for col_name, spec in columns.items():
        type_str = spec.get("type", "string")
        dtype = _TYPE_MAP.get(type_str, pa.String)
        # Natural-key columns must be non-null
        nullable = col_name not in natural_keys
        schema_columns[col_name] = pa.Column(dtype, nullable=nullable)

    return pa.DataFrameSchema(schema_columns, strict=True)


def validate(df: pd.DataFrame, config_name: str, yaml_path: Path | str) -> pd.DataFrame:
    """
    Validate *df* against its datasets.yaml contract.

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

    schema = _build_schema(columns, natural_keys)

    try:
        validated = schema.validate(df, lazy=True)
    except pa.errors.SchemaErrors as exc:
        raise ContractViolation(config_name, exc.failure_cases) from exc

    logger.info(
        f"Validated '{config_name}' ({len(validated)} rows, {len(columns)} cols)"
    )
    return validated
