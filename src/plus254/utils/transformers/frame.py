import pandas as pd



def _promote_header_row(df, header_row, data_start_row):
    """Promote a specific row to column names and slice data starting from another row."""
    df = df.copy()
    df.columns = df.iloc[header_row].reset_index(drop=True)
    df = df.iloc[data_start_row:].reset_index(drop=True)
    return df



def _clean_two_layer_header(df: pd.DataFrame, header_row: int = 0) -> pd.DataFrame:
    """Clean where actual headers are in value rows
    """
    df = df.copy()
    df = df.drop(df.index[header_row]).reset_index(drop=True)
    return df


def _drop_header_artifact_rows(df: pd.DataFrame, n_cols: int = 3) -> pd.DataFrame:
    """Remove leading rows where the first n columns are all empty/None."""
    while len(df) > 0:
        first_vals = [df.iloc[0, i] for i in range(min(n_cols, len(df.columns)))]
        if all(x is None or (isinstance(x, str) and x.strip().lower() in ('', 'none'))
               for x in first_vals):
            df = df.iloc[1:]
        else:
            break
    return df


def _merge_shifted_columns(df, column_pairs=None, column_groups=None):
    """Merge columns where values are shifted across adjacent columns.

    Parameters
    ----------
    column_pairs : list of (int|str, int|str), optional
        Pairs of (left, right) column positions/names to merge where the left
        column is null exactly where the right has values (perfect complement).
    column_groups : list of tuple, optional
        Groups of column positions/names to merge into the leftmost column.
        For each row, the first non-null value across the group wins. Handles
        3+ column shifts where values spread across columns without overlap.
    """
    df = df.copy()
    idx_to_drop = set()
    col_list = list(df.columns)

    def _idx(c):
        return c if isinstance(c, int) else col_list.index(c)

    if column_groups is not None:
        for group in column_groups:
            gi = [_idx(c) for c in group]
            target = gi[0]
            for src in gi[1:]:
                if src >= df.shape[1] or src in idx_to_drop:
                    continue
                src_vals = df.iloc[:, src]
                target_vals = df.iloc[:, target]
                null_in_target = target_vals.isna()
                if null_in_target.any():
                    df.iloc[null_in_target.values, target] = src_vals[null_in_target].values
                idx_to_drop.add(src)

    ncols = df.shape[1]
    if column_pairs is None:
        pairs = [(i, i + 1) for i in range(ncols - 1)]
    else:
        pairs = []
        for left, right in column_pairs:
            li = _idx(left)
            ri = _idx(right)
            pairs.append((li, ri))

    for li, ri in pairs:
        if li in idx_to_drop or ri in idx_to_drop or li >= df.shape[1] or ri >= df.shape[1]:
            continue

        left_col = df.iloc[:, li]
        right_col = df.iloc[:, ri]

        left_null = left_col.isna()
        right_notnull = right_col.notna()

        if (left_null == right_notnull).all():
            df.iloc[left_null.values, li] = df.iloc[left_null.values, ri].values
            idx_to_drop.add(ri)

    keep = [i for i in range(df.shape[1]) if i not in idx_to_drop]
    return df.iloc[:, keep]