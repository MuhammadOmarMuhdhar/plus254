import pandas as pd
from plus254.utils.tidy import tidy, normalize_column_names, month_int_to_name


def process_forex(df_dict):
    df_results = {}

    for forex_df in ["forex_end_period", "forex_period_average"]:
        df = df_dict[forex_df]

        df.columns = df.iloc[0]
        df = normalize_column_names(df)
        df = df.iloc[1:].reset_index(drop=True)
        df["year"] = df["year"].astype(int)
        df = month_int_to_name(df, "month")
        df_long = df.melt(
            id_vars=["year", "month"],
            var_name="metric",
            value_name="value",
        )
        df_long = tidy(df_long, month_col="month")
        df_long = df_long.sort_values(["year", "month"]).reset_index(drop=True)
        df_results[forex_df] = df_long

    return df_results
