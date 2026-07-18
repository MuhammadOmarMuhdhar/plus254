import logging
from pathlib import Path
from typing import Any
from plus254.quality_checks.exceptions import QualityViolation
import pandas as pd
from plus254.utils.config import load_dataset_spec


def _nested_dimensions(
    df: pd.DataFrame, group_by: str, dimensions: list[str]
) -> list[str]:
    """Return dimension columns whose values each appear in exactly 1 group."""
    nested = []
    for dim in dimensions:
        groups_per_value = df.groupby(dim, sort=False)[group_by].nunique()
        if (groups_per_value == 1).all():
            nested.append(dim)
    return nested


def check_dimensional_coverage(
    df: pd.DataFrame,
    config_name: str,
    yaml_path: Path | str,
    threshold: float = 0.80,
) -> dict[str, Any]:
    """
    For each group (by the first natural key), check what % of expected
    dimension combinations are present. If >= threshold, the group passes. 
    If all groups pass, the overall check passes.
    """
    spec = load_dataset_spec(yaml_path, config_name)
    natural_keys = spec.get("natural_keys", [])

    if len(natural_keys) < 2:
        raise QualityViolation(
            f"[{config_name}] Coverage check requires at least 2 natural keys; data needs at least two columns,"
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

    nested = _nested_dimensions(df, group_by, dimensions)
    if nested:
        return {
            "passed": True,
            "overall_coverage": 1.0,
            "groups": [],
            "below_threshold": [],
            "skipped": True,
            "reason": (
                f"hierarchical dimensions under '{group_by}': "
                f"{', '.join(nested)} (each value appears in 1 group only)"
            ),
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