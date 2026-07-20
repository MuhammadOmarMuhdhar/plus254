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
            .pipe(tidy.forward_fill, [0])
            .pipe(frame.merge_shifted_columns, column_groups=[(2,3,4)])
            .iloc[:, 0:3]
            .pipe(
                lambda d: d.replace({
                    '-': 0
                })
            )
            .pipe(lambda d: d.dropna())
            .set_axis([
                        "item",
                        'operator',
                        "value"
                    ], axis=1)
            .assign(year=year,quarter=quarter)
            .pipe(tidy.tidy)
            [["year", "quarter", "operator", "item", "value"]]
            .assign(operator=lambda d: tidy.replace_words(d, 2, {
                        'wananchi': 'wananchi (zuku)',
                        'wadani': 'wadani cable',
                        'star': 'star times',
                        'multichoice': 'multichoice (dstv)',
                        'ctn': 'ctn (msa)',
                        'cableone': 'cable one',
                        'gotv': 'go tv',

                    }))
            .reset_index(drop=True)
        )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)