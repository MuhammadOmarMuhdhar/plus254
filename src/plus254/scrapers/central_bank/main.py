import logging
import time
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from plus254.utils.hf_utils import save_to_hf
from plus254.scrapers.central_bank import central_bank_links
from plus254.scrapers.central_bank.forex import process_forex
from plus254.scrapers.central_bank.monetary import process_monetary_survey
from plus254.scrapers.central_bank.bop import process_bop_annual
from plus254.scrapers.central_bank.trade import (
    process_exports_global,
    process_exports_africa,
    process_domestic_exports,
    process_imports_global,
    process_imports_africa,
    process_imports_commodity,
    process_principal_exports,
)
from plus254.scrapers.central_bank.fiscal import process_fiscal_revenue_expenditure
from plus254.scrapers.central_bank.debt import process_public_debt, process_domestic_debt
from plus254.scrapers.central_bank.gdp import process_gdp_quarterly

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


PROCESSORS = {
    "forex": process_forex,
    "monetary_survey": process_monetary_survey,
    "bop_annual": process_bop_annual,
    "exports_global": process_exports_global,
    "exports_africa": process_exports_africa,
    "domestic_exports": process_domestic_exports,
    "imports_global": process_imports_global,
    "imports_africa": process_imports_africa,
    "imports_commodity": process_imports_commodity,
    "principal_exports": process_principal_exports,
    "fiscal_revenue_expenditure": process_fiscal_revenue_expenditure,
    "public_debt": process_public_debt,
    "domestic_debt": process_domestic_debt,
    "gdp_quarterly": process_gdp_quarterly,
}


def fetch_all():
    logger.info(f"Fetching {len(central_bank_links)} CSV tables")
    df_dict = {}
    for name, url in central_bank_links.items():
        logger.info(f"Fetching: {name}")
        try:
            df_dict[name] = pd.read_csv(url)
        except Exception:
            logger.exception(f"Failed to fetch {name}")
            raise
    return df_dict


def run_all(df_dict):
    results = {}
    for name, processor in PROCESSORS.items():
        logger.info(f"Processing: {name}")
        try:
            result = processor(df_dict)
            if name == "forex":
                results["forex_end_period"] = result["forex_end_period"]
                results["forex_period_average"] = result["forex_period_average"]
            elif name == "fiscal_revenue_expenditure":
                results["fiscal_revenue"] = result["revenue"]
                results["fiscal_grants"] = result["grants"]
                results["fiscal_expenditure"] = result["expenditure"]
            else:
                results[name] = result
        except Exception:
            logger.exception(f"Failed to process {name}")
            raise
    return results


def run():
    logger.info("Central Bank scraper started")
    start = time.time()
    try:
        df_dict = fetch_all()
        results = run_all(df_dict)
        logger.info(f"Saving {len(results)} datasets")
        yaml_path = Path(__file__).parent / "datasets.yaml"
        for name, df in results.items():
            save_to_hf(df, config_name=name, overwrite=False, yaml_path=yaml_path)
        logger.info(f"Completed in {time.time() - start:.1f}s")
    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run()
