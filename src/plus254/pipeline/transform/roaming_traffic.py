import pandas as pd
from plus254.utils.transformers import tidy

def transform(records):
    def process(df, year, quarter):
        return (
            df
            .pipe(tidy.normalise_nulls)
            .pipe(lambda d: d.loc[:, d.isna().mean() < 0.5])
            .replace('-', 0)
            .set_axis(
                ['country', 'incoming voice', 'incoming sms',
                 'outgoing voice', 'outgoing sms', 'data volumes'],
                axis=1,
            )
            .melt(id_vars=['country'], var_name='item', value_name='value')
            .assign(year=year, quarter=quarter)
            .pipe(tidy.tidy, value_col='value')
            .assign(metric=lambda d: [item[1] for item in d['item'].str.split()], 
                    item=lambda d: [item[0] for item in d['item'].str.split()]
                    )
            .assign(country=lambda d: d['country'].replace({
                's. sudan': 'south sudan',
                's.sudan': 'south sudan',
                'democraticrepublicofcongo': 'democratic republic of congo',
            }))
            [['year', 'quarter', 'country', 'metric', 'item', 'value']]
            .reset_index(drop=True)
        )

    groups = {}
    for r in records:
        key = (r["year"], r["quarter"])
        groups.setdefault(key, {})[r["table_index"]] = r["raw_df"]

    outbound_frames = []
    inbound_frames = []

    for (year, quarter), tables in groups.items():
        outbound_frames.append(process(tables[0], year, quarter))
        inbound_frames.append(process(tables[1], year, quarter))

    outbound_combined = tidy.sort_by_date(
        pd.concat(outbound_frames, ignore_index=True)
    ).reset_index(drop=True)

    inbound_combined = tidy.sort_by_date(
        pd.concat(inbound_frames, ignore_index=True)
    ).reset_index(drop=True)

    return {
        'roaming_traffic': outbound_combined,
        'inbound_roaming_traffic': inbound_combined,
    }