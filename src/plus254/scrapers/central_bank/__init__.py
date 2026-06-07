import json

from .forex import process_forex_df
from .monetary import process_monetary_survey
from .bop import process_bop_annual
from .trade import (
    process_exports_global,
    process_exports_africa,
    process_domestic_exports,
    process_imports_global,
    process_imports_africa,
    process_imports_commodity,
    process_principal_exports,
)
from .fiscal import process_fiscal_revenue_expenditure
from .debt import process_public_debt, process_domestic_debt
from .gdp import process_gdp_quarterly
from pathlib import Path
_json_path = Path(__file__).resolve().parent.parent / "central_bank.json"

with open(_json_path) as f:
    central_bank_links = json.load(f)
