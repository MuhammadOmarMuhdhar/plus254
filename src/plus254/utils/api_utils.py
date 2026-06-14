import logging
import time
from datetime import datetime

import requests

logger = logging.getLogger(__name__)


def check_freshness(session, url, stored_date=None, params=None, date_field="updated_at"):
    if stored_date is None:
        return True
    try:
        stored_dt = datetime.fromisoformat(stored_date)
    except ValueError:
        return True

    p = dict(params or {})
    p.setdefault("page_size", 1)

    try:
        r = session.get(url, params=p, timeout=30)
        r.raise_for_status()
        data = r.json()
    except Exception:
        logger.exception("Failed to check for new data")
        return True

    if not data.get("results"):
        return False

    api_latest = max(
        rec[date_field] for rec in data["results"] if rec.get(date_field)
    )
    api_dt = datetime.fromisoformat(api_latest).replace(tzinfo=None)

    return api_dt > stored_dt


def fetch_paginated(session, start_url, params=None, stored_date=None,
                    date_field="updated_at", max_retries=5, timeout=30, delay=2):
    results = []
    url = start_url
    page = 1

    stored_dt = None
    if stored_date:
        try:
            stored_dt = datetime.fromisoformat(stored_date)
        except ValueError:
            pass

    while url:
        retries = 0
        while True:
            try:
                r = session.get(
                    url, params=params if page == 1 else None, timeout=timeout
                )

                if r.status_code == 429:
                    wait = int(r.headers.get("Retry-After", 60))
                    logger.warning(f"Rate limited on page {page}. Waiting {wait}s...")
                    time.sleep(wait)
                    retries += 1
                    if retries > max_retries:
                        raise RuntimeError(
                            f"Too many rate-limit retries on page {page}"
                        )
                    continue

                r.raise_for_status()
                break

            except requests.exceptions.RequestException as e:
                retries += 1
                if retries > max_retries:
                    raise RuntimeError(
                        f"Failed page {page} after {max_retries} retries: {e}"
                    )
                wait = 2 ** retries
                logger.warning(f"Error on page {page}: {e}. Retrying in {wait}s...")
                time.sleep(wait)

        d = r.json()
        results.extend(d["results"])
        logger.info(f"Page {page}: {len(results)}/{d['count']} records")

        if stored_dt and d["results"]:
            all_older = all(
                datetime.fromisoformat(rec[date_field]).replace(tzinfo=None) <= stored_dt
                for rec in d["results"]
                if rec.get(date_field)
            )
            if all_older:
                logger.info(
                    f"  All records on page {page} are older than stored date. Stopping."
                )
                break

        url = d.get("next")
        page += 1
        time.sleep(delay)

    return results
