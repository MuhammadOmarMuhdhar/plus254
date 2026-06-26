import time
from pathlib import Path

import logging
from dotenv import load_dotenv
from plus254.utils.hf import save_to_hf
from plus254.scrapers.teaboard.parsers import process_tea_auction_table
from plus254.utils.pdf import fetch_page_soup, download_pdf

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

BASE_URL = "https://eatta.co.ke"


def run():
    logger.info("Tea scraper started")
    start = time.time()
    try:
        soup = fetch_page_soup(f"{BASE_URL}/statistics")
        pdf_bytes, pdf_name = download_pdf(soup, url=BASE_URL)
        df = process_tea_auction_table(pdf_bytes)
        save_to_hf(df, config_name="tea", save_csv=True, csv_filename="tea.csv", overwrite=False, yaml_path=Path(__file__).parent / "datasets.yaml")
        logger.info(f"Completed in {time.time() - start:.1f}s")
    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run()
