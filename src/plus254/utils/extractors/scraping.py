import logging
from typing import Optional
import pandas as pd
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


def fetch_soup(
    url: str,
    parser: str = "html.parser",
    timeout: int = 30,
    **kwargs,
) -> BeautifulSoup:
    """Fetch a URL and return a BeautifulSoup object.

    Accepts additional requests.get() kwargs (headers, verify, params, etc.).
    """
    try:
        logger.info("Fetching page: %s", url)
        resp = requests.get(url, timeout=timeout, **kwargs)
        resp.raise_for_status()
        logger.info("Page fetched successfully (%d bytes)", len(resp.content))
        return BeautifulSoup(resp.content, parser)
    except requests.RequestException:
        logger.exception("Failed to fetch page: %s", url)
        raise


def parse_html_table(
    table,
    header_row: int = 0,
    strip: bool = True,
) -> pd.DataFrame:
    """Extract a DataFrame from an HTML <table> tag or BeautifulSoup Tag.
    """
    rows = table.find_all("tr")
    if not rows:
        raise ValueError("Table has no <tr> rows")

    text = (lambda t: t.get_text(strip=strip)) if strip else (lambda t: t.get_text())

    headers = [text(th) for th in rows[header_row].find_all("th")]

    data = []
    for row in rows[header_row + 1 :]:
        cells = [text(td) for td in row.find_all(["td", "th"])]
        if cells:
            data.append(cells)

    ncols = len(headers)
    if data and any(len(r) != ncols for r in data):
        logger.warning(
            "Column count mismatch: header has %d columns, normalizing rows", ncols
        )
        normalized = []
        for r in data:
            if len(r) < ncols:
                normalized.append(r + [None] * (ncols - len(r)))
            elif len(r) > ncols:
                normalized.append(r[:ncols])
            else:
                normalized.append(r)
        data = normalized

    df = pd.DataFrame(data, columns=headers)
    logger.info("Table extracted: %d rows x %d columns", len(df), len(df.columns))
    return df


def table_from_url(
    url: str,
    table_id: Optional[str] = None,
    table_class: Optional[str] = None,
    table_index: int = 0,
    header_row: int = 0,
    strip: bool = True,
    **kwargs,
) -> pd.DataFrame:
    """One-shot: fetch a URL and extract an HTML table as a DataFrame.
    """
    soup = fetch_soup(url, **kwargs)

    if table_id:
        table = soup.find("table", id=table_id)
        if not table:
            raise ValueError(f"No <table> found with id='{table_id}' at {url}")
    elif table_class:
        table = soup.find("table", class_=table_class)
        if not table:
            raise ValueError(f"No <table> found with class='{table_class}' at {url}")
    else:
        tables = soup.find_all("table")
        if not tables:
            raise ValueError(f"No <table> elements found at {url}")
        if table_index >= len(tables):
            raise ValueError(
                f"Table index {table_index} out of range ({len(tables)} tables found)"
            )
        table = tables[table_index]

    return parse_html_table(table, header_row=header_row, strip=strip)


def tables_from_url(
    url: str,
    header_row: int = 0,
    strip: bool = True,
    **kwargs,
) -> list[pd.DataFrame]:
    """Fetch a URL and extract *all* HTML tables as a list of DataFrames."""
    soup = fetch_soup(url, **kwargs)
    tables = soup.find_all("table")
    if not tables:
        raise ValueError(f"No <table> elements found at {url}")
    return [
        parse_html_table(t, header_row=header_row, strip=strip) for t in tables
    ]

