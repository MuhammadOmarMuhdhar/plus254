from plus254.utils.transformers import tidy, frame
import pandas as pd


def transform(df):
    id_vars = ["year", "month"]

    return (
        df.copy()
        .pipe(
            frame.promote_header_row, 2, 3
            )
        .pipe(tidy.normalize_column_names)
        .dropna()
        .assign(year=lambda d: d["year"].astype(int), month=lambda d: d["month"].astype(int))
        .pipe(tidy.month_int_to_name, month_col="month")
        .pipe(lambda d: d.melt(
            id_vars=id_vars,
            value_vars=[c for c in d.columns if c not in id_vars + ['total']],
            var_name="item",
            value_name="value"
        ))
        .pipe(tidy.tidy)
        .reset_index(drop=True)
    )