import pandas as pd
import numpy as np
from plus254.utils.transformers import tidy, frame

def transform(records):

    dfs = []
    for record in records:
        year = record["year"]
        quarter = record["quarter"]
        raw_df = record["raw_df"]

        if isinstance(raw_df, list):
            processed = []
            for tbl in raw_df:
                tbl = tbl.copy()
                col0_vals = tbl.iloc[:, 0].astype(str).str.lower().str.strip() if tbl.shape[1] > 0 else pd.Series(dtype=str)
                has_advisory = col0_vals.str.contains(
                    r'digitalinvestigations|digitalforensics',
                    na=False, regex=True
                ).any()
                indicator = "advisories" if has_advisory else "threats"
                tbl.columns = range(tbl.shape[1])
                tbl.insert(0, "__indicator__", indicator)
                processed.append(tbl)
            df_working = pd.concat(processed, ignore_index=True)
            df_working.columns = range(df_working.shape[1])
        else:
            df_working = raw_df
            if df_working.shape[1] > 0:
                col0_vals = df_working.iloc[:, 0].astype(str).str.lower().str.strip()
                has_indicator = (
                    col0_vals.str.contains(r'^(threat|advisory)', na=False, regex=True).any()
                )
                if not has_indicator:
                    has_advisory_content = col0_vals.str.contains(
                        r'digitalinvestigations|digitalforensics',
                        na=False, regex=True
                    ).any()
                    indicator = "advisories" if has_advisory_content else "threats"
                    df_working = df_working.copy()
                    df_working.columns = range(df_working.shape[1])
                    df_working.insert(0, "__indicator__", indicator)
                    df_working.columns = range(df_working.shape[1])

        transformed = (
            df_working
            .pipe(tidy.normalise_nulls)
            .pipe(frame.drop_header_artifact_rows)
            .pipe(frame.merge_shifted_columns)
            .pipe(lambda d: (
                d.assign(**{d.columns[0]: d.iloc[:, 0].fillna(d.iloc[:, 1])})
                .iloc[:, [i for i in range(d.shape[1]) if i != 1]]
                if d.shape[1] >= 2
                and d.iloc[:, 0].isna().mean() > 0.5
                and d.iloc[:, 1].isna().mean() > 0.5
                else d
            ))
            .pipe(tidy.forward_fill, [0])
            .pipe(lambda d: d.dropna(how="all", axis=1))
            .iloc[:, 0:3]
            .set_axis(["metric", "item", "value"], axis=1)
            .assign(year=year, quarter=quarter)
            .pipe(tidy.tidy)
            .assign(item=lambda d: tidy.replace_words(d, 1, {
                "malware": "malware",
                "brute": "brute force attacks",
                "web": "web application attacks",
                "system": "system vulnerabilities",
                "mobile": "mobile application attacks",
                "ddos": "ddos",
                "digitalinvestigations": "digital investigations",
                "digitalforensics": "digital forensics",
            }))
            [["year", "quarter", "metric", "item", "value"]]
            .reset_index(drop=True)
        )
        dfs.append(transformed)

    df_combined = pd.concat(dfs, ignore_index=True)
    df_combined = tidy.sort_by_date(df_combined)
    return df_combined.reset_index(drop=True)