import importlib
import logging
import sys
import time
from pathlib import Path
import pandas as pd
from plus254.pipeline.load.load import load
from plus254.utils.config import load_datasets
from plus254.utils.loaders import huggingface
from plus254.utils.logging import setup_logging
from plus254.pipeline.orchestrator.registry import get_slugs
import argparse


setup_logging()
logger = logging.getLogger("seed")

YAML_PATH = Path("src/plus254/datasets.yaml")

def should_seed(slug: str) -> bool:
    existing = huggingface.pull(slug)
    if existing.empty:
        logger.info("[%s] No existing data → will seed", slug)
        return True
    logger.info("[%s] Already has %d rows → skipping", slug, len(existing))
    return False


def _dispatch(slug: str, result: pd.DataFrame | dict[str, pd.DataFrame],
              dry_run: bool) -> None:
    if isinstance(result, dict):
        for sub_slug, df in result.items():
            load(df, sub_slug, dry_run=dry_run)
    else:
        load(result, slug, dry_run=dry_run)


def main():

    parser = argparse.ArgumentParser(description="Seed HF datasets")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--slug", type=str, default=None)
    args = parser.parse_args()

    start = time.time()
    seeded = skipped = 0
    failed_slugs: list[str] = []

    load_datasets(YAML_PATH)  # validate YAML loads early
    fixed = get_slugs(YAML_PATH, source_type="fixed")
    static = get_slugs(YAML_PATH, source_type="static")

    rolling_sources: dict[str, list[str]] = {}
    rolling_root = Path("src/plus254/pipeline/extract/dynamic/rolling_source")
    if rolling_root.exists():
        for d in rolling_root.iterdir():
            if d.is_dir():
                slugs = get_slugs(YAML_PATH, source_type=f"rolling_{d.name}")
                if slugs:
                    rolling_sources[d.name] = slugs

    if args.slug:
        t = args.slug
        fixed = [s for s in fixed if s == t]
        static = [s for s in static if s == t]
        rolling_sources = {
            k: [s for s in v if s == t]
            for k, v in rolling_sources.items()
        }
        rolling_sources = {k: v for k, v in rolling_sources.items() if v}
        if not any([fixed, static, rolling_sources]):
            logger.error("Slug '%s' not found in any source type", t)
            sys.exit(1)

    logger.info("=" * 60)
    logger.info("SEED — dry_run=%s", args.dry_run)
    logger.info("Fixed: %d  Static: %d  Rolling: %s",
                len(fixed), len(static), list(rolling_sources.keys()))
    logger.info("=" * 60)

    for slug in fixed:
        if not should_seed(slug):
            skipped += 1
            continue
        try:
            mod = importlib.import_module(
                "plus254.pipeline.extract.dynamic.fixed_source." + slug)
            df = mod.extract()
            mod = importlib.import_module(
                "plus254.pipeline.transform." + slug)
            _dispatch(slug, mod.transform(df), args.dry_run)
            seeded += 1
        except Exception as e:
            logger.error("[%s] Failed: %s", slug, e)
            failed_slugs.append(slug)

    for slug in static:
        if not should_seed(slug):
            skipped += 1
            continue
        try:
            mod = importlib.import_module(
                "plus254.pipeline.extract.static." + slug)
            df = mod.extract()
            mod = importlib.import_module(
                "plus254.pipeline.transform." + slug)
            _dispatch(slug, mod.transform(df), args.dry_run)
            seeded += 1
        except Exception as e:
            logger.error("[%s] Failed: %s", slug, e)
            failed_slugs.append(slug)

    for source, source_slugs in rolling_sources.items():
        needed = [s for s in source_slugs if should_seed(s)]
        if not needed:
            skipped += len(source_slugs)
            continue

        logger.info("[rolling:%s] Extracting (needed: %s) …", source, needed)
        try:
            mod = importlib.import_module(
                "plus254.pipeline.extract.dynamic.rolling_source."
                + source + ".extract")
            all_records = mod.extract(slugs=set(needed))
        except Exception as e:
            logger.error("[rolling:%s] Extraction failed: %s", source, e)
            failed_slugs.extend(needed)
            continue

        for slug in needed:
            slug_records = [r for r in all_records
                            if r.get("dataset") == slug]
            if not slug_records:
                logger.warning("[%s] No records found → skipping", slug)
                failed_slugs.append(slug)
                continue
            try:
                mod = importlib.import_module(
                    "plus254.pipeline.transform." + slug)
                _dispatch(slug, mod.transform(slug_records), args.dry_run)
                seeded += 1
            except Exception as e:
                logger.error("[%s] Failed: %s", slug, e)
                failed_slugs.append(slug)

    elapsed = time.time() - start
    logger.info("=" * 60)
    logger.info("SEED COMPLETE — %d seeded, %d skipped, %d failures (%.1fs)",
                seeded, skipped, len(failed_slugs), elapsed)
    if failed_slugs:
        logger.info("Failed slugs: %s", ", ".join(failed_slugs))
    logger.info("=" * 60)
    sys.exit(1 if failed_slugs else 0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Aborted by user.")
        sys.exit(130)
