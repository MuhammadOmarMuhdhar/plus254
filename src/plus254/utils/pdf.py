import pandas as pd
import io
import requests
from bs4 import BeautifulSoup
import logging
import pdfplumber
from tqdm import tqdm
from urllib.parse import urljoin

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logging.getLogger("pdfminer").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


def _fetch_page_soup(url, verify=False):
    try:
        logger.info("Fetching page: %s", url)
        page = requests.get(url, verify=verify)
        page.raise_for_status()
        logger.info("Page fetched successfully")
        return BeautifulSoup(page.content, "html.parser")
    except requests.RequestException as e:
        logger.error(f"Failed to fetch page: {e}")
        raise


def _download_pdf(soup, url=None, name=None):
    try:
        logger.info("Extracting PDF link")
        pdf_file = None
        if name:
            pdf_file = [a for a in soup.find_all("a") if a.get("title") and a["title"].strip() == name]
        if not pdf_file and soup.find_all("a", class_="download-link"):
            pdf_file = soup.find_all("a", class_="download-link")
        if not pdf_file:
            raise ValueError("No download link found in HTML")
        href = pdf_file[0]["href"].strip()
        pdf_name = href.split("/")[-1]
        pdf_url = urljoin(url, href) if url else href
        logger.info(f"PDF found: {pdf_name}")
        logger.info(f"Downloading: {pdf_url}")
        response = requests.get(pdf_url, stream=True, verify=False, timeout=120)
        response.raise_for_status()
        if not response.content.startswith(b"%PDF"):
            raise ValueError(f"Downloaded content is not a PDF (starts with {response.content[:30]})")
        logger.info(f"PDF downloaded successfully ({len(response.content) / 1024:.1f} KB)")
        return io.BytesIO(response.content), pdf_name
    except requests.RequestException as e:
        logger.error(f"Failed to download PDF from {pdf_url}: {e}")
        raise
    except ValueError as e:
        logger.error(f"Invalid PDF link: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in download_pdf: {type(e).__name__}: {e}")
        raise


def _extract_pdf_table(
    pdf_bytes,
    page_num=None,
    explicit_vertical_lines=None,
    pick_table_with=None,
    horizontal_strategy="lines",
    snap_tolerance=3,
    join_tolerance=3,
    intersection_tolerance=3,
):
    try:
        logger.info("Parsing PDF table")
        all_rows = []
        header = None

        with pdfplumber.open(pdf_bytes) as pdf:
            total_pages = len(pdf.pages)

            if page_num is not None:
                if isinstance(page_num, int):
                    page_num = [page_num]
                for p in page_num:
                    if p < 1 or p > total_pages:
                        raise ValueError(f"Page {p} out of range (1-{total_pages})")
                pages = [pdf.pages[p - 1] for p in page_num]
                logger.info(f"Extracting from pages {list(page_num)} of {total_pages}")
            else:
                pages = pdf.pages
                logger.info(f"PDF has {total_pages} pages")

            if explicit_vertical_lines is not None:
                table_settings = {
                    "vertical_strategy": "explicit",
                    "explicit_vertical_lines": list(explicit_vertical_lines),
                    "horizontal_strategy": horizontal_strategy,
                    "snap_tolerance": snap_tolerance,
                    "join_tolerance": join_tolerance,
                    "intersection_tolerance": intersection_tolerance,
                }

            for page in tqdm(pages, desc="Extracting tables", disable=None):
                if explicit_vertical_lines is not None:
                    table = page.extract_table(table_settings)
                else:
                    tables = page.find_tables()
                    if not tables:
                        continue
                    if pick_table_with:
                        selected = None
                        for t in tables:
                            text = " ".join(
                                str(c) for row in t.extract() for c in row if c
                            )
                            if pick_table_with in text:
                                selected = t
                                break
                        if selected is None:
                            continue
                        table = selected.extract()
                    else:
                        table = tables[0].extract()

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

        # Normalize all rows to match header width (handle merged cells mismatch)
        ncols = len(header)
        normalized = []
        for row in all_rows:
            if len(row) < ncols:
                normalized.append(row + [None] * (ncols - len(row)))
            elif len(row) > ncols:
                normalized.append(row[:ncols])
            else:
                normalized.append(row)
        all_rows = normalized

        df = pd.DataFrame(all_rows, columns=header)
        logger.info(f"Table extracted: {len(df)} rows")
        return df

    except Exception as e:
        logger.error(f"Failed to parse PDF: {type(e).__name__}: {e}")
        raise


def _detect_column_boundaries(pdf_bytes, page_num, min_line_height=10, cluster_tolerance=2):
    with pdfplumber.open(pdf_bytes) as pdf:
        total_pages = len(pdf.pages)
        if page_num < 1 or page_num > total_pages:
            raise ValueError(f"Page {page_num} out of range (1-{total_pages})")

        page = pdf.pages[page_num - 1]

        v_edges = [
            e for e in page.edges
            if e['orientation'] == 'v' and (e['bottom'] - e['top']) >= min_line_height
        ]

        if not v_edges:
            return []

        xs = sorted(set(round(e['x0'], 1) for e in v_edges))

        clusters = []
        for x in xs:
            if not clusters or x - clusters[-1][-1] > cluster_tolerance:
                clusters.append([x])
            else:
                clusters[-1].append(x)

        return [round(sum(c) / len(c), 1) for c in clusters]

