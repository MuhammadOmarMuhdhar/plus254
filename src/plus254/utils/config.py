"""Centralised dataset manifest helpers."""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any
import yaml

DEFAULT_DATASETS_YAML = Path("src/plus254/datasets.yaml")


def load_datasets(yaml_path: Path | str = DEFAULT_DATASETS_YAML) -> dict[str, Any]:
    """Load the full datasets manifest."""
    with open(yaml_path) as f:
        return yaml.safe_load(f) or {}


def load_dataset_spec(yaml_path: Path | str, slug: str) -> dict[str, Any]:
    """Return the YAML spec for a single dataset slug.

    Raises
    ------
    ValueError
        If *slug* is not present in the manifest.
    """
    raw = load_datasets(yaml_path)
    spec = raw.get(slug)
    if not spec:
        raise ValueError(
            f"'{slug}' not found in {yaml_path}. Available: {sorted(raw.keys())}"
        )
    return spec


def bump_last_updated(yaml_path: Path | str, slug: str) -> None:
    """Rewrite ``datasets.yaml`` with the current UTC timestamp for *slug*."""
    yaml_path = Path(yaml_path)
    raw = load_datasets(yaml_path)

    if slug not in raw:
        raise ValueError(f"Slug '{slug}' not found in {yaml_path}")

    raw[slug]["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    with open(yaml_path, "w") as f:
        yaml.dump(
            raw,
            f,
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
        )
