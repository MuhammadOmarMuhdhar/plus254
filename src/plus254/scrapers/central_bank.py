import pandas as pd
import numpy as np
import json 
import time
import logging
import pandas as pd
from datasets import Dataset, load_dataset
from huggingface_hub import HfApi
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

with open("src/plus254/scrapers/central_bank.json", "r") as file:
    central_bank_links = json.load(file)


# ── Helper functions ──────────────────────────────────────────────────────

def _extract_columns(df, header_row, data_start_row):
    """Extract column names from a specific row and trim data above it."""
    df = df.copy()
    df.columns = df.iloc[header_row].reset_index(drop=True)
    df = df.iloc[data_start_row:].reset_index(drop=True)
    return df


def _normalize_columns(df):
    """Strip whitespace and lowercase column names."""
    df = df.copy()
    df.columns = df.columns.str.strip().str.lower()
    return df


def _convert_month_to_name(df, month_col='month'):
    """Convert integer month to full month name."""
    df = df.copy()
    df[month_col] = df[month_col].astype(int).apply(
        lambda x: pd.to_datetime(str(x), format='%m').strftime('%B')
    )
    return df


def _set_month_categorical(df, month_col='month'):
    """Set month column as ordered categorical."""
    df = df.copy()
    month_order = pd.date_range('2000-01', periods=12, freq='MS').strftime('%B').tolist()
    df[month_col] = pd.Categorical(df[month_col], categories=month_order, ordered=True)
    return df


def _clean_numeric_values(df, col='value'):
    """Clean comma-separated strings and convert to numeric."""
    df = df.copy()
    df[col] = df[col].astype(str).str.replace(',', '').replace('NaN', np.nan)
    df = df.dropna(subset=[col])
    df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


def _capitalize_columns(df):
    """Standardize column names to Title Case."""
    df = df.copy()
    df.columns = df.columns.str.capitalize()
    return df


# ── Data processing functions ───────────────────────────────────────────────

def process_forex_df(df_dict):
    df_results = {}

    for forex_df in ['forex_end_period', 'forex_period_average']:
        df = df_dict[forex_df]

        df.columns = df.iloc[1]
        df = _normalize_columns(df)
        df = df.iloc[2:].reset_index(drop=True)
        df['year'] = df['year'].astype(int)
        df = _convert_month_to_name(df, 'month')
        df_long = df.melt(
            id_vars=['year', 'month'],
            var_name='metric',
            value_name='value'
        )
        df_long = _set_month_categorical(df_long, 'month')
        df_long = df_long.sort_values(['year', 'month']).reset_index(drop=True)
        df_long = _capitalize_columns(df_long)
        df_results[forex_df] = df_long

    return df_results


def process_monetary_survey(df_dict):
    df = df_dict['monetary_survey']
    years = df.iloc[0, 2:].fillna(method='ffill').astype(int).values
    months = df.iloc[2, 2:].values

    date_cols = [f"{y}-{m}" for y, m in zip(years, months)]
    df.columns = ['section_code', 'indicator'] + date_cols
    df = df.iloc[3:].copy()

    df = df.replace('NaN', np.nan).dropna(subset=['indicator'], how='all')
    df['section_code'] = df['section_code'].fillna(method='ffill')

    section_map = {
        'A.': 'Central Bank of Kenya',
        'B': 'Other Depository Corporation Survey',
        'C': 'Depository Corporation Survey'
    }
    df['section'] = df['section_code'].map(section_map)

    value_cols = [c for c in df.columns if c not in ['section_code', 'indicator', 'section']]
    df_long = df.melt(
        id_vars=['section', 'indicator'],
        value_vars=value_cols,
        var_name='period',
        value_name='value'
    )

    df_long[['year', 'month']] = df_long['period'].str.split('-', expand=True)
    df_long['year'] = df_long['year'].astype(int)
    df_long['month'] = df_long['month'].str.strip()
    df_long['month'] = df_long['month'].str.replace('Sept', 'Sep')
    df_long['month'] = pd.to_datetime(df_long['month'], format='%b').dt.strftime('%B')

    df_long = _clean_numeric_values(df_long, 'value')
    df_long = df_long[['section', 'indicator', 'year', 'month', 'value']].sort_values(
        ['section', 'indicator', 'year', 'month']
    ).reset_index(drop=True)

    df_long = _set_month_categorical(df_long, 'month')
    df_long = df_long.sort_values(['year', 'month']).reset_index(drop=True)
    df_long = _capitalize_columns(df_long)
    return df_long


def process_bop_annual(df_dict):
    df = df_dict['bop_annual']

    df.columns = df.iloc[2]
    df = _normalize_columns(df)
    df = df.iloc[3:].reset_index(drop=True)

    df_long = df.melt(
        id_vars=['bpm6 concept'],
        var_name='year',
        value_name='value'
    )

    df_long['year'] = df_long['year'].astype(int)
    df_long = df_long.sort_values(['year']).reset_index(drop=True)
    df_long.rename(columns={'bpm6 concept': 'category'}, inplace=True)

    df_long = _capitalize_columns(df_long)
    return df_long


def process_exports_global(df_dict):
    df = df_dict['exports_global']
    df = _extract_columns(df, 2, 3)
    df = _normalize_columns(df)

    id_vars = ['year', 'month']
    value_vars = [
        'U.K', 'GERMANY', 'U.S.A', 'NETHERLANDS', 'UGANDA',
        'TANZANIA', 'PAKISTAN', 'FRANCE', 'EGYPT', 'BELGIUM', 'OTHERS', 'TOTAL'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_exports_africa(df_dict):
    df = df_dict['exports_africa']
    df = _extract_columns(df, 2, 3)
    df = _normalize_columns(df)

    id_vars = ['year', 'month']
    value_vars = [
        'UGANDA',
        'TANZANIA',
        'ZAMBIA',
        'EGYPT',
        'RWANDA',
        'ZIMBABWE',
        'ETHIOPIA',
        'SOMALIA',
        'South AFRICA',
        'DRC',
        'Other',
        'Total'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_domestic_exports(df_dict):
    df = df_dict['domestic_exports']
    df = _extract_columns(df, 3, 6)
    df = _normalize_columns(df)

    id_vars = ['year', 'month']
    value_vars = [
        'Coffee',
        'Tea',
        'Petroleum',
        'Chemicals',
        'Fish',
        'Horticulture',
        'Cement',
        'Other',
        'Total'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_imports_global(df_dict):
    df = df_dict['imports_global']
    df = _extract_columns(df, 2, 3)
    df = _normalize_columns(df)

    id_vars = ['year', 'month']
    value_vars = [
        'U.K',
        'U.S.A',
        'GERMANY',
        'ITALY',
        'U.A.E',
        'S.ARABIA',
        'FRANCE',
        'INDIA',
        'S.AFRICA',
        'JAPAN',
        'CHINA',
        'OTHERS',
        'TOTAL'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_imports_africa(df_dict):
    df = df_dict['imports_africa']
    df = _extract_columns(df, 4, 5)
    df = _normalize_columns(df)

    id_vars = ['year', 'month']
    value_vars = [
        'UGANDA',
        'TANZANIA',
        'ZAMBIA',
        'EGYPT',
        'South AFRICA',
        'ZIMBABWE',
        'Other',
        'Total'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_imports_commodity(df_dict):
    df = df_dict['imports_commodity']
    df = _extract_columns(df, 2, 4)
    df = _normalize_columns(df)

    id_vars = ['year', 'month']
    value_vars = [
        'Food and Live Animals',
        'Beverages and Tobacco',
        'Crude Materials Inedible except Fuels',
        'Mineral Fuels Lubricants and related Materials',
        'Animals and Vegetable Oils and Fats',
        'Chemicals',
        'Manufactured Goods Classified Chiefly by Materials',
        'Machinery and Transport Equipment',
        'Other',
        'TOTAL'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_principal_exports(df_dict):
    df = df_dict['principal_exports']
    df = df.iloc[7:].reset_index(drop=True)

    df.columns = [
        'year', 'month',
        'coffee volume', 'coffee value', 'coffee average',
        'tea volume', 'tea value', 'tea average',
        'horticulture volume', 'horticulture value', 'horticulture average'
    ]

    id_vars = ['year', 'month']
    value_vars = [
        'coffee volume', 'coffee value', 'coffee average',
        'tea volume', 'tea value', 'tea average',
        'horticulture volume', 'horticulture value', 'horticulture average'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_fiscal_revenue_expenditure(df_dict):
    df = df_dict['fiscal_revenue_expenditure']
    df = df.iloc[7:].reset_index(drop=True)

    df.columns = [
        'fiscal year', 'month',
        'import duty', 'excise duty', 'income tax', 'vat', 'other tax income', 'total tax revenue',
        'non tax revenue', 'total revenue',
        'programme grants', 'project grants', 'total grants',
        'domestic interest', 'foreign interest', 'wages salaries', 'pensions', 'other recurrent', 'total recurrent expenditure',
        'county transfer', 'development expenditure', 'total expenditure'
    ]

    id_vars = ['fiscal year', 'month']
    df.dropna(subset=id_vars, inplace=True)
    df['fiscal year'] = df['fiscal year'].astype(int)
    df = _convert_month_to_name(df, 'month')

    # --- Revenue ---
    revenue_cols = [
        'import duty', 'excise duty', 'income tax', 'vat', 'other tax income', 'total tax revenue',
        'non tax revenue', 'total revenue'
    ]
    revenue = df[id_vars + revenue_cols].melt(id_vars=id_vars, var_name='metric', value_name='value')
    revenue = _set_month_categorical(revenue, 'month')

    # --- Grants ---
    grants_cols = ['programme grants', 'project grants', 'total grants']
    grants = df[id_vars + grants_cols].melt(id_vars=id_vars, var_name='metric', value_name='value')
    grants = _set_month_categorical(grants, 'month')

    # --- Expenditure ---
    expenditure_cols = [
        'domestic interest', 'foreign interest', 'wages salaries', 'pensions', 'other recurrent',
        'total recurrent expenditure', 'county transfer', 'development expenditure', 'total expenditure'
    ]
    expenditure = df[id_vars + expenditure_cols].melt(id_vars=id_vars, var_name='metric', value_name='value')
    expenditure = _set_month_categorical(expenditure, 'month')

    # Capitalize and return
    revenue = _capitalize_columns(revenue)
    grants = _capitalize_columns(grants)
    expenditure = _capitalize_columns(expenditure)

    return {'revenue': revenue, 'grants': grants, 'expenditure': expenditure}


def process_public_debt(df_dict):
    df = df_dict['public_debt']
    df = _extract_columns(df, 3, 4)
    df = _normalize_columns(df)

    id_vars = ['year', 'month']
    value_vars = ['domestic debt', 'external debt', 'total']

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)
    df['month'] = df['month'].astype(int)
    df = _convert_month_to_name(df, 'month')

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_domestic_debt(df_dict):
    df = df_dict['domestic_debt']
    df = _extract_columns(df, 2, 4)
    df['fiscal year'] = df['fiscal year'].str.strip()
    df = df[df['fiscal year'].str.match(r'^[\w]+-[\w]+$', na=False)]

    df['parsed'] = pd.to_datetime('01-' + df['fiscal year'], format='mixed')
    df['year'] = df['parsed'].dt.year
    df['month'] = df['parsed'].dt.strftime('%B')
    df = df.drop(columns='parsed')
    df.columns = df.columns.str.strip().str.replace(r'\*+', '', regex=True).str.strip().str.lower()

    id_vars = ['year', 'month']
    value_vars = [
        'treasury bills',
        'treasury bonds',
        'government stocks',
        'overdraft at central bank',
        'advances from commercial banks',
        'other domestic debt',
        'total domestic debt'
    ]

    df.dropna(subset=id_vars, inplace=True)
    df['year'] = df['year'].astype(int)

    df_long = df.melt(
        id_vars=id_vars,
        value_vars=value_vars,
        var_name='metric',
        value_name='value'
    )

    df_long = _set_month_categorical(df_long, 'month')
    df_long = _capitalize_columns(df_long)
    return df_long


def process_gdp_quarterly(df_dict):
    df = df_dict['gdp_quarterly']

    years = df.iloc[2, 2:].ffill().bfill().astype(int).values
    quarters = df.iloc[3, 2:].values
    date_cols = [f"{y}-{q}" for y, q in zip(years, quarters)]

    df.columns = ['0', 'activity'] + date_cols
    df = df.iloc[4:].copy()
    df = df.replace('NaN', np.nan).dropna(subset=['activity'], how='all')

    value_cols = [c for c in df.columns if c not in ['0', 'activity']]
    df_long = df.melt(
        id_vars=['activity'],
        value_vars=value_cols,
        var_name='period',
        value_name='value'
    )

    df_long[['year', 'quarter']] = df_long['period'].str.split('-', expand=True)
    df_long['year'] = df_long['year'].astype(int)
    df_long['quarter'] = df_long['quarter'].str.strip()
    df_long.drop(columns=['period'], inplace=True)

    df_long = _clean_numeric_values(df_long, 'value')

    df_long = df_long.sort_values(['year', 'quarter', 'activity']).reset_index(drop=True)
    df_long = _capitalize_columns(df_long)

    return df_long


