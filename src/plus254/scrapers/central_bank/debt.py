import pandas as pd
from plus254.utils.df_utils import (
    extract_columns,
    normalize_columns,
    convert_month_to_name,
    set_month_categorical,
    capitalize_columns,
    clean_numeric_values,
)


def process_public_debt(df_dict):
    df = df_dict["public_debt"]
    df = extract_columns(df, 2, 3)
    df = normalize_columns(df)

    id_vars = ["year", "month"]
    value_vars = ["domestic debt", "external debt", "total"]

    df.dropna(subset=id_vars, inplace=True)
    df["year"] = df["year"].astype(int)
    df["month"] = df["month"].astype(int)
    df = convert_month_to_name(df, "month")

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name="metric",
        value_name="value",
    )

    df_long = clean_numeric_values(df_long, "value")
    df_long = set_month_categorical(df_long, "month")
    df_long = capitalize_columns(df_long)
    return df_long


def process_domestic_debt(df_dict):
    df = df_dict["domestic_debt"]
    df = extract_columns(df, 1, 3)
    df = normalize_columns(df)
    df["fiscal year"] = df["fiscal year"].str.strip()
    df = df[df["fiscal year"].str.match(r"^[\w]+-[\w]+$", na=False)]

    df["parsed"] = pd.to_datetime("01-" + df["fiscal year"], format="mixed")
    df["year"] = df["parsed"].dt.year
    df["month"] = df["parsed"].dt.strftime("%B")
    df = df.drop(columns="parsed")
    df.columns = df.columns.str.strip().str.replace(r"\*+", "", regex=True).str.strip().str.lower()

    id_vars = ["year", "month"]
    value_vars = [
        "treasury bills",
        "treasury bonds",
        "government stocks",
        "overdraft at central bank",
        "advances from commercial banks",
        "other domestic debt",
        "total domestic debt",
    ]

    df.dropna(subset=id_vars, inplace=True)
    df["year"] = df["year"].astype(int)

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name="metric",
        value_name="value",
    )

    df_long = clean_numeric_values(df_long, "value")
    df_long = set_month_categorical(df_long, "month")
    df_long = capitalize_columns(df_long)
    return df_long
