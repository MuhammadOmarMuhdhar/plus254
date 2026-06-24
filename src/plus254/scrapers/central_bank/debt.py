import pandas as pd
from plus254.utils.tidy import tidy, promote_header_row, normalize_column_names, month_int_to_name


def process_public_debt(df_dict):
    df = df_dict["public_debt"]
    df = promote_header_row(df, 2, 3)
    df = normalize_column_names(df)
    df.dropna(subset=["year", "month"], inplace=True)
    df["year"] = df["year"].astype(int)
    df["month"] = df["month"].astype(int)
    df = month_int_to_name(df, "month")
    df_long = df.melt(
        id_vars=["year", "month"],
        value_vars=["domestic debt", "external debt", "total"],
        var_name="metric",
        value_name="value",
    )
    df_long = tidy(df_long, month_col="month")
    return df_long


def process_domestic_debt(df_dict):
    df = df_dict["domestic_debt"]
    df = promote_header_row(df, 1, 3)
    df = normalize_column_names(df)
    df["fiscal year"] = df["fiscal year"].str.strip()
    df = df[df["fiscal year"].str.match(r"^[\w]+-[\w]+$", na=False)]

    df["parsed"] = pd.to_datetime("01-" + df["fiscal year"], format="mixed")
    df["year"] = df["parsed"].dt.year
    df["month"] = df["parsed"].dt.strftime("%B")
    df = df.drop(columns="parsed")
    df.columns = df.columns.str.strip().str.replace(r"\*+", "", regex=True).str.strip().str.lower()

    df.dropna(subset=["year", "month"], inplace=True)
    df["year"] = df["year"].astype(int)

    df_long = df.melt(
        id_vars=["year", "month"],
        value_vars=[
            "treasury bills", "treasury bonds", "government stocks",
            "overdraft at central bank", "advances from commercial banks",
            "other domestic debt", "total domestic debt",
        ],
        var_name="metric",
        value_name="value",
    )
    df_long = tidy(df_long, month_col="month")
    return df_long
