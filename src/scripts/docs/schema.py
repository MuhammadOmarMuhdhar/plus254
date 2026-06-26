def build_schema(config_name, info, row_count, columns_info):
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
