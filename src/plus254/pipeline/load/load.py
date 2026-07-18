import logging
from pathlib import Path
from typing import Any
import pandas as pd
from plus254.quality_checks.main import QualityReport
from plus254.utils.config import bump_last_updated, load_dataset_spec
from plus254.utils.loaders import huggingface
from plus254.utils.loaders import merge

logger = logging.getLogger(__name__)

DEFAULT_YAML = Path("src/plus254/datasets.yaml")

def load(
    df: pd.DataFrame,
    slug: str,
    *,
    yaml_path: Path | str = DEFAULT_YAML,
    dry_run: bool = False,
    coverage_threshold: float = 0.65,
    repo_id: str | None = None,
    token: str | None = None,
) -> pd.DataFrame:
    """Validate, upsert, and push a dataset to the HuggingFace backend."""
    yaml_path = Path(yaml_path)
    spec = load_dataset_spec(yaml_path, slug)

    logger.info("[%s] Running quality checks …", slug)
    report = QualityReport(
        df,
        config_name=slug,
        yaml_path=yaml_path,
        coverage_threshold=coverage_threshold,
    )
    report.log_summary()
    report.raise_on_failure()
    validated = report.df
    logger.info("[%s] Quality checks passed.", slug)

    natural_keys: list[str] = spec.get("natural_keys", [])
    if not natural_keys:
        logger.warning(
            "[%s] No natural_keys defined — performing full replace.", slug
        )

    logger.info("[%s] Pulling existing dataset from HuggingFace …", slug)
    existing = huggingface.pull(slug, repo_id=repo_id, token=token)

    if natural_keys and not existing.empty:
        merged = merge.upsert(existing, validated, natural_keys)
    else:
        merged = validated.copy()

    logger.info(
        "[%s] Merge: %d existing + %d new → %d final",
        slug,
        len(existing),
        len(validated),
        len(merged),
    )

    if dry_run:
        logger.info("[%s] DRY RUN — skipping push.", slug)
        return merged

    logger.info("[%s] Pushing to HuggingFace …", slug)
    try:
        huggingface.push(slug, merged, repo_id=repo_id, token=token)
        logger.info("[%s] Push complete.", slug)
    except Exception:
        logger.error("[%s] Push failed — manifest not updated.", slug)
        raise

    bump_last_updated(yaml_path, slug)
    logger.info("[%s] Bumped last_updated in manifest.", slug)

    return merged
