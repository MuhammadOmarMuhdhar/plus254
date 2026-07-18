from pathlib import Path
from typing import List
import yaml
from plus254.utils.config import load_datasets

_EXTRACT_ROOT = Path(__file__).resolve().parents[1] / "extract"
_ROLLING_ROOT = _EXTRACT_ROOT / "dynamic" / "rolling_source"


def _get_rolling_slugs(source: str) -> set[str]:
    """Read a rolling-source manifest and return all dataset slugs mentioned."""
    manifest_path = _ROLLING_ROOT / source / "manifest.yaml"
    if not manifest_path.exists():
        return set()

    with open(manifest_path) as f:
        manifest = yaml.safe_load(f) or []

    slugs: set[str] = set()
    for report in manifest:
        for table in report.get("tables", []):
            slug = table.get("dataset")
            if slug:
                slugs.add(slug)
    return slugs


def _get_all_rolling_slugs() -> dict[str, set[str]]:
    """Return {source_name: {slugs}} for all rolling sources."""
    result: dict[str, set[str]] = {}
    if not _ROLLING_ROOT.exists():
        return result
    for source_dir in _ROLLING_ROOT.iterdir():
        if source_dir.is_dir():
            slugs = _get_rolling_slugs(source_dir.name)
            if slugs:
                result[source_dir.name] = slugs
    return result


def get_slugs(
    yaml_path: str | Path,
    *,
    source_type: str | None = None,
    frequency: str | None = None,
) -> List[str]:
    """Return dataset slugs matching the requested source type and/or frequency."""
    yaml_path = Path(yaml_path)
    datasets = load_datasets(yaml_path)

    all_rolling = _get_all_rolling_slugs()
    any_rolling_slugs: set[str] = (
        set().union(*all_rolling.values()) if all_rolling else set()
    )

    matched: list[str] = []

    for slug, spec in datasets.items():
        inferred: str | None = None
        if (_EXTRACT_ROOT / "dynamic" / "fixed_source" / f"{slug}.py").exists():
            inferred = "fixed"
        elif (_EXTRACT_ROOT / "static" / f"{slug}.py").exists():
            inferred = "static"
        elif slug in any_rolling_slugs:
            for source_name, source_slugs in all_rolling.items():
                if slug in source_slugs:
                    inferred = f"rolling_{source_name}"
                    break

        if inferred is None:
            continue

        if source_type is not None:
            if source_type == "rolling":
                if not inferred.startswith("rolling_"):
                    continue
            else:
                if inferred != source_type:
                    continue

        if frequency is not None:
            spec_freq = spec.get("update_frequency", "")
            if spec_freq != frequency:
                continue

        matched.append(slug)

    return sorted(matched)
