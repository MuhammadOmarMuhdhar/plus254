import pandas as pd
from plus254.utils.df_utils import (
    normalize_columns,
    snake_case_columns,
    lowercase_values,
    clean_numeric_values,
)

def process_registered_voters(df):

    df.columns = df.iloc[0]
    df = df.iloc[1:]

    df = normalize_columns(df)
    df = clean_numeric_values(df, "registered voters")
    df = lowercase_values(df)
    df = snake_case_columns(df)
    df = df.rename(columns={"registered_voters": "value"})

    return df