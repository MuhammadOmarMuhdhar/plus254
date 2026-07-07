from typing import Any
import pandas as pd

def check_duplicates(df: pd.DataFrame, natural_keys: list[str]) -> dict[str, Any]:
    """
    Check for duplicate rows based on natural keys.

    Returns
    -------
    dict with keys: passed (bool), duplicate_count (int), duplicate_rows (DataFrame|None)
    """
    duplicates = df[df.duplicated(subset=natural_keys, keep=False)]
    dup_count = len(duplicates)
    return {
        "passed": dup_count == 0,
        "duplicate_count": dup_count,
        "duplicate_rows": duplicates if dup_count > 0 else None,
    }