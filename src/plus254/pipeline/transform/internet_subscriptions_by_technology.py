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
                .pipe(lambda d: d.loc[:, d.isna().mean() < 0.5])
                .pipe(frame.drop_header_artifact_rows)
                .iloc[:, 0:2]
                .set_axis(["item", "value"], axis=1)
                .pipe(tidy.tidy)
                .assign(year=year, quarter=quarter)
                [["year", "quarter", "item", "value"]]
                .assign(item=lambda d: tidy.replace_words(d, 2, {
                    "terrestrial": "terrestrial wireless",
                    "satellite": "satellite",
                    "dsl": "dsl (copper)",
                    "fibre": "fibre",
                    "cable": "cable",
                    "other": "other",
                }))
            .loc[lambda d: ~d["item"].str.contains("total", case=False, na=False)]
            .reset_index(drop=True)
            )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)