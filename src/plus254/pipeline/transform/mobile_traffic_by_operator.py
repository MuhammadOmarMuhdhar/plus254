import pandas as pd
from src.plus254.utils.transformers import tidy, frame, prune

def transform(records):

    dfs = []
    for record in records:
        year = record["year"]
        quarter = record["quarter"]
        raw_df = record["raw_df"]

        label_indices, _, cleaned_df = prune.prune_columns(raw_df)
        
        transformed = (
            cleaned_df
            .pipe(tidy.normalise_nulls)
            .pipe(frame.drop_header_artifact_rows)
            .pipe(tidy.normalise_nulls)
            .pipe(tidy.forward_fill, label_indices)
            .iloc[:6]                          # one period group = 6 rows
            .pipe(lambda d: d.dropna(axis=1, how='all').iloc[:, 1:].set_axis(
                ['metric', 'item', 'safaricom', 'airtel', 'telkom', 'finserve', 'jamii', 'total'], axis=1))
            .pipe(lambda d: d.melt(id_vars=['item', 'metric'], var_name='entity', value_name='value')
                .assign(year=year, quarter=quarter)
                .assign(item=lambda d: d['item'].str.replace(r'.*\n', '', regex=True)))
            .pipe(tidy.tidy)
            [['year', 'quarter', 'entity', 'metric', 'item', 'value']]
            .assign(metric=lambda d: tidy.replace_words(d, 3, {
                'voice': 'voice',
                'sms': 'sms'
            }))
            .assign(item=lambda d: tidy.replace_words(d, 4, {
                'on net': 'on-net',
                'off net': 'off-net'
            }))
            .reset_index(drop=True)
        )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)
