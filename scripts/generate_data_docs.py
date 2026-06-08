#!/usr/bin/env python3
"""Generate dataset documentation from live data on Hugging Face.

Outputs:
  - docs/datasets/*.md               — Human-readable Markdown per dataset
  - docs/datasets/index.md           — Dataset index page
  - src/plus254/api/schema/*.json    — Machine-readable JSON schemas

Usage:
  python scripts/generate_data_docs.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

import pandas as pd
import yaml
import json
from plus254.api.data import get_dataset
from plus254.api.config import DATASETS

PROJECT_ROOT = Path(__file__).resolve().parent.parent
YAML_PATH = PROJECT_ROOT / "src" / "plus254" / "api" / "datasets.yaml"
DOCS_DIR = PROJECT_ROOT / "docs" / "datasets"
SCHEMA_DIR = PROJECT_ROOT / "src" / "plus254" / "api" / "schema"

with open(YAML_PATH) as f:
    schema_config = yaml.safe_load(f)


def describe_column(series):
    col_dtype = series.dtype
    null_count = int(series.isna().sum())
    non_null = series.dropna()

    info = {
        "dtype": str(col_dtype),
        "nullable": null_count > 0,
        "null_count": null_count,
        "non_null_count": int(len(series) - null_count),
        "sample_values": non_null.head(5).tolist(),
    }

    if pd.api.types.is_numeric_dtype(col_dtype):
        desc = series.describe()
        info["stats"] = {
            "count": int(desc["count"]),
            "mean": float(desc["mean"]),
            "std": float(desc["std"]),
            "min": float(desc["min"]),
            "25%": float(desc["25%"]),
            "50%": float(desc["50%"]),
            "75%": float(desc["75%"]),
            "max": float(desc["max"]),
        }

    if pd.api.types.is_datetime64_any_dtype(col_dtype):
        info["stats"] = {
            "min": str(series.min()),
            "max": str(series.max()),
        }

    return info


def esc(text):
    return str(text).replace("|", "\\|")


def generate_markdown(config_name, df, info, columns_info):
    lines = []
    lines.append(f"# {info['name']}")
    lines.append("")
    lines.append(info["description"])
    lines.append("")
    lines.append(f"- **Source:** {info['source']}")
    lines.append(f"- **API endpoint:** `GET /{info['slug']}/{config_name}`")
    lines.append(f"- **Rows:** {len(df)}")
    if info.get("url"):
        lines.append(f"- **Source URL:** [{info['url']}]({info['url']})")
    lines.append("")

    lines.append("## Columns")
    lines.append("")
    lines.append("| Column | Type | Description | Nullable | Null count | Unique |")
    lines.append("|--------|------|-------------|----------|------------|--------|")
    for col, col_info in columns_info.items():
        nullable = "Yes" if col_info["nullable"] else "No"
        unique = df[col].nunique()
        lines.append(
            f"| {esc(col)} | {esc(col_info['dtype'])} | {esc(col_info.get('description', ''))} | {nullable} | {col_info['null_count']} | {unique} |"
        )
    lines.append("")

    lines.append("## Sample Values")
    lines.append("")
    for col, col_info in columns_info.items():
        samples = col_info["sample_values"]
        if samples:
            sample_str = ", ".join(str(s) for s in samples[:3])
            suffix = " ..." if len(samples) > 3 else ""
            lines.append(f"- **{esc(col)}:** {esc(sample_str)}{suffix}")
    lines.append("")

    numeric_cols = {
        c: v for c, v in columns_info.items() if "stats" in v and "mean" in v["stats"]
    }
    if numeric_cols:
        lines.append("## Summary Statistics")
        lines.append("")
        lines.append("| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |")
        lines.append("|--------|-------|------|-----|-----|-----|-----|-----|-----|")
        for col, cinfo in numeric_cols.items():
            s = cinfo["stats"]
            fmt = lambda v: f"{v:.4g}" if abs(v) > 1e6 else f"{v:.2f}"
            lines.append(
                f"| {esc(col)} | {s['count']} | {fmt(s['mean'])} | {fmt(s['std'])} | {fmt(s['min'])} | {fmt(s['25%'])} | {fmt(s['50%'])} | {fmt(s['75%'])} | {fmt(s['max'])} |"
            )
        lines.append("")

    lines.append("## Sample Data")
    lines.append("")
    sample = df.head(5)
    headers = [esc(c) for c in sample.columns]
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|" + "|".join("---" for _ in headers) + "|")
    for _, row in sample.iterrows():
        cells = [esc(str(row[c])) for c in sample.columns]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")

    return "\n".join(lines)


def generate_index(datasets_info):
    lines = []
    lines.append("# Datasets")
    lines.append("")
    lines.append("All datasets available through the plus254 API.")
    lines.append("")

    groups = {}
    for config_name, info in sorted(datasets_info.items()):
        groups.setdefault(info["slug"], []).append((config_name, info))

    for slug, datasets in sorted(groups.items()):
        lines.append(f"## {slug}")
        lines.append("")
        lines.append("| Dataset | Description | Rows | Endpoint |")
        lines.append("|---------|-------------|------|----------|")
        for config_name, info in sorted(datasets):
            rows = info.get("row_count", "?")
            lines.append(
                f"| [{info['name']}]({config_name}.md) | {info['description']} | {rows} | `GET /{slug}/{config_name}` |"
            )
        lines.append("")

    return "\n".join(lines)


def run():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)

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

        schema = {
            "config": config_name,
            "slug": info["slug"],
            "name": info["name"],
            "source": info["source"],
            "description": info["description"],
            "url": info.get("url", ""),
            "row_count": row_count,
            "columns": [
                {
                    "name": col,
                    "type": col_info["dtype"],
                    "description": col_info.get("description", ""),
                    "nullable": col_info["nullable"],
                    "null_count": col_info["null_count"],
                    "non_null_count": col_info["non_null_count"],
                    "sample_values": col_info["sample_values"][:5],
                    "stats": col_info.get("stats"),
                }
                for col, col_info in columns_info.items()
            ],
        }

        schema_path = SCHEMA_DIR / f"{config_name}.json"
        with open(schema_path, "w") as f:
            json.dump(schema, f, indent=2, default=str)
        print(f"  Schema -> {schema_path}")

        md = generate_markdown(config_name, df, info, columns_info)
        md_path = DOCS_DIR / f"{config_name}.md"
        with open(md_path, "w") as f:
            f.write(md)
        print(f"  Markdown -> {md_path}")

    index_md = generate_index(datasets_info)
    index_path = DOCS_DIR / "index.md"
    with open(index_path, "w") as f:
        f.write(index_md)
    print(f"Index -> {index_path}")

    print(f"\nDone. Generated {len(datasets_info)} dataset docs.")


if __name__ == "__main__":
    run()
