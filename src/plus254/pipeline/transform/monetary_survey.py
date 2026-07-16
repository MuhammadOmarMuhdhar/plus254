import numpy as np
import pandas as pd
from plus254.utils.transformers import tidy, prune

def transform(df: pd.DataFrame) -> pd.DataFrame:
    date_cols = prune._build_date_columns(df)

    SECTION_MAP = {
        "A.": "Central Bank of Kenya",
        "B": "Other Depository Corporation Survey",
        "C": "Depository Corporation Survey",
    }

    return (
        df.copy()
        .set_axis(["section_code", "indicator"] + date_cols, axis=1)
        .iloc[2:]
        .pipe(tidy._normalise_nulls)
        .assign(section_code=lambda d: d["section_code"].ffill())
        .assign(category=lambda d: d["section_code"].map(SECTION_MAP))
        .melt(id_vars=["category", "indicator"], value_vars=date_cols, var_name="period", value_name="value")
        .assign(_date=lambda d: pd.to_datetime(d["period"].str.replace("Sept", "Sep"), format="%Y-%b"))
        .assign(year=lambda d: d["_date"].dt.year, month=lambda d: d["_date"].dt.strftime("%B"))
        .drop(columns=["period", "_date"])
        .rename(columns={"indicator": "item"})
        .pipe(tidy._sort_by_date)
        .pipe(tidy._tidy, value_col="value", month_col="month")
        .assign(year=lambda d: d["year"].astype(int))
        .sort_values(["year", "month","category", "item" ])
        .dropna(subset=["value", "item"])
        .drop_duplicates(keep="last")
        .reset_index(drop=True)
        [["year","month", "category", "item", "value"]]
    )