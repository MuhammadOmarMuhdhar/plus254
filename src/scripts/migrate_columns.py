"""Migrate column names on HuggingFace datasets to match normalized schema.

Run: python -m src.scripts.migrate_columns
"""

import os
import sys
import logging
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from dotenv import load_dotenv
import pandas as pd
from datasets import load_dataset, Dataset

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

REPO_ID = os.environ.get("HF_REPO_ID")
TOKEN = os.environ.get("HF_TOKEN")

RENAME_MAP = {
    # Kilimo datasets (same rename for all 18 configs)
    "production_value_livestock": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "crop_area": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "production_quantity_livestock": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "livestock_population": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "crop_yield": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "production_value_crops": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "production_quantity_crops": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "production_area": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "export_quantity": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "import_quantity": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "apparent_consumption": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "total_value_of_import": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "total_value_of_export": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "political_governance_economic_investments": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "cane_deliveries": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "quantity_of_gok_subsidized_fertilizer": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "gok_fertilizer_subsidy_beneficiaries": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "gok_fertilizer_subsidy_funds_allocated": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    "gok_fertilizer_subsidy_expenditure": {
        "columns": {"time_period": "year", "domain_name": "metric", "item_name": "item", "data_value": "value"},
        "order": ["year", "area_level", "area_name", "metric", "item", "value"],
    },
    # Central Bank
    "monetary_survey": {
        "columns": {"indicator": "metric"},
        "order": ["section", "metric", "year", "month", "value"],
    },
    "bop_annual": {
        "columns": {"category": "metric"},
        "order": ["year", "metric", "value"],
    },
    "gdp_quarterly": {
        "columns": {"activity": "metric"},
        "order": ["year", "quarter", "metric", "value"],
    },
    # IEBC (HF has .pdf suffix; push to clean name)
    "rov_per_polling_station.pdf": {
        "columns": {"registered_voters": "value"},
        "order": None,
        "push_name": "rov_per_polling_station",
    },
}


def migrate_config(config_name, rename_spec):
    try:
        logger.info(f"Loading config '{config_name}' from {REPO_ID}")
        dataset = load_dataset(REPO_ID, config_name, token=TOKEN, split="train")
        df = dataset.to_pandas()
        original_cols = list(df.columns)
        logger.info(f"  Columns before: {original_cols}")

        rename_map = rename_spec["columns"]
        has_changes = any(c in df.columns for c in rename_map)
        if not has_changes:
            logger.info(f"  SKIP: no columns to rename (already migrated?)")
            return

        df = df.rename(columns=rename_map)

        new_order = rename_spec.get("order")
        if new_order:
            existing = [c for c in new_order if c in df.columns]
            rest = [c for c in df.columns if c not in existing]
            df = df[existing + rest]

        logger.info(f"  Columns after:  {list(df.columns)}")
        logger.info(f"  Rows: {len(df)}")

        push_name = rename_spec.get("push_name", config_name)
        logger.info(f"  Pushing to HuggingFace as '{push_name}'...")
        Dataset.from_pandas(df).push_to_hub(
            REPO_ID, config_name=push_name, token=TOKEN, private=False
        )
        logger.info(f"  Done.")
    except Exception:
        logger.exception(f"  FAILED config '{config_name}'")


def run():
    if not REPO_ID:
        logger.error("HF_REPO_ID is not set")
        sys.exit(1)

    logger.info(f"Migrating columns in {REPO_ID}")
    for config_name, spec in RENAME_MAP.items():
        migrate_config(config_name, spec)


if __name__ == "__main__":
    run()
