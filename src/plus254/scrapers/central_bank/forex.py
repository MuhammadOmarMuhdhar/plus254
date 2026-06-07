import pandas as pd
from plus254.utils.df_utils import (
    normalize_columns,
    convert_month_to_name,
    set_month_categorical,
    capitalize_columns,
)


def process_forex_df(df_dict):
    df_results = {}

    for forex_df in ["forex_end_period", "forex_period_average"]:
        df = df_dict[forex_df]

        df.columns = df.iloc[0]
        df = normalize_columns(df)
        df = df.iloc[1:].reset_index(drop=True)
        df["year"] = df["year"].astype(int)
        df = convert_month_to_name(df, "month")
        df_long = df.melt(
            id_vars=["year", "month"],
            var_name="metric",
            value_name="value",
        )
        df_long = set_month_categorical(df_long, "month")
        df_long = df_long.sort_values(["year", "month"]).reset_index(drop=True)
        df_long = capitalize_columns(df_long)
        df_results[forex_df] = df_long

    return df_results
