import re

def snake_case(text: str) -> str:
    """Convert text to snake_case."""
    return re.sub(r"[^A-Za-z0-9]+", "_", str(text)).strip("_").lower()


def _split_camel_case(text: str) -> str:
    """Insert spaces at camelCase boundaries."""
    s = str(text)
    if not s:
        return s
    return re.sub(r"(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", " ", s)


def _squash(text: str) -> str:
    """Strip all non-alphanumeric characters and uppercase."""
    return re.sub(r"[^A-Za-z0-9]", "", str(text)).upper()