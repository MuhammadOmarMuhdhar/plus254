from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

HF_REPO_ID = os.environ.get("HF_REPO_ID")

_yaml_path = Path(__file__).resolve().parent / "datasets.yaml"

def _load_datasets():
    import yaml
    with open(_yaml_path) as f:
        raw = yaml.safe_load(f)
    datasets = {}
    for key, info in raw.items():
        datasets[key] = {k: v for k, v in info.items() if k != "columns"}
    return datasets

DATASETS = _load_datasets()