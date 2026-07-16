from plus254.utils.transformers import tidy, frame
import pandas as pd

def transform(df):
    id_vars = ["year", "month"]

    return (
        df.copy()
        .pipe(
            frame._promote_header_row, 1, 2
            )
        .pipe(tidy._normalize_column_names)
        .dropna()
        .assign(year=lambda d: d["year"].astype(int), month=lambda d: d["month"].astype(int))
        .pipe(tidy._month_int_to_name, month_col="month")
        .pipe(lambda d: d.melt(
            id_vars=id_vars,
            value_vars=[c for c in d.columns if c not in id_vars + ['total']],
            var_name="item",
            value_name="value"
        ))
        .pipe(tidy._tidy, value_col="value", month_col="month")
        .reset_index(drop=True)
    )