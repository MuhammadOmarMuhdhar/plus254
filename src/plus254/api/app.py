from flask import Flask, jsonify, abort
from .config import DATASETS
from .data import get_dataset

app = Flask(__name__)

@app.get("/")
def list_datasets():
    grouped = {}
    for name, info in DATASETS.items():
        slug = info["slug"]
        grouped.setdefault(slug, []).append({
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

@app.get("/<slug>/<config_name>")
def get_dataset_endpoint(slug, config_name):
    if config_name not in DATASETS:
        abort(404, description=f"Unknown dataset: {config_name}")

    info = DATASETS[config_name]
    if info["slug"] != slug:
        abort(404, description=f"Dataset {config_name} not found in group {slug}")

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


if __name__ == "__main__":
    app.run(debug=True, port=5000)
