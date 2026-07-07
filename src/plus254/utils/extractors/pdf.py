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


def _trim_continuation_rows(rows):
    """Skip leading empty rows, keep table rows, stop at prose markers."""
    trimmed = []
    started = False
    for row in rows:
        non_empty = [str(c).strip() for c in row if c and str(c).strip()]
        if not non_empty:
            if started:
                trimmed.append(row)
            continue
        started = True
        # Stop at obvious non-table prose
        first = non_empty[0].lower()
        if first.startswith("source:"):
            break
        if "page" in first and any(ch.isdigit() for ch in first):
            break
        trimmed.append(row)
    # Strip trailing empty rows
    while trimmed and not [c for c in trimmed[-1] if c and str(c).strip()]:
        trimmed.pop()
    return trimmed


def _extract_pdf_table(
    pdf_bytes,
    page_num=None,
    explicit_vertical_lines=None,
    pick_table_with=None,
    horizontal_strategy="lines",
    snap_tolerance=3,
    join_tolerance=3,
    intersection_tolerance=3,
    return_all=False,
):
    try:
        logger.info("Parsing PDF table")

        if return_all:
            return _extract_all_pdf_tables(
                pdf_bytes,
                page_num=page_num,
                explicit_vertical_lines=explicit_vertical_lines,
                pick_table_with=pick_table_with,
                horizontal_strategy=horizontal_strategy,
                snap_tolerance=snap_tolerance,
                join_tolerance=join_tolerance,
                intersection_tolerance=intersection_tolerance,
            )

        all_rows = []
        header = None
        match_found = False

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
                table_data = None

                if explicit_vertical_lines is not None:
                    table_data = page.extract_table(table_settings)
                else:
                    tables = page.find_tables()
                    if pick_table_with:
                        selected = None
                        for t in tables:
                            text = " ".join(
                                str(c) for row in t.extract() for c in row if c
                            )
                            if pick_table_with in text:
                                selected = t
                                break

                        if selected is not None:
                            table_data = selected.extract()
                            if not match_found:
                                match_found = True
                        elif match_found:
                            if tables:
                                table_data = tables[0].extract()
                                logger.info("Using first table on continuation page")
                            else:
                                continuation_settings = {
                                    "vertical_strategy": "text",
                                    "horizontal_strategy": "text",
                                    "snap_tolerance": snap_tolerance,
                                    "join_tolerance": join_tolerance,
                                    "intersection_tolerance": intersection_tolerance,
                                }
                                raw_data = page.extract_table(continuation_settings)
                                if raw_data:
                                    table_data = _trim_continuation_rows(raw_data)
                                else:
                                    table_data = None
                                logger.info("Using trimmed text-based extraction on continuation page")
                    else:
                        if tables:
                            table_data = tables[0].extract()

                if not table_data:
                    continue
                if header is None:
                    header = table_data[0]
                    all_rows.extend(table_data[1:])
                else:
                    rows = [r for r in table_data if r != header]
                    all_rows.extend(rows)

        if header is None:
            raise ValueError("No table found in PDF")

        ncols = len(header)

        # Identify "real" column positions from the richest data row on the
        # first page (most non-null values, excluding header-artifact rows
        # that only contain merged-cell sub-headers like.
        # Continuation pages may have fewer columns (no merged-cell artifacts);
        # we spread their values across the correct header positions.
        real_indices = None
        best_row = None
        best_count = 0
        for row in all_rows:
            if len(row) != ncols:
                continue
            non_null = [i for i, v in enumerate(row) if v is not None]
            if len(non_null) > best_count:
                best_count = len(non_null)
                best_row = non_null
        if best_count > 1:
            real_indices = best_row

        normalized = []
        for row in all_rows:
            if (
                real_indices is not None
                and 1 < len(row) <= len(real_indices) < ncols
            ):
                mapped = [None] * ncols
                for i, val in zip(real_indices, row):
                    mapped[i] = val
                normalized.append(mapped)
            elif len(row) < ncols:
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


def _extract_all_pdf_tables(
    pdf_bytes,
    page_num=None,
    explicit_vertical_lines=None,
    pick_table_with=None,
    horizontal_strategy="lines",
    snap_tolerance=3,
    join_tolerance=3,
    intersection_tolerance=3,
):
    """Extract every matching table independently and return a list of DataFrames."""
    all_dfs = []

    with pdfplumber.open(pdf_bytes) as pdf:
        total_pages = len(pdf.pages)

        if page_num is not None:
            if isinstance(page_num, int):
                page_num = [page_num]
            for p in page_num:
                if p < 1 or p > total_pages:
                    raise ValueError(f"Page {p} out of range (1-{total_pages})")
            pages = [pdf.pages[p - 1] for p in page_num]
            logger.info(f"Extracting all tables from pages {list(page_num)} of {total_pages}")
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

        last_match_header = None
        for page in tqdm(pages, desc="Extracting tables", disable=None):
            if explicit_vertical_lines is not None:
                table_data = page.extract_table(table_settings)
                if table_data:
                    header = table_data[0]
                    rows = table_data[1:]
                    ncols = len(header)
                    normalized = [
                        (row + [None] * (ncols - len(row)))[:ncols]
                        for row in rows
                    ]
                    df = pd.DataFrame(normalized, columns=header)
                    all_dfs.append(df)
            else:
                tables = page.find_tables()
                page_matches = []
                match_indices = []

                if pick_table_with:
                    for i, t in enumerate(tables):
                        text = " ".join(str(c) for row in t.extract() for c in row if c)
                        if pick_table_with in text:
                            page_matches.append(t)
                            match_indices.append(i)
                else:
                    if tables:
                        page_matches.append(tables[0])
                        match_indices.append(0)

                # Handle orphan continuation rows that appear BEFORE the first keyword match
                if (
                    last_match_header is not None
                    and all_dfs
                    and pick_table_with
                    and match_indices
                    and match_indices[0] > 0
                ):
                    for i in range(match_indices[0]):
                        orphan_data = tables[i].extract()
                        if not orphan_data:
                            continue
                        orphan_text = " ".join(
                            str(c) for row in orphan_data for c in row if c
                        )
                        if pick_table_with in orphan_text:
                            continue
                        if len(orphan_data) > 3:
                            continue
                        header = last_match_header
                        ncols = len(header)
                        rows = [r for r in orphan_data if r != header]
                        normalized = [
                            (row + [None] * (ncols - len(row)))[:ncols]
                            for row in rows
                        ]
                        new_df = pd.DataFrame(normalized, columns=header)
                        all_dfs[-1] = pd.concat(
                            [all_dfs[-1], new_df], ignore_index=True
                        )
                        logger.info(
                            "Merged orphan continuation rows into last table"
                        )

                if page_matches:
                    for t in page_matches:
                        table_data = t.extract()
                        if not table_data:
                            continue
                        header = table_data[0]
                        rows = [r for r in table_data[1:] if r != header]
                        ncols = len(header)
                        normalized = [
                            (row + [None] * (ncols - len(row)))[:ncols]
                            for row in rows
                        ]
                        df = pd.DataFrame(normalized, columns=header)
                        all_dfs.append(df)
                        last_match_header = header
                elif last_match_header is not None:
                    continuation_settings = {
                        "vertical_strategy": "text",
                        "horizontal_strategy": "text",
                        "snap_tolerance": snap_tolerance,
                        "join_tolerance": join_tolerance,
                        "intersection_tolerance": intersection_tolerance,
                    }
                    raw_data = page.extract_table(continuation_settings)
                    if raw_data:
                        table_data = _trim_continuation_rows(raw_data)
                        if table_data:
                            header = last_match_header
                            ncols = len(header)
                            # On continuation pages every row is data; there is no
                            # repeated header because borders (and often the header
                            # row itself) are missing.
                            rows = table_data
                            normalized = [
                                (row + [None] * (ncols - len(row)))[:ncols]
                                for row in rows
                            ]
                            new_df = pd.DataFrame(normalized, columns=header)
                            if all_dfs:
                                all_dfs[-1] = pd.concat(
                                    [all_dfs[-1], new_df], ignore_index=True
                                )
                                logger.info("Merged continuation rows into last table")
                            else:
                                all_dfs.append(new_df)
                                logger.info(
                                    "Added continuation rows as new table (no prior match)"
                                )

    logger.info(f"Extracted {len(all_dfs)} tables")
    return all_dfs


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
