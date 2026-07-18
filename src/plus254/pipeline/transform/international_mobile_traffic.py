import pandas as pd
from src.plus254.utils.transformers import tidy, frame, prune

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
                .pipe(tidy.forward_fill, label_indices=[0])
                .iloc[0:8, 0:3]
                .pipe(lambda d: d.assign(**{
                    d.columns[0]: d.iloc[:, 0].str.replace('\n', ' ').str.replace('International', '')
                }))
                .set_axis(['item', 'region', 'value'], axis=1)
                .assign(year=year, quarter=quarter)
                .dropna()
                .pipe(tidy.tidy)
                .assign(item=lambda d: tidy.replace_words(d, 0, {
                        'incoming': 'incoming',
                        'outgoing': 'outgoing',
                    }
                ))
                .reset_index(drop=True)
                [['year', 'quarter', 'region', 'item', 'value']]
                
            )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)