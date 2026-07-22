import pandas as pd
from plus254.utils.transformers import tidy, frame


sector_mapping = {
    'communication information &': 'communication information & technology',
    'human work health activities & social work': 'human health & social work',
    'water collection supply; waste': 'water supply & waste collection',
    'agriculture, fishing forestry &': 'agriculture, forestry & fishing',
    'public administration defence &': 'public administration & defence',
    'repair wholesale of motor & retail vehicles trade;': 'wholesale & retail trade; repair of motor vehicles',
    'professional services & technical': 'professional & technical services',
    'accommodation service activities & food': 'accommodation & food service activities',
}


def transform(records):
    frames = []
    for record in records:
        df = record["raw_df"]

        processed = (
            df
            .pipe(frame.promote_header_row, 0, 1)
            .pipe(tidy.normalise_nulls)
            .rename(columns=lambda c: c.replace('\n', ' ') if isinstance(c, str) else c)
            .assign(year=lambda d: d['County'].eq('MOMBASA').cumsum().map(lambda g: 2025 - g))
            .melt(id_vars=['year', 'County'], var_name='sector', value_name='value')
            .assign(County=lambda d: d['County'].str.replace('\n', '', regex=False).str.replace(r'\s+', ' ', regex=True).str.strip())
            .query("County != 'County'")
            .assign(value=lambda d: d['value'].astype(str).str.replace(r'\((.*)\)', r'-\1', regex=True))
            .pipe(tidy.tidy)
            .assign(sector=lambda d: d['sector'].replace(sector_mapping))
            .query("sector != 'gcp'")
            .reset_index(drop=True)
        )
        frames.append(processed)

    return pd.concat(frames, ignore_index=True)
