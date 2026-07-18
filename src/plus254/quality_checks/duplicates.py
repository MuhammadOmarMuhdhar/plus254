from typing import Any
import pandas as pd

def check_duplicates(df: pd.DataFrame) -> dict[str, Any]:
    """Check for duplicate rows. """
    duplicates = df[df.duplicated(keep=False)]
    dup_count = len(duplicates)
    return {
        "passed": dup_count == 0,
        "duplicate_count": dup_count,
        "duplicate_rows": duplicates if dup_count > 0 else None,
    }