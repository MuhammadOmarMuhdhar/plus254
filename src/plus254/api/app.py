from flask import Flask, jsonify, abort
from .config import DATASETS
from .data import get_dataset
from pathlib import Path
import json as json_lib

app = Flask(__name__)

_SCHEMA_DIR = Path(__file__).resolve().parent / "schema"

@app.get("/")
def list_datasets():
    grouped = {}
    for name, info in DATASETS.items():
        cat = info["category"]
        grouped.setdefault(cat, []).append({
            "config": name,
            "name": info["name"],
            "description": info["description"],
            "source": info["source"],
            "url": info["url"],
        })
    return jsonify({
        "count": len(DATASETS),
        "groups": grouped,
    })

@app.get("/<category>/<config_name>")
def get_dataset_endpoint(category, config_name):
    if config_name not in DATASETS:
        abort(404, description=f"Unknown dataset: {config_name}")

    info = DATASETS[config_name]
    if info["category"] != category:
        abort(404, description=f"Dataset {config_name} not found in category {category}")

    try:
        df = get_dataset(config_name)
        if df is None:
            abort(404, description=f"Dataset not found: {config_name}")

        return jsonify({
            "source": info["source"],
            "description": info["description"],
            "url": info["url"],
            "data": df.to_dict(orient="records"),
        })
    except Exception as e:
        abort(500, description=f"Failed to load dataset: {str(e)}")


@app.get("/schema/<category>/<config_name>")
def get_dataset_schema(category, config_name):
    schema_path = _SCHEMA_DIR / f"{config_name}.json"
    if not schema_path.exists():
        abort(404, description=f"Schema not found: {config_name}")
    with open(schema_path) as f:
        return jsonify(json_lib.load(f))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
