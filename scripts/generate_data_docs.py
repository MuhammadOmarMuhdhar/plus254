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
ASTRO_DIR = PROJECT_ROOT / "website" / "src" / "content" / "dataset"
SCHEMA_DIR = PROJECT_ROOT / "src" / "plus254" / "api" / "schema"


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


def _fmt_num(v):
    return f"{v:.4g}" if abs(v) > 1e6 else f"{v:.2f}"


def _render_header(config_name, df, info):
    lines = []
    endpoint = f"GET /{info['slug']}/{config_name}"
    lines.append("---")
    lines.append(f'title: "{info["name"]}"')
    lines.append(f'description: "{info["description"]}"')
    lines.append(f'source: "{info["source"]}"')
    lines.append(f"endpoint: \"{endpoint}\"")
    lines.append(f"rows: {len(df)}")
    lines.append(f'category: "{info["slug"]}"')
    if info.get("url"):
        lines.append(f'sourceUrl: "{info["url"]}"')
    lines.append("---")
    lines.append("")
    lines.append(info["description"])
    lines.append("")
    lines.append(f"- **Source:** {info['source']}")
    lines.append(f"- **API endpoint:** `{endpoint}`")
    lines.append(f"- **Rows:** {len(df)}")
    if info.get("url"):
        lines.append(f"- **Source URL:** [{info['url']}]({info['url']})")
    lines.append("")
    return lines


def _render_column_table(columns_info, df):
    lines = []
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
    return lines


def _render_stats_table(columns_info):
    numeric_cols = {
        c: v for c, v in columns_info.items() if "stats" in v and "mean" in v["stats"]
    }
    lines = []
    if numeric_cols:
        lines.append("## Summary Statistics")
        lines.append("")
        lines.append("| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |")
        lines.append("|--------|-------|------|-----|-----|-----|-----|-----|-----|")
        for col, cinfo in numeric_cols.items():
            s = cinfo["stats"]
            lines.append(
                f"| {esc(col)} | {s['count']} | {_fmt_num(s['mean'])} | {_fmt_num(s['std'])} | {_fmt_num(s['min'])} | {_fmt_num(s['25%'])} | {_fmt_num(s['50%'])} | {_fmt_num(s['75%'])} | {_fmt_num(s['max'])} |"
            )
        lines.append("")
    return lines


def _render_sample_data(df):
    lines = []
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
    return lines


def generate_markdown(config_name, df, info, columns_info):
    lines = []
    lines.extend(_render_header(config_name, df, info))
    lines.extend(_render_column_table(columns_info, df))
    lines.extend(_render_stats_table(columns_info))
    lines.extend(_render_sample_data(df))
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


def _build_schema(config_name, info, row_count, columns_info):
    return {
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


def run():
    DOCS_DIR.mkdir(parents=True, exist_ok=True)
    ASTRO_DIR.mkdir(parents=True, exist_ok=True)
    SCHEMA_DIR.mkdir(parents=True, exist_ok=True)

    with open(YAML_PATH) as f:
        schema_config = yaml.safe_load(f)

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

        schema = _build_schema(config_name, info, row_count, columns_info)

        schema_path = SCHEMA_DIR / f"{config_name}.json"
        with open(schema_path, "w") as f:
            json.dump(schema, f, indent=2, default=str)
        print(f"  Schema -> {schema_path}")

        md = generate_markdown(config_name, df, info, columns_info)
        md_path = DOCS_DIR / f"{config_name}.md"
        with open(md_path, "w") as f:
            f.write(md)
        print(f"  Markdown -> {md_path}")
        astro_path = ASTRO_DIR / f"{config_name}.md"
        with open(astro_path, "w") as f:
            f.write(md)
        print(f"  Markdown -> {astro_path}")

    index_md = generate_index(datasets_info)
    index_path = DOCS_DIR / "index.md"
    with open(index_path, "w") as f:
        f.write(index_md)
    print(f"Index -> {index_path}")

    print(f"\nDone. Generated {len(datasets_info)} dataset docs.")


if __name__ == "__main__":
    run()
