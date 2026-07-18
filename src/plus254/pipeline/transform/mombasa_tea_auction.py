from plus254.utils.transformers import tidy, frame
import pandas as pd

def transform(df):
    df_cleaned = (
        df
        .pipe(tidy.normalise_nulls)
        .pipe(frame.promote_header_row, 0, 1)
        .dropna(how="any")
        .pipe(lambda d: d.assign(
            **{"Sale week": d["Sale week"].str.replace(r"WEEK ", "", regex=True)}
        ))
        .pipe(lambda d: d[d["Sale week"] != "Grand Total"])
        .set_axis(["Sale week", "price", "sold", "offered", "unsold"], axis=1)
        .assign(**{"Sale week": lambda d: pd.to_numeric(d["Sale week"], errors="coerce")})
        .assign(date=lambda d: pd.to_datetime("2026-01-01") + pd.to_timedelta(
            (d["Sale week"] - 1) * 7, unit="D"
        ))
        .melt(id_vars=["date"], value_vars=["price", "sold", "offered"],
              var_name="metric", value_name="value")
        .pipe(tidy.sort_by_date)
        .pipe(tidy.tidy)
        .reset_index(drop=True)
    )

    tea_volumes = df_cleaned[df_cleaned["metric"].isin(["sold", "offered"])].reset_index(drop=True)
    tea_prices = df_cleaned[df_cleaned["metric"] == "price"].reset_index(drop=True)
    tea_prices.drop(columns=["metric"], inplace=True)
    
    return {
        "mombasa_tea_auction": tea_volumes,
        "mombasa_tea_auction_price": tea_prices
    }