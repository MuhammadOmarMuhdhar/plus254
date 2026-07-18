import pandas as pd


def _format_failures(failures: pd.DataFrame) -> str:
    lines = []
    grouped = failures.groupby("check", sort=False)

    for check, group in grouped:
        if check == "column_in_schema":
            cols = ", ".join(group["failure_case"].dropna().unique())
            lines.append(f"  Columns in DataFrame but not in schema: {cols}")

        elif check == "column_in_dataframe":
            cols = ", ".join(group["failure_case"].dropna().unique())
            lines.append(f"  Columns in schema but not in DataFrame: {cols}")

        elif check == "not_nullable":
            for _, row in group.iterrows():
                lines.append(
                    f"  Null in non-nullable column '{row['column']}' at row {int(row['index'])}"
                )

        elif check == "dtype":
            for _, row in group.iterrows():
                lines.append(
                    f"  Type mismatch in '{row['column']}': expected {row['failure_case']}"
                )

        else:
            for _, row in group.iterrows():
                parts = []
                if pd.notna(row.get("column")):
                    parts.append(f"column='{row['column']}'")
                if pd.notna(row.get("failure_case")):
                    parts.append(f"value={row['failure_case']}")
                if pd.notna(row.get("index")):
                    parts.append(f"row={int(row['index'])}")
                lines.append(f"  {check}: {', '.join(parts)}")

    return "\n".join(lines)


class ContractViolation(Exception):
    """Raised when a DataFrame fails validation against its datasets.yaml contract."""

    def __init__(self, config_name: str, failures: pd.DataFrame):
        self.config_name = config_name
        self.failures = failures
        super().__init__(
            f"Contract violation for '{config_name}' -- {len(failures)} failure(s)\n"
            f"{_format_failures(failures)}"
        )

class QualityViolation(Exception):
    """Raised when a data quality check fails at the upload gate."""