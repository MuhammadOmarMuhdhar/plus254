import importlib
import logging
from typing import Any
import pandas as pd
from prefect import task
from plus254.pipeline.load.load import load

logger = logging.getLogger(__name__)

def _dispatch_load(
    slug: str, result: pd.DataFrame | dict[str, pd.DataFrame], dry_run: bool
) -> None:
    """Handle both single-DataFrame and multi-DataFrame transform outputs."""
    if isinstance(result, dict):
        for sub_slug, df in result.items():
            load(df, sub_slug, dry_run=dry_run)
    else:
        load(result, slug, dry_run=dry_run)
        
@task(retries=2, retry_delay_seconds=60)
def run_fixed_source(slug: str, dry_run: bool = False) -> None:
    """Extract → Transform → Load for one fixed-source slug."""
    logger.info("[%s] Starting fixed-source pipeline", slug)
    try:
        extract_mod = importlib.import_module(
            f"plus254.pipeline.extract.dynamic.fixed_source.{slug}"
        )
        df = extract_mod.extract()

        transform_mod = importlib.import_module(
            f"plus254.pipeline.transform.{slug}"
        )
        result = transform_mod.transform(df)

        _dispatch_load(slug, result, dry_run)

        logger.info("[%s] Pipeline complete", slug)

    except Exception as e:
        logger.error("[%s] Pipeline failed: %s", slug, e)


@task(retries=2, retry_delay_seconds=60)
def run_static_source(slug: str, dry_run: bool = False) -> None:
    """Extract → Transform → Load for one static-source slug."""
    logger.info("[%s] Starting static-source pipeline", slug)
    try:

        extract_mod = importlib.import_module(
            f"plus254.pipeline.extract.static.{slug}"
        )
        df = extract_mod.extract()

        transform_mod = importlib.import_module(
            f"plus254.pipeline.transform.{slug}"
        )
        result = transform_mod.transform(df)

        _dispatch_load(slug, result, dry_run)

        logger.info("[%s] Pipeline complete", slug)

    except Exception as e:
        logger.error("[%s] Pipeline failed: %s", slug, e)


@task(retries=2, retry_delay_seconds=60)
def extract_rolling_source(source: str) -> list[dict[str, Any]]:
    """Download all PDFs for a rolling source and extract all tables.

    'source' is the directory name under extract/dynamic/rolling_source/
    """
    logger.info("Starting rolling-source extraction: %s", source)
    try:
        extract_mod = importlib.import_module(
            f"plus254.pipeline.extract.dynamic.rolling_source.{source}.extract"
        )
        records = extract_mod.extract()
        logger.info("Extraction complete: %d records", len(records))
        return records
    except Exception as e:
        logger.error("Extraction failed: %s", e)
        raise


@task(retries=2, retry_delay_seconds=60)
def run_rolling_slug(
    slug: str, records: list[dict[str, Any]], dry_run: bool = False
) -> None:
    """Filter records by slug → Transform → Load."""
    logger.info("[%s] Starting rolling-source pipeline (%d records)", slug, len(records))
    try:
        slug_records = [r for r in records if r.get("dataset") == slug]
        if not slug_records:
            logger.warning("[%s] No records found — skipping", slug)
            return

        transform_mod = importlib.import_module(
            f"plus254.pipeline.transform.{slug}"
        )
        result = transform_mod.transform(slug_records)

        _dispatch_load(slug, result, dry_run)

        logger.info("[%s] Pipeline complete", slug)

    except Exception as e:
        logger.error("[%s] Pipeline failed: %s", slug, e)

