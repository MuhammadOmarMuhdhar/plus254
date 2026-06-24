import re
import unicodedata

import pandas as pd


# ---------------------------------------------------------------------------
# Private: text utilities
# ---------------------------------------------------------------------------

def _snake_case(text: str) -> str:
    """Convert text to snake_case."""
    return re.sub(r"[^A-Za-z0-9]+", "_", str(text)).strip("_").lower()


def _split_camel_case(text: str) -> str:
    """Insert spaces at camelCase boundaries."""
    s = str(text)
    if not s:
        return s
    return re.sub(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", " ", s)


def _squash(text: str) -> str:
    """Strip all non-alphanumeric characters and uppercase."""
    return re.sub(r"[^A-Za-z0-9]", "", str(text)).upper()


# ---------------------------------------------------------------------------
# Public: preprocessing utilities  (called before melt / as standalone steps)
# ---------------------------------------------------------------------------

def promote_header_row(df, header_row, data_start_row):
    """Promote a specific row to column names and slice data starting from another row."""
    df = df.copy()
    df.columns = df.iloc[header_row].reset_index(drop=True)
    df = df.iloc[data_start_row:].reset_index(drop=True)
    return df


def normalize_column_names(df):
    """Strip whitespace, lowercase, and collapse internal spaces in column names."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\s+", " ", regex=True)
    return df


def month_int_to_name(df, month_col="month"):
    """Convert integer month column (1-12) to month name strings (January-December)."""
    df = df.copy()
    df[month_col] = df[month_col].astype(int).apply(
        lambda x: pd.to_datetime(str(x), format="%m").strftime("%B")
    )
    return df


# ---------------------------------------------------------------------------
# Private: frame utilities
# ---------------------------------------------------------------------------

def _order_month_categorical(df, month_col="month"):
    """Convert month column to an ordered pandas Categorical (Jan-Dec)."""
    df = df.copy()
    month_order = pd.date_range("2000-01", periods=12, freq="MS").strftime("%B").tolist()
    df[month_col] = pd.Categorical(df[month_col], categories=month_order, ordered=True)
    return df


def _coerce_numeric(df, col="value"):
    """Convert a column to numeric, stripping commas and dropping NaN rows."""
    df = df.copy()
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "", regex=False), errors="coerce")
    df = df.dropna(subset=[col])
    return df


def _snake_case_column_names(df):
    """Convert all column names to snake_case."""
    df = df.copy()
    df.columns = [_snake_case(c) for c in df.columns]
    return df


# ---------------------------------------------------------------------------
# Private: cleaning utilities
# ---------------------------------------------------------------------------

def _lowercase_strings(df):
    """Lowercase all string-type columns."""
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.lower()
    return df


# ---------------------------------------------------------------------------
# Public: entry point
# ---------------------------------------------------------------------------

def tidy(df, *, value_col="value", month_col=None):
    """Tidy a DataFrame: normalize columns, coerce numerics, handle months, lowercase, snake_case.

    Parameters
    ----------
    df : pd.DataFrame
    value_col : str, default "value"
        Column name to coerce to numeric (post-normalize).
    month_col : str, optional
        Column name for month ordering (post-normalize, e.g. "month").
    """
    if month_col:
        df = _order_month_categorical(df, month_col=month_col)
    df = normalize_column_names(df)
    df = _coerce_numeric(df, col=value_col)
    df = _lowercase_strings(df)
    df = _snake_case_column_names(df)
    return df
