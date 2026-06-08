import numpy as np
import pandas as pd


def extract_columns(df, header_row, data_start_row):
    df = df.copy()
    df.columns = df.iloc[header_row].reset_index(drop=True)
    df = df.iloc[data_start_row:].reset_index(drop=True)
    return df


def normalize_columns(df):
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\s+", " ", regex=True)
    return df


def convert_month_to_name(df, month_col="month"):
    df = df.copy()
    df[month_col] = df[month_col].astype(int).apply(
        lambda x: pd.to_datetime(str(x), format="%m").strftime("%B")
    )
    return df


def set_month_categorical(df, month_col="month"):
    df = df.copy()
    month_order = pd.date_range("2000-01", periods=12, freq="MS").strftime("%B").tolist()
    df[month_col] = pd.Categorical(df[month_col], categories=month_order, ordered=True)
    return df


def clean_numeric_values(df, col="value"):
    df = df.copy()
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "", regex=False), errors="coerce")
    df = df.dropna(subset=[col])
    return df


def capitalize_columns(df):
    df = df.copy()
    df.columns = df.columns.str.capitalize()
    return df
