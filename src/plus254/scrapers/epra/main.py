from plus254.scrapers.epra.parsers import fuel_prices
from plus254.utils.scraping import table_from_url
from plus254.utils.hf import save_to_hf
from dotenv import load_dotenv
import logging
import time
from pathlib import Path

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def run():
    logger.info("EPRA scraper started")
    start = time.time()
    url = 'https://www.epra.go.ke/pump-prices'
    try:
        df = table_from_url(url, table_id='datatable')
        name, df_clean = fuel_prices(df)
        logger.info("Saving dataset to hf")
        yaml_path = Path(__file__).parent / "datasets.yaml"
        save_to_hf(df_clean, config_name=name, overwrite=False, yaml_path=yaml_path)
        logger.info(f"Completed in {time.time() - start:.1f}s")
    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run()