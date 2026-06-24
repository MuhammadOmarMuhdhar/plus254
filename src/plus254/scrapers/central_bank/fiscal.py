import pandas as pd
from plus254.utils.tidy import tidy, month_int_to_name


def process_fiscal_revenue_expenditure(df_dict):
    df = df_dict["fiscal_revenue_expenditure"]
    df = df.iloc[6:].reset_index(drop=True)

    df.columns = [
        "fiscal year", "month",
        "import duty", "excise duty", "income tax", "vat", "other tax income", "total tax revenue",
        "non tax revenue", "total revenue",
        "programme grants", "project grants", "total grants",
        "domestic interest", "foreign interest", "wages salaries", "pensions", "other recurrent", "total recurrent expenditure",
        "county transfer", "development expenditure", "total expenditure",
    ]

    id_vars = ["fiscal year", "month"]
    df.dropna(subset=id_vars, inplace=True)
    df["fiscal year"] = df["fiscal year"].astype(int)
    df = month_int_to_name(df, "month")

    revenue_cols = [
        "import duty", "excise duty", "income tax", "vat", "other tax income", "total tax revenue",
        "non tax revenue", "total revenue",
    ]
    revenue = df[id_vars + revenue_cols].melt(id_vars=id_vars, var_name="metric", value_name="value")
    revenue = tidy(revenue, month_col="month")

    grants_cols = ["programme grants", "project grants", "total grants"]
    grants = df[id_vars + grants_cols].melt(id_vars=id_vars, var_name="metric", value_name="value")
    grants = tidy(grants, month_col="month")

    expenditure_cols = [
        "domestic interest", "foreign interest", "wages salaries", "pensions", "other recurrent",
        "total recurrent expenditure", "county transfer", "development expenditure", "total expenditure",
    ]
    expenditure = df[id_vars + expenditure_cols].melt(id_vars=id_vars, var_name="metric", value_name="value")
    expenditure = tidy(expenditure, month_col="month")

    return {"revenue": revenue, "grants": grants, "expenditure": expenditure}
