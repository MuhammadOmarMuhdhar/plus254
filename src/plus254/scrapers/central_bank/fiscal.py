from plus254.utils.df_utils import (
    convert_month_to_name,
    set_month_categorical,
    capitalize_columns,
    clean_numeric_values,
)


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
    df = convert_month_to_name(df, "month")

    revenue_cols = [
        "import duty", "excise duty", "income tax", "vat", "other tax income", "total tax revenue",
        "non tax revenue", "total revenue",
    ]
    revenue = df[id_vars + revenue_cols].melt(id_vars=id_vars, var_name="metric", value_name="value")
    revenue = clean_numeric_values(revenue, "value")
    revenue = set_month_categorical(revenue, "month")

    grants_cols = ["programme grants", "project grants", "total grants"]
    grants = df[id_vars + grants_cols].melt(id_vars=id_vars, var_name="metric", value_name="value")
    grants = clean_numeric_values(grants, "value")
    grants = set_month_categorical(grants, "month")

    expenditure_cols = [
        "domestic interest", "foreign interest", "wages salaries", "pensions", "other recurrent",
        "total recurrent expenditure", "county transfer", "development expenditure", "total expenditure",
    ]
    expenditure = df[id_vars + expenditure_cols].melt(id_vars=id_vars, var_name="metric", value_name="value")
    expenditure = clean_numeric_values(expenditure, "value")
    expenditure = set_month_categorical(expenditure, "month")

    revenue = capitalize_columns(revenue)
    grants = capitalize_columns(grants)
    expenditure = capitalize_columns(expenditure)

    return {"revenue": revenue, "grants": grants, "expenditure": expenditure}
