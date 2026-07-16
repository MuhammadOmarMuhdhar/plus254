from plus254.utils.transformers import tidy
import pandas as pd

def transform(df):
    id_vars = ["year", "month"]

    cleaned_df = (
        df.copy()
        .pipe(lambda d: d.set_axis(d.iloc[1].ffill().values, axis=1))
        .pipe(lambda d: d.set_axis(
            ["year", "month", "coffee", 'coffee', 'coffee',
            'tea', 'tea', 'tea', 'horticulture', 'horticulture', 'horticulture'],
                axis=1
            )
        )
        .pipe(lambda d: d.set_axis(
                                pd.MultiIndex.from_arrays([d.columns, d.iloc[3]]),
                                axis=1
                            ))
        .pipe(tidy._normalise_nulls)
        .pipe(lambda d: d.drop(index=1))
        .pipe(lambda d: d.drop(index=4))
        .pipe(lambda d: d.drop(index=5))
        .pipe(lambda d: d[d.iloc[:, 0].notna()])
        .pipe(lambda d: d.set_axis(d.columns.set_names(['item', 'measure']), axis=1))
        .pipe(lambda d: d.set_index(d.columns[:2].tolist()))
        .rename_axis(index=['year', 'month'])
        .stack(level='item', future_stack=True)
        .melt(id_vars=['year', 'month', 'item'], var_name='measure', value_name='value')
        .assign(value=lambda d: d['value'].astype(str).str.replace(',', '', regex=False).astype(float))
        .pipe(tidy._month_int_to_name)
        .assign(year=lambda d: d["year"].astype(int))
        .pipe(tidy._tidy)
        .reset_index(drop=True)

    )

    volume_df = cleaned_df.query("measure == 'volume'").drop(columns='measure').reset_index(drop=True)
    value_df = cleaned_df.query("measure == 'value'").drop(columns='measure').reset_index(drop=True)
    avergae_price_df = cleaned_df.query("measure == 'average'").drop(columns='measure').reset_index(drop=True)

    return {
        'principal_exports': volume_df,
        'principal_exports_value': value_df,
        'principal_exports_average_price': avergae_price_df
    }
