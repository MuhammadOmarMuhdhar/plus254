"""Data quality checks for notebooks and the upload pipeline.

Usage:
    from plus254.pipeline.quality_checks.main import QualityReport

    report = QualityReport(df, "pump_prices", "path/to/datasets.yaml")
    report.log_summary()
    report.raise_on_failure()
"""

import logging
from pathlib import Path
from typing import Any

import pandas as pd
import yaml

from .duplicates import check_duplicates
from .dimensional_coverage import check_dimensional_coverage
from .exceptions import QualityViolation
from .schema import check_schema

logger = logging.getLogger(__name__)


class QualityReport:
    """Run all quality checks on construction.

    Parameters
    ----------
    df : pd.DataFrame
        Data to validate.
    config_name : str
        Top-level key in datasets.yaml.
    yaml_path : Path or str
        Path to the collector's datasets.yaml.
    coverage_threshold : float
        Minimum dimensional coverage ratio (default 0.70).

    Attributes
    ----------
    df : pd.DataFrame
        Schema-validated DataFrame (may be coerced).
    natural_keys : list[str] | None
        Natural keys read from the YAML spec, if defined.
    results : dict[str, Any]
        Raw check results keyed by check name.
    """

    def __init__(
        self,
        df: pd.DataFrame,
        config_name: str,
        yaml_path: Path | str,
        coverage_threshold: float = 0.80,
    ):
        self.df = df
        self.config_name = config_name
        self.yaml_path = Path(yaml_path)
        self.coverage_threshold = coverage_threshold
        self.results: dict[str, Any] = {}
        self.natural_keys: list[str] | None = None

        spec = self._load_spec()
        self.natural_keys = spec.get("natural_keys")
        columns = spec.get("columns", {})

        if columns:
            self.df = check_schema(self.df, config_name, self.yaml_path)
            self.results["schema"] = {"passed": True, "n_columns": len(columns)}
        else:
            self.results["schema"] = {"passed": True, "skipped": True}

        if self.natural_keys:
            self.results["duplicates"] = check_duplicates(self.df, self.natural_keys)
        else:
            self.results["duplicates"] = {"passed": True, "skipped": True}

        self.results["coverage"] = check_dimensional_coverage(
            self.df, config_name, self.yaml_path, threshold=coverage_threshold,
        )

    def _load_spec(self) -> dict:
        with open(self.yaml_path) as f:
            raw = yaml.safe_load(f) or {}
        spec = raw.get(self.config_name)
        if not spec:
            available = sorted(raw.keys())
            raise ValueError(
                f"'{self.config_name}' not found in {self.yaml_path}. "
                f"Available: {available}"
            )
        return spec

    def log_summary(self) -> None:
        """Log a structured summary of all check results."""
        logger.info(
            "Quality report for '%s' (%d rows)", self.config_name, len(self.df)
        )

        sch = self.results.get("schema", {})
        if sch.get("skipped"):
            logger.info("  Schema: skipped (no columns defined)")
        else:
            logger.info(
                "  Schema: PASS (%d cols, %d rows)", sch.get("n_columns", 0), len(self.df)
            )

        dup = self.results.get("duplicates", {})
        if dup.get("skipped"):
            logger.info("  Duplicates: skipped (no natural keys)")
        elif dup.get("passed"):
            logger.info("  Duplicates: PASS (0 duplicates)")
        else:
            logger.warning(
                "  Duplicates: FAIL -- %d duplicate rows on natural keys",
                dup["duplicate_count"],
            )

        cov = self.results.get("coverage", {})
        if cov.get("skipped"):
            logger.info("  Coverage: skipped")
        elif cov.get("passed"):
            logger.info(
                "  Coverage: PASS -- %.1f%% overall", cov["overall_coverage"] * 100
            )
        else:
            logger.warning(
                "  Coverage: FAIL -- %.1f%% overall (threshold: %.0f%%)",
                cov["overall_coverage"] * 100,
                self.coverage_threshold * 100,
            )
            for g in cov.get("below_threshold", []):
                period = ", ".join(f"{k}={v}" for k, v in g["group"].items())
                logger.warning(
                    "    -- %s: %d/%d (%.1f%%)",
                    period,
                    g["actual"],
                    g["expected"],
                    g["coverage"] * 100,
                )

    def to_text(self) -> str:
        """Return a plain-text summary string (for notebooks)."""
        lines = [
            f"Quality Report: {self.config_name} ({len(self.df)} rows)",
            f"Coverage threshold: {self.coverage_threshold:.0%}",
            "",
        ]

        sch = self.results.get("schema", {})
        if sch.get("skipped"):
            lines.append("Schema: skipped (no columns defined)")
        else:
            lines.append(
                f"Schema: PASS ({sch.get('n_columns', 0)} cols, {len(self.df)} rows)"
            )

        dup = self.results.get("duplicates", {})
        if dup.get("skipped"):
            lines.append("Duplicates: skipped (no natural keys)")
        elif dup.get("passed"):
            lines.append("Duplicates: PASS (0 duplicates)")
        else:
            lines.append(
                f"Duplicates: FAIL -- {dup['duplicate_count']} duplicate rows"
            )

        cov = self.results.get("coverage", {})
        if cov.get("skipped"):
            lines.append("Coverage: skipped")
        elif cov.get("passed"):
            lines.append(f"Coverage: PASS -- {cov['overall_coverage']:.1%} overall")
        else:
            lines.append(
                f"Coverage: FAIL -- {cov['overall_coverage']:.1%} overall "
                f"(threshold: {self.coverage_threshold:.0%})"
            )
            for g in cov.get("below_threshold", []):
                period = ", ".join(f"{k}={v}" for k, v in g["group"].items())
                lines.append(
                    f"  -- {period}: {g['actual']}/{g['expected']} ({g['coverage']:.1%})"
                )

        return "\n".join(lines)

    def raise_on_failure(self) -> None:
        """Raise QualityViolation if any hard-fail check did not pass."""
        dup = self.results.get("duplicates", {})
        if not dup.get("passed") and not dup.get("skipped"):
            raise QualityViolation(
                f"[{self.config_name}] Duplicate natural keys: "
                f"{dup['duplicate_count']} rows"
            )

        cov = self.results.get("coverage", {})
        if not cov.get("passed") and not cov.get("skipped"):
            groups = ", ".join(
                ", ".join(f"{k}={v}" for k, v in g["group"].items())
                for g in cov["below_threshold"]
            )
            raise QualityViolation(
                f"[{self.config_name}] Dimensional coverage "
                f"{cov['overall_coverage']:.1%} below threshold "
                f"{self.coverage_threshold:.0%}. Failed groups: {groups}"
            )
