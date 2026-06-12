from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv()

HF_REPO_ID = os.environ.get("HF_REPO_ID")


def _load_datasets():
    import yaml

    scrapers_dir = Path(__file__).resolve().parent.parent / "scrapers"
    datasets = {}
    for yaml_path in sorted(scrapers_dir.glob("*/datasets.yaml")):
        with open(yaml_path) as f:
            raw = yaml.safe_load(f)
        for key, info in raw.items():
            datasets[key] = {k: v for k, v in info.items() if k != "columns"}
    return datasets


DATASETS = _load_datasets()
