"""Data quality checks for notebooks and the upload pipeline."""
import logging
from pathlib import Path
from typing import Any
from plus254.quality_checks.exceptions import QualityViolation
import pandas as pd
import yaml

def _load_spec(yaml_path: Path | str, config_name: str) -> dict:
    yaml_path = Path(yaml_path)
    with open(yaml_path) as f:
        raw = yaml.safe_load(f) or {}
    spec = raw.get(config_name, {})
    if not spec:
        raise ValueError(f"'{config_name}' not found in {yaml_path}")
    return spec

def check_dimensional_coverage(
    df: pd.DataFrame,
    config_name: str,
    yaml_path: Path | str,
    threshold: float = 0.70,
) -> dict[str, Any]:
    """
    For each group (by the first natural key), check what % of expected
    dimension combinations are present. The remaining natural keys are
    treated as categorical dimensions.

    Returns
    -------
    dict with keys:
        passed (bool) — True if overall_coverage >= threshold
        overall_coverage (float)
        groups (list of dicts per group)
        below_threshold (list of groups that failed)
    """
    spec = _load_spec(yaml_path, config_name)
    natural_keys = spec.get("natural_keys", [])

    if len(natural_keys) < 2:
        raise QualityViolation(
            f"[{config_name}] Coverage check requires at least 2 natural keys, "
            f"got {len(natural_keys)}: {natural_keys}"
        )

    group_by = natural_keys[0]
    dimensions = natural_keys[1:]

    dim_uniques = {col: df[col].dropna().unique() for col in dimensions}
    expected_count = 1
    for vals in dim_uniques.values():
        expected_count *= len(vals)

    if expected_count == 0:
        return {
            "passed": True,
            "overall_coverage": 1.0,
            "groups": [],
            "below_threshold": [],
            "skipped": True,
        }

    results = []
    below_threshold = []

    for group_key, grp in df.groupby(group_by, sort=False):
        actual = (
            grp[dimensions]
            .dropna(how="any")
            .drop_duplicates()
            .shape[0]
        )
        coverage = actual / expected_count
        group_result = {
            "group": {group_by: group_key},
            "expected": expected_count,
            "actual": actual,
            "coverage": coverage,
        }
        results.append(group_result)
        if coverage < threshold:
            below_threshold.append(group_result)

    overall = (
        sum(r["actual"] for r in results) / (len(results) * expected_count)
        if results
        else 1.0
    )

    return {
        "passed": overall >= threshold,
        "overall_coverage": overall,
        "groups": results,
        "below_threshold": below_threshold,
        "skipped": False,
    }