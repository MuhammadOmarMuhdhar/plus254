import pandas as pd
from plus254.utils.tidy import tidy


def process_registered_voters(df):

    df.columns = df.iloc[0]
    df = df.iloc[1:]

    df = tidy(df, value_col="registered voters")
    df = df.rename(columns={"registered_voters": "value"})

    return df
