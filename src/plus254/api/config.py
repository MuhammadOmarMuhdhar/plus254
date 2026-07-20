from dotenv import load_dotenv
import os
from pathlib import Path

from plus254.utils.config import load_datasets as _load_all

load_dotenv()

HF_REPO_ID = os.environ.get("HF_REPO_ID")


def _load_datasets():
    datasets_yaml = Path(__file__).resolve().parent.parent / "datasets.yaml"
    raw = _load_all(datasets_yaml)
    return {
        slug: {k: v for k, v in info.items() if k != "columns"}
        for slug, info in raw.items()
    }


DATASETS = _load_datasets()
