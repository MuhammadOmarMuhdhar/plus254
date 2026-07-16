import pandas as pd
from src.plus254.utils.transformers import tidy, frame, prune

def transform(records):

    dfs = []
    for record in records:
        year = record["year"]
        quarter = record["quarter"]
        raw_df = record["raw_df"]

        label_indices, _, cleaned = prune._prune(raw_df)
        transformed = (
            cleaned
            .pipe(tidy._normalise_nulls)
            .pipe(frame._drop_header_artifact_rows)
            .pipe(frame._merge_shifted_columns, column_pairs=[(7,8),(9,10)])
            .pipe(lambda d: d.loc[:, d.isna().mean() < 0.5]) 
            .pipe(frame._drop_header_artifact_rows)
            .pipe(
                lambda d: d.iloc[0:8] if len(d.columns) == 8 else d.iloc[0:8, 0:8])
            .pipe(lambda d: d.replace("-", 0))
            .set_axis([
                        "item",
                        "< 256 Kbps",
                        "256 Kbps – 2 Mbps",
                        "2 – 10 Mbps",
                        "10 – 30 Mbps",
                        "30 – 100 Mbps",
                        "100 Mbps – 1 Gbps",
                        "≥ 1 Gbps"
                    ], axis=1)
            .melt(id_vars="item", var_name="metric", value_name="value")
            .assign(year=year,quarter=quarter)
            .pipe(tidy._tidy)
            .assign(item=lambda d: tidy._replace_words(d, 0, {
                    'cable': 'cable',
                    'dsl': 'dsl (copper)',
                    'ftth': 'ftth',
                    'ftto': 'ftto',
                    'fixed\nwireless': 'fixed wireless',
                    'fixedwireless': 'fixed wireless',
                    'otherfixed': 'other fixed',
                    'satellite': 'satellite',
                }
            ))
            [["year", "quarter", "metric", "item", "value"]]
            .reset_index(drop=True)
        )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy._sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)