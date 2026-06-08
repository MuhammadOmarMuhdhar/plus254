import os
import time
import logging
import pandas as pd
from datasets import Dataset, load_dataset
from huggingface_hub import HfApi
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def save_to_hf(df, repo_id=None, token=None, config_name="default", save_csv=False, csv_filename="data.csv", overwrite=False):
    repo_id = repo_id or os.environ.get("HF_REPO_ID")
    token = token or os.environ.get("HF_TOKEN")

    if not repo_id:
        raise ValueError("HF_REPO_ID is not set")

    if overwrite:
        logger.info(f"Overwriting config '{config_name}' (skip merge)")
        combined = df
    else:
        try:
            logger.info(f"Loading existing config '{config_name}' from HuggingFace")
            existing = load_dataset(repo_id, config_name, token=token, split="train")
            existing_df = existing.to_pandas()
            logger.info(f"Existing dataset: {len(existing_df)} rows")

            combined = pd.concat([existing_df, df], ignore_index=True)
            logger.info(f"Combined: {len(combined)} rows ({len(combined) - len(existing_df)} new)")
        except Exception:
            logger.warning("Could not load existing dataset (first run?)")
            combined = df

    logger.info(f"Pushing config '{config_name}' to HuggingFace")
    start = time.time()
    Dataset.from_pandas(combined).push_to_hub(repo_id, config_name=config_name, token=token, private=False)
    logger.info(f"Pushed in {time.time() - start:.1f}s")

    if save_csv:
        csv_path = f"{config_name}/{csv_filename}"
        logger.info(f"Uploading CSV ({csv_path})")
        csv_start = time.time()
        HfApi().upload_file(
            path_or_fileobj=combined.to_csv(index=False).encode(),
            path_in_repo=csv_path,
            repo_id=repo_id,
            repo_type="dataset",
            token=token,
        )
        logger.info(f"CSV uploaded in {time.time() - csv_start:.1f}s")
