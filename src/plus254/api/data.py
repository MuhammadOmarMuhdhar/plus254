from datasets import load_dataset
from .config import HF_REPO_ID, DATASETS

def get_dataset(config_name):
    if config_name not in DATASETS:
        return None
    ds = load_dataset(HF_REPO_ID, config_name, split="train")
    return ds.to_pandas()