from src.plus254.utils.transformers import tidy
import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Shared logic for both end-period and period-average forex."""
    return (
        df.copy()
        .pipe(lambda d: d.set_axis(d.iloc[0].tolist(), axis=1))
        .iloc[1:]
        .pipe(tidy.month_int_to_name, month_col="Month")
        .melt(id_vars=["Year", "Month"], var_name="item", value_name="value")
        .pipe(tidy.tidy, value_col="value", month_col="Month")
        .sort_values(["year", "month"])
        .assign(year=lambda d: d["year"].astype(int))
        .reset_index(drop=True)
    )
