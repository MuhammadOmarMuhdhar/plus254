from plus254.utils.transformers import tidy, frame
import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.copy()
        .pipe(frame._promote_header_row, 2, 3)
        .pipe(lambda d: d.set_axis(
            ['year', 'month'] + d.columns[2:].tolist(), axis=1
        ))
        .assign(year=lambda d: d["year"].astype(int), month=lambda d: d["month"].astype(int))
        .pipe(tidy._month_int_to_name, month_col="month")
        .pipe(
            lambda d: d.melt(
                id_vars=["year", "month"],
                value_vars=[c for c in d.columns if c not in ["year", "month"] + [ ' Total ' ]],
                var_name="item",
                value_name="value"
            )
        )
        .pipe(tidy._tidy)
        .reset_index(drop=True)
    )