import logging
import time
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from plus254.utils.hf_utils import save_to_hf
from plus254.utils.scraping_utils import scrape_url, extract_pdf, extract_table
from plus254.scrapers.iebc.voters import process_registered_voters


load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

def run():
    logger.info("IEBC scraper started")
    start = time.time()
    try:
        soup = scrape_url("https://www.iebc.or.ke/registration/?Statistics_of_Voter_2022")
        pdf_bytes, pdf_name  = extract_pdf(soup, "https://www.iebc.or.ke/docs/", "Registered Voters per Polling Station" )
        df = extract_table(pdf_bytes)
        procesed_df = process_registered_voters(df)
        logger.info(f"Saving {pdf_name} to hf")
        save_to_hf(procesed_df, config_name=pdf_name.replace(".pdf", ""), overwrite=False, yaml_path=Path(__file__).parent / "datasets.yaml")
        logger.info(f"Completed in {time.time() - start:.1f}s")
    except Exception:
        logger.exception("Pipeline failed")
        raise

if __name__ == "__main__":
    run()
