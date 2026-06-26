import pandas as pd
from plus254.utils.tidy import tidy


def process_indicator(df):
    """Normalize a raw Kilimo indicator DataFrame."""
    df = tidy(df, value_col="item")
    df["area_level"] = df["area_level"].replace("admin_1", "county")
    df = df.rename(columns={
        "time_period": "year",
        "domain_name": "metric",
        "item_name": "item",
        "data_value": "value",
    })
    df = df[["year", "area_level", "area_name", "metric", "item", "value"]]
    return df
