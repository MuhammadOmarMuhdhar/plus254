import pandas as pd
from plus254.utils.transformers import tidy

def transform(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.copy()
        .pipe(lambda d: d.set_axis(d.iloc[1].tolist(), axis=1))
        .pipe(tidy.normalize_column_names)
        .iloc[2:]
        .assign(**{
            "bpm6 concept": lambda d: (
                d["bpm6 concept"]
                .astype(str)
                .str.strip()
                .str.lower()
                .str.replace(r"^[a-f]\.\s*", "", regex=True)          
                .str.replace(r"n\.\s*i\.\s*e\.", "n.i.e.", regex=True) 
                .str.replace(r"\s*,\s*", ", ", regex=True)             
                .str.replace(r"\s*:\s*", ": ", regex=True)             
                .str.replace(r"\s+", " ", regex=True)                  
                .str.strip()
            )
        })
        .melt(id_vars=["bpm6 concept"], var_name="year", value_name="value")
        .assign(year=lambda d: d["year"].astype(int))
        .rename(columns={"bpm6_concept": "item"})
        .pipe(tidy.tidy, value_col="value")
        .pipe(lambda d: d.rename(columns={"bpm6_concept": "item"}))
        .drop_duplicates(keep="last")
        .reset_index(drop=True)
        [["year", "item", "value"]]
    )