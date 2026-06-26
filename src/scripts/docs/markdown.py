def html_esc(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


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
    lines.append(f'topic: "{info["slug"]}"')
    if info.get("url"):
        lines.append(f'sourceUrl: "{info["url"]}"')
    if info.get("last_updated"):
        lines.append(f'lastUpdated: "{info["last_updated"]}"')
    lines.append("---")
    lines.append("")
    return lines


def _render_column_table(columns_info, df):
    lines = []
    lines.append("## Columns")
    lines.append("")
    lines.append('<table class="dataset-table">')
    lines.append("<thead>")
    lines.append("<tr><th>Column</th><th>Type</th><th>Description</th><th>Nullable</th><th>Null count</th><th>Unique</th></tr>")
    lines.append("</thead>")
    lines.append("<tbody>")
    for col, col_info in columns_info.items():
        nullable = "Yes" if col_info["nullable"] else "No"
        unique = df[col].nunique()
        desc = html_esc(col_info.get("description", ""))
        lines.append("<tr>")
        lines.append(f'<td data-label="Column"><code>{html_esc(col)}</code></td>')
        lines.append(f'<td data-label="Type">{html_esc(col_info["dtype"])}</td>')
        lines.append(f'<td data-label="Description">{desc}</td>')
        lines.append(f'<td data-label="Nullable">{nullable}</td>')
        lines.append(f'<td data-label="Null count">{col_info["null_count"]}</td>')
        lines.append(f"<td data-label=\"Unique\">{unique}</td>")
        lines.append("</tr>")
    lines.append("</tbody>")
    lines.append("</table>")
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
        lines.append('<table class="dataset-table">')
        lines.append("<thead>")
        lines.append("<tr><th>Column</th><th>Count</th><th>Mean</th><th>Std</th><th>Min</th><th>25%</th><th>50%</th><th>75%</th><th>Max</th></tr>")
        lines.append("</thead>")
        lines.append("<tbody>")
        for col, cinfo in numeric_cols.items():
            s = cinfo["stats"]
            lines.append("<tr>")
            lines.append(f'<td data-label="Column"><code>{html_esc(col)}</code></td>')
            lines.append(f'<td data-label="Count">{s["count"]}</td>')
            lines.append(f'<td data-label="Mean">{_fmt_num(s["mean"])}</td>')
            lines.append(f'<td data-label="Std">{_fmt_num(s["std"])}</td>')
            lines.append(f'<td data-label="Min">{_fmt_num(s["min"])}</td>')
            lines.append(f'<td data-label="25%">{_fmt_num(s["25%"])}</td>')
            lines.append(f'<td data-label="50%">{_fmt_num(s["50%"])}</td>')
            lines.append(f'<td data-label="75%">{_fmt_num(s["75%"])}</td>')
            lines.append(f'<td data-label="Max">{_fmt_num(s["max"])}</td>')
            lines.append("</tr>")
        lines.append("</tbody>")
        lines.append("</table>")
        lines.append("")
    return lines


import json
import math


def _clean_json_val(val):
    if val is None:
        return None
    if hasattr(val, "item"):
        val = val.item()
    if isinstance(val, float) and math.isnan(val):
        return None
    if isinstance(val, (int, float)):
        return val
    return str(val)


def _render_sample_data(df):
    lines = []
    lines.append("## Sample Data")
    lines.append("")
    sample = df.head(5)
    headers = list(sample.columns)
    records = [{col: _clean_json_val(row[col]) for col in headers} for _, row in sample.iterrows()]
    json_str = json.dumps(records, indent=2)
    lines.append(f'<pre class="code-block"><code>{html_esc(json_str)}</code></pre>')
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
