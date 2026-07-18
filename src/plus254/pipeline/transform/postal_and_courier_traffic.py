import pandas as pd
from src.plus254.utils.transformers import tidy, frame, prune

def transform(records):

    dfs = []
    for record in records:
        year = record["year"]
        quarter = record["quarter"]
        raw_df = record["raw_df"]

        label_indices, _, cleaned = prune.prune_columns(raw_df)
        transformed = (
                cleaned
                .pipe(tidy.normalise_nulls)
                .pipe(frame.drop_header_artifact_rows)
                .pipe(frame.merge_shifted_columns)
                .pipe(
                        lambda df: df.drop(df.columns[2], axis=1) if df.shape[1] > 5 else df
                )
                .pipe(tidy.forward_fill, [0])
                .iloc[:, 0:3]
                .pipe(lambda d: d.assign(**{d.columns[1]: ['Domestic',
                                                            'International Outgoing',
                                                            'International Incoming',
                                                            'Domestic',
                                                            'International Outgoing',
                                                            'International Incoming']})
                    )
                .set_axis([
                            "item",
                            'metric',
                            "value"
                        ], axis=1)
                .assign(year=year,quarter=quarter)
                .pipe(tidy.tidy)
                [["year", "quarter", "metric", "item", "value"]]
                .reset_index(drop=True)
            )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)