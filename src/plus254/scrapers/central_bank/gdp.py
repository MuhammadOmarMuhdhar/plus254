import numpy as np
import pandas as pd
from plus254.utils.df_utils import (
    clean_numeric_values,
    snake_case_columns,
    lowercase_values,
)


def process_gdp_quarterly(df_dict):
    df = df_dict["gdp_quarterly"]

    years = df.iloc[1, 2:].ffill().bfill().astype(int).values
    quarters = df.iloc[2, 2:].values
    date_cols = [f"{y}-{q}" for y, q in zip(years, quarters)]

    df.columns = ["0", "activity"] + date_cols
    df = df.iloc[3:].copy()
    df = df.replace("NaN", np.nan).dropna(subset=["activity"], how="all")

    value_cols = [c for c in df.columns if c not in ["0", "activity"]]
    df_long = df.melt(
        id_vars=["activity"],
        value_vars=value_cols,
        var_name="period",
        value_name="value",
    )

    df_long[["year", "quarter"]] = df_long["period"].str.split("-", expand=True)
    df_long["year"] = df_long["year"].astype(int)
    df_long["quarter"] = df_long["quarter"].str.strip()
    df_long.drop(columns=["period"], inplace=True)

    df_long = clean_numeric_values(df_long, "value")

    df_long = df_long.sort_values(["year", "quarter", "activity"]).reset_index(drop=True)
    df_long = lowercase_values(df_long)
    df_long = snake_case_columns(df_long)

    return df_long
