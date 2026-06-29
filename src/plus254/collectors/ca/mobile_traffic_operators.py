import pandas as pd
from src.plus254.utils import tidy, prune


def _rename_operator_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Drop residual empty columns, the period label column, then apply operator names."""
    df = df.dropna(axis=1, how='all').iloc[:, 1:]
    df.columns = ['item', 'metric', 'safaricom', 'airtel',
                  'telkom', 'finserve', 'jamii', 'total']
    return df


def _melt_to_long(df: pd.DataFrame, year: int, quarter: int) -> pd.DataFrame:
    """Pivot wide operator columns to long format and attach period metadata."""
    long = df.melt(id_vars=['item', 'metric'], var_name='operator', value_name='value')
    long['item'] = long['item'].str.replace(r'.*\n', '', regex=True)
    long['year'] = year
    long['quarter'] = quarter
    return long


def _filter_totals(df: pd.DataFrame) -> pd.DataFrame:
    """Remove aggregated 'total' rows from metric and operator dimensions."""
    return (
        df[df['metric'] != 'total']
          .pipe(lambda d: d[d['operator'] != 'total'])
          .reset_index(drop=True)
    )


def parse_mobile_traffic_operators(df: pd.DataFrame, year: int, quarter: int) -> pd.DataFrame:
    """
    Parse a raw mobile traffic operators table into tidy long format.
    Returns one row per (year, quarter, item, metric, operator).
    """

    label_indices, _, cleaned_df = prune.prune(df)

    result = (
        cleaned_df
        .pipe(tidy._drop_header_artifact_rows)
        .pipe(tidy._normalise_nulls)
        .pipe(tidy._forward_fill, label_indices)
        .iloc[:6]                          # one period group = 6 rows
        .pipe(_rename_operator_columns)
        .pipe(_melt_to_long, year, quarter)
        .pipe(tidy.tidy)
        [['year', 'quarter', 'item', 'metric', 'operator', 'value']]
        .pipe(_filter_totals)
    )

    return result