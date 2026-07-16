from plus254.utils.transformers import tidy

def transform(df):
    return (
        df
        .iloc[1:, [1, 3, 5, 8, 10]]
        .set_axis(
            [
                "county",
                "constituency",
                "ward",
                "polling_station",
                "value",
            ],
            axis=1,
        )
        .query("county != 'Total' and constituency != 'Total'")
        .pipe(tidy._tidy)
        .dropna()
        .reset_index(drop=True)
    )