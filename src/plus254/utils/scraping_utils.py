import pandas as pd
import io
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote
import logging
import pdfplumber
import pandas as pd
from tqdm import tqdm


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.getLogger("pdfminer").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


def scrape_url(url):
    try:
        logger.info("Fetching statistics page")
        page = requests.get(url, verify = False)
        page.raise_for_status()
        logger.info("Page fetched successfully")
        return BeautifulSoup(page.content, "html.parser")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch page: {e}")
        raise


def extract_pdf(soup, url=None, name=None):
    try:
        logger.info("Extracting PDF link")
        pdf_file = None
        if name:
            pdf_file = soup.find_all("a", title=name)
        if not pdf_file and soup.find_all("a", class_="download-link"):
            pdf_file = soup.find_all("a", class_="download-link")
        if not pdf_file:
            raise ValueError("No download link found in HTML")
        href = pdf_file[0]["href"].strip()
        pdf_name = href.split("/")[-1]
        if href.startswith("http"):
            pdf_url = href
        else:
            pdf_url = f"{url}/{quote(href, safe='/')}"
        logger.info(f"PDF found: {pdf_name}")
        logger.info(f"Downloading: {pdf_url}")
        response = requests.get(pdf_url, stream=True, verify=False, timeout=120)
        response.raise_for_status()
        logger.info(f"PDF downloaded successfully ({len(response.content) / 1024:.1f} KB)")
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


def extract_table(pdf_bytes, page_num=None):
    try:
        logger.info("Parsing PDF table")
        all_rows = []
        header = None
        with pdfplumber.open(pdf_bytes) as pdf:
            total_pages = len(pdf.pages)
            if page_num is not None:
                if page_num < 1 or page_num > total_pages:
                    raise ValueError(f"Page {page_num} out of range (1-{total_pages})")
                pages = [pdf.pages[page_num - 1]]
                logger.info(f"Extracting from page {page_num} of {total_pages}")
            else:
                pages = pdf.pages
                logger.info(f"PDF has {total_pages} pages")
            for i, page in enumerate(tqdm(pages, desc="Extracting tables", disable=None)):
                table = page.extract_table()
                if not table:
                    continue
                if header is None:
                    header = table[0]
                    all_rows.extend(table[1:])
                else:
                    rows = [r for r in table[1:] if r != header]
                    all_rows.extend(rows)
        if header is None:
            raise ValueError("No table found in PDF")
        df = pd.DataFrame(all_rows, columns=header)
        logger.info(f"Table extracted: {len(df)} rows")
        return df
    except Exception as e:
        logger.error(f"Failed to parse PDF: {type(e).__name__}: {e}")
        raise