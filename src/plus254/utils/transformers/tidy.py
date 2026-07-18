from typing import Dict
import numpy as np
import pandas as pd
from .text import snake_case
import calendar
import pandas as pd

def sort_by_date(df):
    month_order = {m: i for i, m in enumerate(calendar.month_name[1:], start=1)}

    priority = ["year", "quarter", "month"]
    sort_cols = [c for c in priority if c in df.columns]

    if not sort_cols:
        return df

    return df.sort_values(
        by=sort_cols,
        key=lambda s: s.map(month_order) if s.name == "month" else s
    )

def normalize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Strip whitespace, lowercase, and collapse internal spaces in column names."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(r"\s+", " ", regex=True)
    return df

def _snake_case_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Convert all column names to snake_case."""
    df = df.copy()
    df.columns = [snake_case(c) for c in df.columns]
    return df

def month_int_to_name(df: pd.DataFrame, month_col: str = "month") -> pd.DataFrame:
    """Convert integer month column (1-12) to month name strings (January-December)."""
    df = df.copy()
    df[month_col] = df[month_col].astype(int).apply(
        lambda x: pd.to_datetime(str(x), format="%m").strftime("%B")
    )
    return df


def _extract_year_month(
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


def normalise_nulls(df: pd.DataFrame) -> pd.DataFrame:
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


def forward_fill(df: pd.DataFrame, label_indices: list) -> pd.DataFrame:
    """Replace empty strings with None, then forward-fill label columns."""
    df = df.replace('', None)
    for col_idx in label_indices:
        col = df.columns[col_idx]
        df[col] = df[col].ffill()
    return df


def _filter_totals(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows where any cell contains 'total' (case-insensitive)."""
    return df[~df.astype(str).apply(
        lambda col: col.str.lower().str.strip().str.contains('total')
    ).any(axis=1)]

def _build_date_columns(
    df: pd.DataFrame,
    *,
    start_col: int = 2,
    month_header_row: int = 1,
    year_col_start: int = 2,
    separator: str = "-",
    year_row: int | None = None,
) -> list[str]:
    """Build year-month column labels from the two-row header.

    Parameters
    ----------
    df : pd.DataFrame
        Source dataframe with a two-row header (years in column labels,
        months in `month_header_row`).
    start_col : int, default 2
        Index of the first data column (columns before this are skipped,
        e.g. ID/name columns).
    month_header_row : int, default 1
        Row index (via .iloc) containing the month labels.
    year_col_start : int, default 2
        Index into df.columns where year values begin. Usually matches
        `start_col`, but kept separate in case the year header and data
        columns are offset differently.
    separator : str, default "-"
        String used to join year and month, e.g. "2023-Jan".
    year_row : int | None, default None
        If years are stored in a row (like months) rather than in the
        column labels, pass the row index here. If None, years are read
        from df.columns as before.

    Returns
    -------
    list[str]
        Labels like "2023-Jan" for each data column.
    """
    years_raw = (
        df.iloc[year_row, year_col_start:].values
        if year_row is not None
        else df.columns[year_col_start:].values
    )
    months_raw = df.iloc[month_header_row, start_col:].values

    date_cols = []
    current_year = None
    for y, m in zip(years_raw, months_raw):
        try:
            current_year = int(float(y))
        except (ValueError, TypeError):
            pass
        date_cols.append(f"{current_year}{separator}{m}")
    return date_cols


def _parse_month_name(
    month: str,
    *,
    abbrev_fixes: dict[str, str] | None = None,
    input_format: str = "%b",
    output_format: str = "%B",
) -> str:
    """Normalize abbreviated month names to full names."""
    if abbrev_fixes is None:
        abbrev_fixes = {"Sept": "Sep"}

    month = month.strip()
    for wrong, right in abbrev_fixes.items():
        month = month.replace(wrong, right)

    return pd.to_datetime(month, format=input_format).strftime(output_format)


def replace_words(
    df: pd.DataFrame,
    col: int, 
    mapping: Dict[str, str], 
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


# def _order_month_categorical(df: pd.DataFrame, month_col: str = "month") -> pd.DataFrame:
#     """Convert month column to an ordered pandas Categorical (Jan-Dec)."""
#     df = df.copy()
#     month_order = pd.date_range("2000-01", periods=12, freq="MS").strftime("%B").tolist()
#     df[month_col] = pd.Categorical(df[month_col], categories=month_order, ordered=True)
#     return df


def _coerce_numeric(df: pd.DataFrame, col: str = "value") -> pd.DataFrame:
    """Convert a column to numeric, stripping commas and dropping NaN rows."""
    df = df.copy()
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(",", "", regex=False), errors="coerce").astype(float)
    df = df.dropna(subset=[col])
    return df

def _lowercase_strings(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase all string-type columns, including ordered categoricals."""
    df = df.copy()
    for col in df.select_dtypes(include=["object", "category"]).columns:
        df[col] = df[col].str.lower()
    return df

def tidy(
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
    return (
        df.copy()
        .pipe(sort_by_date)
        .pipe(normalize_column_names)
        .pipe(_coerce_numeric, col=value_col)
        .pipe(_lowercase_strings)
        .pipe(_snake_case_column_names)
        .pipe(_filter_totals)
        .reset_index(drop=True)
    )