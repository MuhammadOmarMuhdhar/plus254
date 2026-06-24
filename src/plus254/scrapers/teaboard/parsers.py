import time
from pathlib import Path

import logging
import pdfplumber
import pandas as pd
from dotenv import load_dotenv
from plus254.utils.tidy import tidy

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


def process_tea_auction_table(pdf_bytes):
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

            df["Year"] = df["Date"].dt.year.astype(int)
            df["Month"] = df["Date"].dt.month_name()
            df = tidy(df, value_col="Value", month_col="Month")
            df = df.sort_values(["date", "sale_week", "metric"]).reset_index(drop=True)
            df = df.loc[:, ~df.columns.str.startswith("__")]
            df = df[["date", "year", "month", "sale_week", "metric", "value"]]

        logger.info(f"Table extracted: {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Failed to parse PDF: {type(e).__name__}: {e}")
        raise
