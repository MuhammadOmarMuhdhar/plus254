import pandas as pd
from plus254.utils.transformers import tidy, frame

def transform(records):

    dfs = []
    for record in records:
        year = record["year"]
        quarter = record["quarter"]
        raw_df = record["raw_df"]

        transformed = (
                raw_df
                .pipe(tidy.normalise_nulls)
                .pipe(frame.drop_header_artifact_rows)
                .pipe(frame.clean_two_layer_header)
                .iloc[1:]                          
                .reset_index(drop=True)
                .dropna(axis=1, how='all')
                .iloc[:, 0:3]
                .pipe(lambda d: d.set_axis(['entity', 'on-net', 'off-net'], axis=1))
                .melt(id_vars=['entity'], var_name='item', value_name='value')
                .assign(year=year, quarter=quarter)
                .pipe(tidy.tidy)
                .assign(entity=lambda d: tidy.replace_words(d, 0, {
                    'safaricom': 'safaricom plc',
                    'airtel': 'airtel ltd',
                    'telkom': 'telkom ltd', 
                    'finserve': 'finserve',
                    'jamii': 'jamii telecom ltd',
                }))
                .reset_index(drop=True)
                [['year', 'quarter', 'entity', 'item', 'value']]
            )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)
