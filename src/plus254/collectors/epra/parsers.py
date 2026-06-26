import pandas as pd
from plus254.utils.tidy import (
    tidy, extract_year_month
)

def fuel_prices(df):
    df = extract_year_month(df, date_col='From', date_format="%d-%m-%Y", year_col="year", month_col="month")

    df_long = df.melt(
        id_vars=['From', 'year', 'month', 'Town'],
        value_vars=['Super (PMS)', 'Diesel (AGO)', 'Kerosene (IK)'],
        var_name='Fuel Type',
        value_name='Price'
    )

    df_long.rename(columns={'From': 'Date', 'Town': 'Location', 'Price': 'Value', 'Fuel Type': 'item'}, inplace=True)
    df_long = tidy(df_long)

    return 'pump_prices', df_long