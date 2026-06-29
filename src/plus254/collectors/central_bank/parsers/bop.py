import pandas as pd
from plus254.utils.tidy import tidy, normalize_column_names


def process_bop_annual(df_dict):
    df = df_dict["bop_annual"]

    df.columns = df.iloc[1]
    df = normalize_column_names(df)
    df = df.iloc[2:].reset_index(drop=True)

    df_long = df.melt(
        id_vars=["bpm6 concept"],
        var_name="year",
        value_name="value",
    )

    df_long = tidy(df_long)
    df_long["year"] = df_long["year"].astype(int)
    df_long = df_long.sort_values(["year"]).reset_index(drop=True)
    df_long.rename(columns={"bpm6_concept": "metric"}, inplace=True)
    df_long = df_long[["year", "metric", "value"]]
    return df_long
