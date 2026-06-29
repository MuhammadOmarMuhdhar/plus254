import pandas as pd

def _strip_column(series: pd.Series) -> pd.Series:
    """Drop NaN, blank, and 'none' string values from a column."""
    col = series.dropna().astype(str).str.strip()
    col = col[col != '']
    col = col[col.str.lower() != 'none']
    return col

def _classify_column(col_vals: pd.Series, min_data_ratio: float, min_label_ratio: float, n_rows: int) -> str:
    """Classify a single cleaned column as 'data', 'label', or 'padding'."""
    fill_ratio = len(col_vals) / n_rows
    min_req = min(min_data_ratio, min_label_ratio)
    if fill_ratio < min_req:
        return 'padding'
    if col_vals.str.match(r'^[\d\s,.]+$').all():
        return 'data' if fill_ratio >= min_data_ratio else 'padding'
    return 'label' if fill_ratio >= min_label_ratio else 'padding'


def prune(df: pd.DataFrame, min_data_ratio: float = 0.15, min_label_ratio: float = 0.10):
    """Filter sparse/padding columns, returning label indices, data indices, and cleaned df."""
    n_rows = len(df)
    col_types = [
        _classify_column(_strip_column(df.iloc[:, i]), min_data_ratio, min_label_ratio, n_rows)
        for i in range(len(df.columns))
    ]

    keep_mask = [t != 'padding' for t in col_types]
    kept_original_indices = [i for i, k in enumerate(keep_mask) if k]

    cleaned_df = df.loc[:, keep_mask].copy()

    label_indices, data_indices, new_cols = [], [], []
    for new_i, orig_i in enumerate(kept_original_indices):
        ct = col_types[orig_i]
        if ct == 'data':
            data_indices.append(new_i)
            new_cols.append(df.columns[orig_i])
        else:
            label_indices.append(new_i)
            new_cols.append(f'label_{new_i}')

    cleaned_df.columns = new_cols
    return label_indices, data_indices, cleaned_df