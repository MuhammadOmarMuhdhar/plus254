import logging
from typing import List
import pandas as pd

logger = logging.getLogger(__name__)


def upsert(existing: pd.DataFrame,
           new: pd.DataFrame,
           natural_keys: List[str]) -> pd.DataFrame:
    """
    Merge *new* rows into *existing*.
    New rows overwrite existing rows on natural-key collision.
    """
    if new.empty:
        return existing.copy()

    if existing.empty:
        return new.copy()

    for name, frame in (("existing", existing), ("new", new)):
        missing = [k for k in natural_keys if k not in frame.columns]
        if missing:
            raise ValueError(f"{name} DataFrame missing natural keys: {missing}")

    existing_keys = existing.set_index(natural_keys).index
    new_keys = new.set_index(natural_keys).index
    mask = existing_keys.isin(new_keys)

    untouched = existing[~mask]
    result = pd.concat([untouched, new], ignore_index=True)

    replaced = mask.sum()
    logger.info(
        f"Upsert: {len(existing)} existing + {len(new)} new "
        f"→ {len(result)} final ({replaced} replaced, {len(untouched)} kept)"
    )

    return result
