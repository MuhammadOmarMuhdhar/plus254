import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from plus254.utils.config import load_datasets, load_dataset_spec
from plus254.utils.loaders import huggingface

from scripts.docs.config import CANONICAL_YAML, OUTPUT_DIR, SCHEMA_DIR
from scripts.docs.analyzer import describe_column
from scripts.docs.markdown import generate_markdown
from scripts.docs.schema import build_schema


def _load_dataset_specs():
    """Return (schema_config: dict, yaml_paths: dict) from canonical YAML."""
    raw = load_datasets(CANONICAL_YAML)
    yaml_paths = {slug: str(CANONICAL_YAML) for slug in raw}
    return raw, yaml_paths


def run(output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)

    schema_config, yaml_paths = _load_dataset_specs()
    datasets_info = {}

    for config_name in sorted(schema_config):
        print(f"Processing: {config_name} ...")

        df = huggingface.pull(config_name)
        if df.empty:
            print(f"  SKIP: no data on HuggingFace")
            continue

        df = df.loc[:, ~df.columns.str.startswith("__")]

        spec = load_dataset_spec(CANONICAL_YAML, config_name)
        col_descriptions = spec.get("columns", {})

        columns_info = {}
        for col in df.columns:
            col_info = describe_column(df[col])
            manual = col_descriptions.get(col, {})
            col_info["description"] = manual.get("description", "")
            columns_info[col] = col_info

        row_count = len(df)
        info = {k: v for k, v in spec.items() if k != "columns"}
        datasets_info[config_name] = {**info, "row_count": row_count}

        schema = build_schema(config_name, info, row_count, columns_info)
        schema_path = SCHEMA_DIR / f"{config_name}.json"
        with open(schema_path, "w") as f:
            json.dump(schema, f, indent=2, default=str)
        print(f"  Schema -> {schema_path}")

        md = generate_markdown(
            config_name, df, info, columns_info,
            yaml_path=CANONICAL_YAML,
        )
        md_path = output_dir / f"{config_name}.md"
        with open(md_path, "w") as f:
            f.write(md)
        print(f"  Markdown -> {md_path}")

    print(f"\nDone. Generated {len(datasets_info)} dataset docs.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate dataset docs")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Output directory for .md files (default: .generated/dataset-docs/)",
    )
    args = parser.parse_args()

    run(args.output_dir)
