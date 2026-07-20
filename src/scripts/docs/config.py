from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
CANONICAL_YAML = PROJECT_ROOT / "src" / "plus254" / "datasets.yaml"
OUTPUT_DIR = PROJECT_ROOT / ".generated" / "dataset-docs"
SCHEMA_DIR = PROJECT_ROOT / "src" / "plus254" / "api" / "schema"
