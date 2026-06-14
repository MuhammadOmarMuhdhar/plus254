import io
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import logging
import pdfplumber
import pandas as pd
from dotenv import load_dotenv
from plus254.utils.hf_utils import save_to_hf
from plus254.utils.df_utils import clean_numeric_values, set_month_categorical, snake_case_columns, lowercase_values

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

BASE_URL = "https://eatta.co.ke"


def scrape_eatta():
    """scrapes: https://eatta.co.ke/statistics"""
    try:
        logger.info("Fetching statistics page")
        page = requests.get(f"{BASE_URL}/statistics")
        page.raise_for_status()
        logger.info("Page fetched successfully")
        return BeautifulSoup(page.content, "html.parser")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch page: {e}")
        raise


def extract_pdf(soup):
    try:
        logger.info("Extracting PDF link")
        pdf_file = soup.find_all("a", class_="download-link")

        if not pdf_file:
            raise ValueError("No download link found in HTML")

        href = pdf_file[0]["href"].strip()
        pdf_name = href.split("/")[-1]
        pdf_url = f"{BASE_URL}/{quote(href, safe='/')}"
        logger.info(f"PDF found: {pdf_name}")

        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()
        logger.info("PDF downloaded successfully")
        return io.BytesIO(response.content), pdf_name

    except requests.RequestException as e:
        logger.error(f"Failed to download PDF from {pdf_url}: {e}")
        raise
    except ValueError as e:
        logger.error(f"Invalid PDF link: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in extract_pdf: {type(e).__name__}: {e}")
        raise


def extract_table(pdf_bytes):
    try:
        logger.info("Parsing PDF table")
        with pdfplumber.open(pdf_bytes) as pdf:
            first_page = pdf.pages[0]
            table = first_page.extract_table()
            df = pd.DataFrame(table[1:], columns=table[0])
            df.columns = df.iloc[0]
            df = df.drop(0)
            df = df[
                df["Average price 2026 (USD)"].notna()
                & (df["Average price 2026 (USD)"] != "")
            ]
            df = df[df["Sale week"] != "Grand Total"]

            for column in df.columns:
                if column == "Average price 2026 (USD)":
                    df[column] = (
                        df[column]
                        .str.replace(" ", "", regex=False)
                        .str.replace(",", "", regex=False)
                        .str.replace("%", "", regex=False)
                        .astype("float")
                    )
                else:
                    df[column] = (
                        df[column]
                        .str.replace(" ", "", regex=False)
                        .str.replace(",", "", regex=False)
                        .str.replace("%", "", regex=False)
                        .str.replace("WEEK", "", regex=False)
                        .astype("int")
                    )

            df["Date"] = pd.to_datetime("2026-01-01") + pd.to_timedelta(
                (df["Sale week"] - 1) * 7, unit="D"
            )
            df = df.rename(columns={
                "Average price 2026 (USD)": "Average price (USD)",
                "Tea sold in Kgs 2026": "Tea sold (Kgs)",
                "Tea offered in Kgs 2026": "Tea offered (Kgs)",
                "Unsold Teas in % 2026": "Unsold tea (%)",
            })

            metric_cols = ["Average price (USD)", "Tea sold (Kgs)", "Tea offered (Kgs)", "Unsold tea (%)"]
            df = df.melt(
                id_vars=["Date", "Sale week"],
                value_vars=metric_cols,
                var_name="Metric",
                value_name="Value",
            )

            df = clean_numeric_values(df, "Value")
            df["Year"] = df["Date"].dt.year.astype(int)
            df["Month"] = df["Date"].dt.month_name()
            df = lowercase_values(df)
            df = snake_case_columns(df)
            df = df.sort_values(["date", "sale_week", "metric"]).reset_index(drop=True)
            df = set_month_categorical(df, "month")
            df = df.loc[:, ~df.columns.str.startswith("__")]
            df = df[["date", "year", "month", "sale_week", "metric", "value"]]

        logger.info(f"Table extracted: {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Failed to parse PDF: {type(e).__name__}: {e}")
        raise


def run():
    logger.info("Tea scraper started")
    start = time.time()
    try:
        soup = scrape_eatta()
        pdf_bytes, pdf_name = extract_pdf(soup)
        df = extract_table(pdf_bytes)
        save_to_hf(df, config_name="tea", save_csv=True, csv_filename="tea.csv", overwrite=False, yaml_path=Path(__file__).parent / "datasets.yaml")
        logger.info(f"Completed in {time.time() - start:.1f}s")
    except Exception:
        logger.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run()
