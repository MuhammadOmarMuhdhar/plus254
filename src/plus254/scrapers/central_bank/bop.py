from plus254.utils.df_utils import (
    normalize_columns,
    snake_case_columns,
    lowercase_values,
    clean_numeric_values,
)


def process_bop_annual(df_dict):
    df = df_dict["bop_annual"]

    df.columns = df.iloc[1]
    df = normalize_columns(df)
    df = df.iloc[2:].reset_index(drop=True)

    df_long = df.melt(
        id_vars=["bpm6 concept"],
        var_name="year",
        value_name="value",
    )

    df_long = clean_numeric_values(df_long, "value")
    df_long["year"] = df_long["year"].astype(int)
    df_long = df_long.sort_values(["year"]).reset_index(drop=True)
    df_long.rename(columns={"bpm6 concept": "category"}, inplace=True)

    df_long = lowercase_values(df_long)
    df_long = snake_case_columns(df_long)
    return df_long
