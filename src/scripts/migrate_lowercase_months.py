import os
import sys
from pathlib import Path

import pandas as pd
from datasets import Dataset, load_dataset
from dotenv import load_dotenv

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from plus254.api.config import DATASETS

load_dotenv()

REPO_ID = os.environ["HF_REPO_ID"]
TOKEN = os.environ["HF_TOKEN"]


def run():
    for config_name in sorted(DATASETS):
        print(f"Loading: {config_name} ...")
        ds = load_dataset(REPO_ID, config_name, split="train", token=TOKEN)
        df = ds.to_pandas()

        if "month" not in df.columns:
            print(f"  No month column, skipping")
            continue

        sample = df["month"].dropna().iloc[0] if not df["month"].dropna().empty else ""
        if sample == sample.lower():
            print(f"  Already lowercase ({sample}), skipping")
            continue

        print(f"  Lowercasing {len(df)} rows...")
        df["month"] = df["month"].str.lower()

        Dataset.from_pandas(df).push_to_hub(
            REPO_ID, config_name=config_name, token=TOKEN, private=False
        )
        print(f"  Pushed")

    print("\nDone.")


if __name__ == "__main__":
    run()
