import logging
import re
import time
from datetime import datetime
from pathlib import Path

import pandas as pd
import requests
import yaml
from dotenv import load_dotenv
from plus254.utils.api_utils import check_freshness, fetch_paginated
from plus254.utils.df_utils import (
    clean_numeric_values,
    lowercase_values,
    normalize_columns,
    snake_case_columns,
)
from plus254.utils.hf_utils import save_to_hf

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

BASE_URL = "https://statistics.kilimo.go.ke/api"
YAML_PATH = Path(__file__).parent / "datasets.yaml"

session = requests.Session()
session.headers.update({
    "Accept": "application/json",
    "Accept-Language": "en",
    "User-Agent": "plus254.co.ke"
})


def read_stored_date():
    if not YAML_PATH.exists():
        return None
    with open(YAML_PATH) as f:
        raw = yaml.safe_load(f)
    if raw and "kilimo" in raw:
        return raw["kilimo"].get("last_updated")
    return None


def update_yaml_timestamp():
    now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    with open(YAML_PATH) as f:
        raw = yaml.safe_load(f)
    if raw and "kilimo" in raw:
        raw["kilimo"]["last_updated"] = now
        with open(YAML_PATH, "w") as f:
            yaml.dump(raw, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        logger.info(f"Updated last_updated in {YAML_PATH}")


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s-]+", "_", text)
    return text.strip("_")


def run():
    logger.info("Kilimo scraper started")
    start = time.time()

    try:
        stored_date = read_stored_date()

        if not check_freshness(session, f"{BASE_URL}/data/",
                               stored_date=stored_date, params={"page_size": 1}):
            logger.info("No new data available — skipping")
            return

        logger.info("New data available — fetching all records")
        raw_data = fetch_paginated(
            session, f"{BASE_URL}/data/",
            params={"page_size": 50},
            stored_date=None,
        )

        df = pd.DataFrame(raw_data)
        indicators = list(df["indicator_name"].unique())
        logger.info(f"Fetched {len(df)} rows, {len(indicators)} indicators")

        for item in indicators:

            if item == "Poulation": 
                continue
            
            indicator_df = df[df["indicator_name"] == item].reset_index(drop=True)
            indicator_df = normalize_columns(indicator_df)
            indicator_df = clean_numeric_values(indicator_df, "item")
            indicator_df = lowercase_values(indicator_df)
            indicator_df = snake_case_columns(indicator_df)
            indicator_df["area_level"] = indicator_df["area_level"].replace("admin_1", "county")
            indicator_df = indicator_df.rename(columns={
                "time_period": "year",
                "domain_name": "metric",
                "item_name": "item",
                "data_value": "value",
            })
            indicator_df = indicator_df[["year", "area_level", "area_name", "metric", "item", "value"]]

            config_name = slugify(item)
            logger.info(f"Saving '{item}' as '{config_name}' ({len(indicator_df)} rows)")
            save_to_hf(indicator_df, config_name=config_name, overwrite=False)

        update_yaml_timestamp()
        logger.info(f"Completed in {time.time() - start:.1f}s")

    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run()
