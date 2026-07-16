from plus254.utils.transformers import tidy
import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Parse quarterly GDP CSV into canonical format."""
    years = df.iloc[1, 2:].ffill().bfill().astype(int).values
    quarters = df.iloc[2, 2:].values
    quarters = [int(q.replace('Q', '')) for q in quarters]
    date_cols = [f"{y}-{q}" for y, q in zip(years, quarters)]
    return (
        df.copy()
        .set_axis(["0", "activity"] + date_cols, axis=1)
        .iloc[3:]
        .pipe(tidy._normalise_nulls)
        .dropna(subset=["activity"], how="all")
        .melt(id_vars=["activity"], var_name="period", value_name="value")
        .assign(
            year=lambda d: d["period"].str.split("-", expand=True)[0].astype(int),
            quarter=lambda d: d["period"].str.split("-", expand=True)[1].str.strip(),
        )
        .drop(columns=["period"])
        .rename(columns={"activity": "item"})
        .pipe(tidy._tidy, value_col="value")
        .assign(
            year=lambda d: d["year"].astype(int),
            quarter=lambda d: d["quarter"].astype(int)
        )
        .reset_index(drop=True)
        [["year", "quarter", "item", "value"]]
    )
