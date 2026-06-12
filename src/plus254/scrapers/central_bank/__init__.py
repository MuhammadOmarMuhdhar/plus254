import yaml

from .forex import process_forex
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

_yaml_path = Path(__file__).resolve().parent / "datasets.yaml"
with open(_yaml_path) as f:
    _raw = yaml.safe_load(f)

# Build scraper URL mapping from the metadata YAML.
# Most config_names match 1:1. Fiscal datasets share one scraper alias
# because the single CSV is split into 3 datasets at processing time.
_SCRAPER_LINKS = {
    "forex_end_period": _raw["forex_end_period"]["url"],
    "forex_period_average": _raw["forex_period_average"]["url"],
    "monetary_survey": _raw["monetary_survey"]["url"],
    "bop_annual": _raw["bop_annual"]["url"],
    "exports_global": _raw["exports_global"]["url"],
    "exports_africa": _raw["exports_africa"]["url"],
    "domestic_exports": _raw["domestic_exports"]["url"],
    "imports_global": _raw["imports_global"]["url"],
    "imports_africa": _raw["imports_africa"]["url"],
    "imports_commodity": _raw["imports_commodity"]["url"],
    "principal_exports": _raw["principal_exports"]["url"],
    "fiscal_revenue_expenditure": _raw["fiscal_revenue"]["url"],
    "public_debt": _raw["public_debt"]["url"],
    "domestic_debt": _raw["domestic_debt"]["url"],
    "gdp_quarterly": _raw["gdp_quarterly"]["url"],
}

central_bank_links = _SCRAPER_LINKS
