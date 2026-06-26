from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent
SCRAPERS_DIR = PROJECT_ROOT / "src" / "plus254" / "collectors"
DOCS_DIR = PROJECT_ROOT / "docs" / "datasets"
ASTRO_DIR = PROJECT_ROOT / ".generated" / "dataset-docs"
SCHEMA_DIR = PROJECT_ROOT / "src" / "plus254" / "api" / "schema"
