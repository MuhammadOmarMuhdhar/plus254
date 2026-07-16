from plus254.utils.transformers import tidy, frame
import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Common preprocessing for all fiscal datasets."""
    clean_df =  (
        df.copy()
        .pipe(frame._promote_header_row, 4, 5)
        .iloc[2:]
        .pipe(lambda d: d.set_axis(
            ['year', 'month'] + d.columns[2:].tolist(), axis=1
        ))
        .assign(year=lambda d: d["year"].astype(int), month=lambda d: d["month"].astype(int))
        .pipe(tidy._month_int_to_name, month_col="month")
        .pipe(
            lambda d: d.melt(
                id_vars=["year", "month"],
                value_vars=[c for c in d.columns if c not in ["fiscal_year", "month"]],
                var_name="item",
                value_name="value"
            )
        )
        .pipe(tidy._tidy)
        .assign(item=lambda d: tidy._replace_words(d, 2, {
                'import': 'import duty',
                'excise': 'excise duty',
                'income': 'income tax',
                'other': 'other tax',
                'programme': 'programme grants',
                'expenditure': 'development expenditure',
               
            }))
        .reset_index(drop=True)
    )

    revenue_df = clean_df.query("item in ['import duty', 'excise duty', 'income tax', 'vat', 'other tax']").reset_index(drop=True)
    grants_df = clean_df.query("item in ['programme grants', 'grants' ]").reset_index(drop=True)    
    expenditure_df = clean_df.query("item in ['domestic interest', 'foreign interest', 'wages and salaries', 'pensions', 'other' , 'development expenditure']").reset_index(drop=True)

    return {
            
            "fiscal_revenue": revenue_df,
            "fiscal_grants": grants_df,
            "fiscal_expenditure": expenditure_df
    }