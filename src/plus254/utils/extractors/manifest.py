import logging
from collections import defaultdict
from pathlib import Path
from typing import Any

import yaml

from plus254.utils.extractors import html, pdf

logger = logging.getLogger(__name__)


def _group_by_download_page(
    manifest: list[dict],
    page_field: str = "download_page",
) -> dict[int, list[dict]]:
    """Group manifest reports by their download page field."""
    groups: dict[int, list[dict]] = defaultdict(list)
    for report in manifest:
        groups[report.get(page_field, 0)].append(report)
    return dict(groups)


def _process_report(report: dict, soup, base_url: str) -> list[dict]:
    """Download a single PDF and extract all tables specified in the report."""
    pdf_name = report["pdf_name"]
    year = report["year"]
    quarter = report["quarter"]
    records: list[dict[str, Any]] = []

    pdf_url = report.get("pdf_url", base_url)
    try:
        pdf_bytes, _ = pdf.download_pdf(soup, url=pdf_url, name=pdf_name)
    except Exception:
        logger.warning(f"[{pdf_name}] Download failed — skipping")
        return records

    for spec in report.get("tables", []):
        dataset = spec["dataset"]
        page_num = spec.get("pdf_page_num")
        search_term = spec.get("search_term")
        return_all = spec.get("return_all", False)

        if page_num is None:
            logger.warning(
                f"[{pdf_name}] {dataset}: pdf_page_num is null — skipping"
            )
            continue

        try:
            result = pdf.extract_pdf_table(
                pdf_bytes,
                page_num=page_num,
                pick_table_with=search_term,
                return_all=return_all,
            )
        except Exception as e:
            logger.warning(
                f"[{pdf_name}] {dataset}: extraction failed ({e}) — skipping"
            )
            continue

        dfs = result if isinstance(result, list) else [result]
        for table_index, raw_df in enumerate(dfs):
            records.append({
                "year": year,
                "quarter": quarter,
                "dataset": dataset,
                "table_index": table_index,
                "raw_df": raw_df,
            })
            logger.info(
                f"[{pdf_name}]  → {dataset}[{table_index}] ({len(raw_df)} rows)"
            )

    return records


def extract_from_manifest(
    manifest_path: str | Path,
    base_url: str,
    page_field: str = "download_page",
    slugs: set[str] | None = None,
) -> list[dict]:
    """Generic manifest-driven PDF extraction for rolling sources.

    Loads the manifest YAML, groups reports by download page, fetches each
    page, downloads PDFs, and extracts tables. Returns records consumable by
    transform functions.

    If *slugs* is provided, only reports whose tables reference at least one
    of the given dataset slugs are processed, and within each report only
    the matching table specs are extracted.
    """
    with open(manifest_path) as f:
        manifest = yaml.safe_load(f)

    total_pdfs = len(manifest)
    all_records: list[dict[str, Any]] = []
    page_groups = _group_by_download_page(manifest, page_field=page_field)

    pdf_counter = 0
    for download_page, reports in page_groups.items():
        page_prefix = f"[page {download_page}]"
        needs_page = any("pdf_url" not in r for r in reports)

        if needs_page:
            logger.info(
                f"{page_prefix} Fetching page (hosts {len(reports)} PDFs) — "
                f"[{pdf_counter + 1}–{pdf_counter + len(reports)}/{total_pdfs}]"
            )

            try:
                soup = html.fetch_soup(f"{base_url}?page={download_page}")
            except Exception as e:
                logger.warning(
                    f"{page_prefix} Page fetch failed: {e} — "
                    f"skipping all {len(reports)} PDFs on this page"
                )
                pdf_counter += len(reports)
                continue
        else:
            soup = None
            logger.info(
                f"{page_prefix} Direct URLs only ({len(reports)} PDFs) — "
                f"[{pdf_counter + 1}–{pdf_counter + len(reports)}/{total_pdfs}]"
            )

        for report in reports:
            pdf_counter += 1

            if slugs is not None:
                needed_tables = [
                    t for t in report.get("tables", [])
                    if t.get("dataset") in slugs
                ]
                if not needed_tables:
                    logger.info(
                        f"[{report['pdf_name']}] No needed tables — skipping"
                    )
                    continue
                report = {**report, "tables": needed_tables}

            log_prefix = f"[{report['pdf_name']}]"

            logger.info(
                f"{log_prefix} Downloading ({report['year']} Q{report['quarter']}) — "
                f"[{pdf_counter}/{total_pdfs}]"
            )

            records = _process_report(report, soup, base_url)
            all_records.extend(records)

            total_tables = len(report.get("tables", []))
            extracted = len(records)
            skipped = total_tables - sum(
                1 for t in report.get("tables", [])
                if t.get("pdf_page_num") is not None
            )
            skipped = max(0, total_tables - extracted)
            logger.info(
                f"{log_prefix} Done. Extracted {extracted}/{total_tables} tables, "
                f"skipped {skipped}"
            )

    logger.info(
        f"Extraction complete. {len(all_records)} total records "
        f"from {total_pdfs} PDFs."
    )
    return all_records
