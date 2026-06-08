from dotenv import load_dotenv
import os

load_dotenv()

HF_REPO_ID = os.environ.get("HF_REPO_ID")

DATASETS = {
    "forex_end_period": {
        "name": "Monthly Exchange Rates (End Period)",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly exchange rates of major currencies against KES (end period)",
        "url": "https://www.centralbank.go.ke/uploads/exchange_rates/677633335_Monthly%20exchange%20rate%20(end%20period).csv",
    },
    "forex_period_average": {
        "name": "Monthly Exchange Rates (Period Average)",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly exchange rates of major currencies against KES (period average)",
        "url": "https://www.centralbank.go.ke/uploads/exchange_rates/2034093818_Monthly%20Exchange%20rate%20(period%20average).csv",
    },
    "monetary_survey": {
        "name": "Depository Corporation Survey",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monetary aggregates from the Depository Corporation Survey",
        "url": "https://www.centralbank.go.ke/uploads/monetary_and_finance_statistics/274043565_Depository%20Corporation%20Survey%20-%20CSV.csv",
    },
    "bop_annual": {
        "name": "Balance of Payments (Annual)",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Annual balance of payments statement",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1657248905_Balance%20of%20Payments%20Statement%20(Annual%20Calender%20Year).csv",
    },
    "exports_global": {
        "name": "Value of Exports to Rest of World",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly value of exports to selected countries outside Africa",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/310335175_Value%20of%20Exports%20to%20Selected%20Rest%20of%20World%20Countries.csv",
    },
    "exports_africa": {
        "name": "Value of Exports to Africa",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly value of exports to selected African countries",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1216083243_Value%20of%20Exports%20to%20Selected%20Africa%20Countries.csv",
    },
    "domestic_exports": {
        "name": "Value of Selected Domestic Exports",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly value of selected domestic export commodities",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1306010805_Value%20of%20Selected%20Domestic%20Exports%20-%20Selected%20Comms.csv",
    },
    "imports_global": {
        "name": "Value of Imports from Rest of World",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly value of direct imports from selected countries outside Africa",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1436491729_Value%20of%20Direct%20Imports%20from%20Selected%20Rest%20of%20the%20World%20Countries.csv",
    },
    "imports_africa": {
        "name": "Value of Imports from Africa",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly value of direct imports from selected African countries",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1764709360_Value%20of%20Direct%20Imports%20from%20Selected%20African%20Countries.csv",
    },
    "imports_commodity": {
        "name": "Value of Imports by Commodity",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly value of direct imports classified by SITC sections",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1126743207_Value%20of%20Direct%20Imports%20by%20Commodities.csv",
    },
    "principal_exports": {
        "name": "Principal Exports — Volume, Value, Unit Prices",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly volume, value, and average unit prices of principal exports (coffee, tea, horticulture)",
        "url": "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/766913717_Principal%20Exports_Volume,%20Value%20and%20Unit%20Prices.csv",
    },
    "fiscal_revenue": {
        "name": "Government Revenue",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly government revenue breakdown",
        "url": "https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv",
    },
    "fiscal_grants": {
        "name": "Government Grants",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly government grants received",
        "url": "https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv",
    },
    "fiscal_expenditure": {
        "name": "Government Expenditure",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly government expenditure breakdown",
        "url": "https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv",
    },
    "public_debt": {
        "name": "Public Debt",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly public debt (domestic and external)",
        "url": "https://www.centralbank.go.ke/uploads/government_finance_statistics/565446111_Public%20Debt.csv",
    },
    "domestic_debt": {
        "name": "Domestic Debt by Instrument",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Monthly domestic debt breakdown by instrument (T-bills, bonds, etc.)",
        "url": "https://www.centralbank.go.ke/uploads/government_finance_statistics/1263030173_Domestic%20Debt%20by%20Instrument.csv",
    },
    "gdp_quarterly": {
        "name": "Quarterly GDP",
        "source": "Central Bank of Kenya",
        "slug": "centralbank",
        "description": "Quarterly GDP estimates by sector",
        "url": "https://www.centralbank.go.ke/uploads/national_accounts_statistics/1084903161_Quarterly%20GDP.csv",
    },
    "tea": {
        "name": "Tea Production and Exports",
        "source": "Tea Board of Kenya",
        "slug": "teaboard",
        "description": "Monthly tea production, export volume, and prices",
        "url": "N/A (separate scraper)",
    },
}