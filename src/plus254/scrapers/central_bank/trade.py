from plus254.utils.df_utils import (
    extract_columns,
    normalize_columns,
    convert_month_to_name,
    set_month_categorical,
    capitalize_columns,
    clean_numeric_values,
)


def process_exports_global(df_dict):
    df = df_dict["exports_global"]
    df = extract_columns(df, 1, 2)
    df = normalize_columns(df)

    id_vars = ["year", "month"]
    value_vars = [
        "u.k", "germany", "u.s.a", "netherlands", "uganda",
        "tanzania", "pakistan", "france", "egypt", "belgium", "others", "total",
    ]

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


def process_exports_africa(df_dict):
    df = df_dict["exports_africa"]
    df = extract_columns(df, 1, 2)
    df = normalize_columns(df)

    id_vars = ["year", "month"]
    value_vars = [
        "uganda", "tanzania", "zambia", "egypt", "rwanda",
        "zimbabwe", "ethiopia", "somalia", "south africa", "drc", "other", "total",
    ]

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


def process_domestic_exports(df_dict):
    df = df_dict["domestic_exports"]
    df = extract_columns(df, 2, 4)
    df = normalize_columns(df)

    id_vars = ["year", "month"]
    value_vars = [
        "coffee", "tea", "petroleum", "chemicals", "fish",
        "horticulture", "cement", "other", "total",
    ]

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


def process_imports_global(df_dict):
    df = df_dict["imports_global"]
    df = extract_columns(df, 1, 2)
    df = normalize_columns(df)

    id_vars = ["year", "month"]
    value_vars = [
        "u.k", "u.s.a", "germany", "italy", "u.a.e",
        "s.arabia", "france", "india", "s.africa", "japan",
        "china", "others", "total",
    ]

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


def process_imports_africa(df_dict):
    df = df_dict["imports_africa"]
    df = extract_columns(df, 3, 4)
    df = normalize_columns(df)

    id_vars = ["year", "month"]
    value_vars = [
        "uganda", "tanzania", "zambia", "egypt",
        "south africa", "zimbabwe", "other", "total",
    ]

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


def process_imports_commodity(df_dict):
    df = df_dict["imports_commodity"]
    df = extract_columns(df, 1, 3)
    df = normalize_columns(df)

    id_vars = ["year", "month"]
    value_vars = [
        "food and live animals",
        "beverages and tobacco",
        "crude materials inedible except fuels",
        "mineral fuels lubricants and related materials",
        "animals and vegetable oils and fats",
        "chemicals",
        "manufactured goods classified chiefly by materials",
        "machinery and transport equipment",
        "other",
        "total",
    ]

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


def process_principal_exports(df_dict):
    df = df_dict["principal_exports"]
    df = df.iloc[6:].reset_index(drop=True)

    df.columns = [
        "year", "month",
        "coffee volume", "coffee value", "coffee average",
        "tea volume", "tea value", "tea average",
        "horticulture volume", "horticulture value", "horticulture average",
    ]

    id_vars = ["year", "month"]
    value_vars = [
        "coffee volume", "coffee value", "coffee average",
        "tea volume", "tea value", "tea average",
        "horticulture volume", "horticulture value", "horticulture average",
    ]

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
