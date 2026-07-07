from typing import Dict
import numpy as np
import pandas as pd
from .text import _snake_case


def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Strip whitespace, lowercase, and collapse internal spaces in column names."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\s+", " ", regex=True)
    return df

def _snake_case_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert all column names to snake_case."""
    df = df.copy()
    df.columns = [_snake_case(c) for c in df.columns]
    return df

def month_int_to_name(df: pd.DataFrame, month_col: str = "month") -> pd.DataFrame:
    """Convert integer month column (1-12) to month name strings (January-December)."""
    df = df.copy()
    df[month_col] = df[month_col].astype(int).apply(
        lambda x: pd.to_datetime(str(x), format="%m").strftime("%B")
    )
    return df


def extract_year_month(
    df: pd.DataFrame, 
    date_col: str, 
    date_format: str = "%d-%m-%Y", 
    year_col: str = "year",
    month_col: str = "month"
):
    """Parse a date column (e.g. '15-12-2025') into year (int) + month (string) columns."""
    df = df.copy()
    parsed = pd.to_datetime(df[date_col], format=date_format)

    df[year_col] = parsed.dt.year.astype(int)
    df[month_col] = parsed.dt.strftime("%B")
    return df


def _normalise_nulls(df: pd.DataFrame) -> pd.DataFrame:
    """Coerce empty strings and 'None' strings to actual None, drop all-null rows."""
    return (
        df.replace('None', None)
          .replace('', None)
          .replace(' None', None)
          .dropna(how='all')
    )


def _replace_by_position(col: str, pos_map: Dict[int, str]) -> pd.Series:
    col = col.copy()
    col.iloc[list(pos_map.keys())] = list(pos_map.values())
    return col


def _forward_fill(df: pd.DataFrame, label_indices: list) -> pd.DataFrame:
    """Replace empty strings with None, then forward-fill label columns."""
    df = df.replace('', None)
    for col_idx in label_indices:
        col = df.columns[col_idx]
        df[col] = df[col].ffill()
    return df


def _filter_totals(df: pd.DataFrame) -> pd.DataFrame:
    """Remove aggregated 'total' rows from metric and operator dimensions."""
    return (
        df[df['metric'] != 'total']
          .pipe(lambda d: d[d['operator'] != 'total'])
          .reset_index(drop=True)
    )


def _replace_words(
    df: pd.DataFrame,
    col: int, mapping: Dict[str, str], 
    case: bool = False, 
    default=None
) -> pd.DataFrame:
    """Replace values in a column (selected by position) based on substring matches."""
    col_name = df.columns[col]

    conditions = [
        df[col_name].str.contains(word, case=case, na=False)
        for word in mapping
    ]
    choices = list(mapping.values())
    fallback = df[col_name] if default is None else default

    return np.select(conditions, choices, default=fallback)


def _order_month_categorical(df: pd.DataFrame, month_col: str = "month") -> pd.DataFrame:
    """Convert month column to an ordered pandas Categorical (Jan-Dec)."""
    df = df.copy()
    month_order = pd.date_range("2000-01", periods=12, freq="MS").strftime("%B").tolist()
    df[month_col] = pd.Categorical(df[month_col], categories=month_order, ordered=True)
    return df


def _coerce_numeric(df: pd.DataFrame, col: str = "value") -> pd.DataFrame:
    """Convert a column to numeric, stripping commas and dropping NaN rows."""
    df = df.copy()
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "", regex=False), errors="coerce")
    df = df.dropna(subset=[col])
    return df


def _lowercase_strings(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase all string-type columns."""
    df = df.copy()
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.lower()
    return df


def _tidy(
    df: pd.DataFrame, 
    *, 
    value_col: str = "value",
    month_col: str = None
) -> pd.DataFrame:
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