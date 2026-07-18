import pandas as pd
from plus254.utils.transformers import prune
from src.plus254.utils.transformers import tidy

def transform(records):

    isp_lablels = {
        'safaricom': 'safaricom',
        'jamii': 'jamii telecommunications',
        'wananchi': 'wananchi group',
        'poa': 'poa internet',
        'ahadi': 'ahadi wireless',
        'vilcom': 'vilcom network',
        'mawingu': 'mawingu networks',
        'starlink': 'starlink',
        'dimension': 'dimension data',
        'liquid': 'liquid',
        'others': 'others',
        'other': 'others',
        'vijiji': 'vijiji connect',
    }
    dfs = []
    for record in records:
        year = record["year"]
        quarter = record["quarter"]
        raw_df = record["raw_df"]

        _, _, cleaned = prune.prune_columns(raw_df)

        transformed = (
            cleaned
            .pipe(tidy.normalise_nulls)
            .iloc[:, 0:2]
            .set_axis(["entity", "value"], axis=1)
            .assign(year=year, quarter=quarter)
            .pipe(tidy.tidy)
            .assign(entity=lambda d: tidy.replace_words(d, 0, isp_lablels))
            [["year", "quarter", "entity", "value"]]
            .reset_index(drop=True)
        )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined  = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)