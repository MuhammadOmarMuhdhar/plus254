import pandas as pd


def describe_column(series):
    col_dtype = series.dtype
    null_count = int(series.isna().sum())
    non_null = series.dropna()

    info = {
        "dtype": str(col_dtype),
        "nullable": null_count > 0,
        "null_count": null_count,
        "non_null_count": int(len(series) - null_count),
        "sample_values": non_null.head(5).tolist(),
    }

    if pd.api.types.is_numeric_dtype(col_dtype):
        desc = series.describe()
        info["stats"] = {
            "count": int(desc["count"]),
            "mean": float(desc["mean"]),
            "std": float(desc["std"]),
            "min": float(desc["min"]),
            "25%": float(desc["25%"]),
            "50%": float(desc["50%"]),
            "75%": float(desc["75%"]),
            "max": float(desc["max"]),
        }

    if pd.api.types.is_datetime64_any_dtype(col_dtype):
        info["stats"] = {
            "min": str(series.min()),
            "max": str(series.max()),
        }

    return info
