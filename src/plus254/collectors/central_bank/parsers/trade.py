import pandas as pd
from plus254.utils.tidy import tidy, promote_header_row, normalize_column_names, month_int_to_name


def _process_trade_table(df, header_row, data_start_row, id_vars, value_vars):
    df = promote_header_row(df, header_row, data_start_row)
    df = normalize_column_names(df)
    df.dropna(subset=id_vars, inplace=True)
    df["year"] = df["year"].astype(int)
    df["month"] = df["month"].astype(int)
    df = month_int_to_name(df, "month")
    df_long = df.melt(id_vars=id_vars, value_vars=value_vars, var_name="metric", value_name="value")
    df_long = tidy(df_long, month_col="month")
    return df_long


def _process_trade_table_no_header(df, id_vars, value_vars):
    df.dropna(subset=id_vars, inplace=True)
    df["year"] = df["year"].astype(int)
    df["month"] = df["month"].astype(int)
    df = month_int_to_name(df, "month")
    df_long = df.melt(id_vars=id_vars, value_vars=value_vars, var_name="metric", value_name="value")
    df_long = tidy(df_long, month_col="month")
    return df_long


def process_exports_global(df_dict):
    return _process_trade_table(
        df_dict["exports_global"], 1, 2,
        ["year", "month"],
        ["u.k", "germany", "u.s.a", "netherlands", "uganda",
         "tanzania", "pakistan", "france", "egypt", "belgium", "others", "total"],
    )


def process_exports_africa(df_dict):
    return _process_trade_table(
        df_dict["exports_africa"], 1, 2,
        ["year", "month"],
        ["uganda", "tanzania", "zambia", "egypt", "rwanda",
         "zimbabwe", "ethiopia", "somalia", "south africa", "drc", "other", "total"],
    )


def process_domestic_exports(df_dict):
    return _process_trade_table(
        df_dict["domestic_exports"], 2, 4,
        ["year", "month"],
        ["coffee", "tea", "petroleum", "chemicals", "fish",
         "horticulture", "cement", "other", "total"],
    )


def process_imports_global(df_dict):
    return _process_trade_table(
        df_dict["imports_global"], 1, 2,
        ["year", "month"],
        ["u.k", "u.s.a", "germany", "italy", "u.a.e",
         "s.arabia", "france", "india", "s.africa", "japan",
         "china", "others", "total"],
    )


def process_imports_africa(df_dict):
    return _process_trade_table(
        df_dict["imports_africa"], 3, 4,
        ["year", "month"],
        ["uganda", "tanzania", "zambia", "egypt",
         "south africa", "zimbabwe", "other", "total"],
    )


def process_imports_commodity(df_dict):
    return _process_trade_table(
        df_dict["imports_commodity"], 1, 3,
        ["year", "month"],
        ["food and live animals", "beverages and tobacco",
         "crude materials inedible except fuels",
         "mineral fuels lubricants and related materials",
         "animals and vegetable oils and fats", "chemicals",
         "manufactured goods classified chiefly by materials",
         "machinery and transport equipment", "other", "total"],
    )


def process_principal_exports(df_dict):
    df = df_dict["principal_exports"]
    df = df.iloc[6:].reset_index(drop=True)
    df.columns = [
        "year", "month",
        "coffee volume", "coffee value", "coffee average",
        "tea volume", "tea value", "tea average",
        "horticulture volume", "horticulture value", "horticulture average",
    ]
    return _process_trade_table_no_header(
        df,
        ["year", "month"],
        ["coffee volume", "coffee value", "coffee average",
         "tea volume", "tea value", "tea average",
         "horticulture volume", "horticulture value", "horticulture average"],
    )
