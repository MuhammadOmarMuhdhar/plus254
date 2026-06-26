import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent.parent))

from plus254.api.config import DATASETS
from plus254.api.data import get_dataset

from scripts.docs.config import SCRAPERS_DIR, ASTRO_DIR, SCHEMA_DIR
from scripts.docs.analyzer import describe_column
from scripts.docs.markdown import generate_markdown
from scripts.docs.schema import build_schema


def _load_scraper_yamls():
    schema_config = {}
    for yaml_path in sorted(SCRAPERS_DIR.glob("*/datasets.yaml")):
        with open(yaml_path) as f:
            raw = yaml.safe_load(f)
        schema_config.update(raw)
    return schema_config


def run():
    ASTRO_DIR.mkdir(parents=True, exist_ok=True)
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)

    schema_config = _load_scraper_yamls()

    datasets_info = {}

    for config_name in sorted(DATASETS):
        print(f"Processing: {config_name} ...")

        df = get_dataset(config_name)
        if df is None:
            print(f"  SKIP: could not load")
            continue

        df = df.loc[:, ~df.columns.str.startswith("__")]

        info = DATASETS[config_name]
        col_descriptions = schema_config.get(config_name, {}).get("columns", {})

        columns_info = {}
        for col in df.columns:
            col_info = describe_column(df[col])
            manual = col_descriptions.get(col, {})
            col_info["description"] = manual.get("description", "")
            columns_info[col] = col_info

        row_count = len(df)
        datasets_info[config_name] = {**info, "row_count": row_count}

        schema = build_schema(config_name, info, row_count, columns_info)

        schema_path = SCHEMA_DIR / f"{config_name}.json"
        with open(schema_path, "w") as f:
            json.dump(schema, f, indent=2, default=str)
        print(f"  Schema -> {schema_path}")

        md = generate_markdown(config_name, df, info, columns_info)
        astro_path = ASTRO_DIR / f"{config_name}.md"
        with open(astro_path, "w") as f:
            f.write(md)
        print(f"  Markdown -> {astro_path}")

    print(f"\nDone. Generated {len(datasets_info)} dataset docs.")


if __name__ == "__main__":
    run()
