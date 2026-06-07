import numpy as np
import pandas as pd
from plus254.utils.df_utils import (
    clean_numeric_values,
    set_month_categorical,
    capitalize_columns,
)


def process_monetary_survey(df_dict):
    df = df_dict["monetary_survey"]

    years_raw = df.columns[2:].values
    months_raw = df.iloc[1, 2:].values

    date_cols = []
    current_year = None
    for y, m in zip(years_raw, months_raw):
        try:
            current_year = int(float(y))
        except (ValueError, TypeError):
            pass
        date_cols.append(f"{current_year}-{m}")

    df.columns = ["section_code", "indicator"] + date_cols
    df = df.iloc[2:].copy()

    df = df.replace("NaN", np.nan).dropna(subset=["indicator"], how="all")
    df["section_code"] = df["section_code"].ffill()

    section_map = {
        "A.": "Central Bank of Kenya",
        "B": "Other Depository Corporation Survey",
        "C": "Depository Corporation Survey",
    }
    df["section"] = df["section_code"].map(section_map)

    value_cols = [c for c in df.columns if c not in ["section_code", "indicator", "section"]]
    df_long = df.melt(
        id_vars=["section", "indicator"],
        value_vars=value_cols,
        var_name="period",
        value_name="value",
    )

    df_long[["year", "month"]] = df_long["period"].str.split("-", expand=True)
    df_long["year"] = df_long["year"].astype(int)
    df_long["month"] = df_long["month"].str.strip()
    df_long["month"] = df_long["month"].str.replace("Sept", "Sep")
    df_long["month"] = pd.to_datetime(df_long["month"], format="%b").dt.strftime("%B")

    df_long = clean_numeric_values(df_long, "value")
    df_long = df_long[["section", "indicator", "year", "month", "value"]].sort_values(
        ["section", "indicator", "year", "month"]
    ).reset_index(drop=True)

    df_long = set_month_categorical(df_long, "month")
    df_long = df_long.sort_values(["year", "month"]).reset_index(drop=True)
    df_long = capitalize_columns(df_long)
    return df_long
