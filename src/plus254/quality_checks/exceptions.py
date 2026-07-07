import pandas as pd

class ContractViolation(Exception):
    """Raised when a DataFrame fails validation against its datasets.yaml contract."""

    def __init__(self, config_name: str, failures: pd.DataFrame):
        self.config_name = config_name
        self.failures = failures
        super().__init__(
            f"Contract violation for '{config_name}': {len(failures)} check(s) failed.\n"
            f"{failures.head(20).to_string(index=False)}"
        )

class QualityViolation(Exception):
    """Raised when a data quality check fails at the upload gate."""