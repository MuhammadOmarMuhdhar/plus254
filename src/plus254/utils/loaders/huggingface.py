"""HuggingFace backend — pull/push contract for the load phase."""

import os
import time
import logging

import pandas as pd
from datasets import Dataset, load_dataset
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def pull(name: str, repo_id: str | None = None, token: str | None = None) -> pd.DataFrame:
    """Pull existing dataset from HuggingFace.
    """
    repo_id = repo_id or os.environ.get("HF_REPO_ID")
    token = token or os.environ.get("HF_TOKEN")

    if not repo_id:
        raise ValueError("HF_REPO_ID is not set")

    try:
        logger.info(f"Pulling existing config '{name}' from HuggingFace")
        ds = load_dataset(repo_id, name, token=token, split="train")
        df = ds.to_pandas()
        logger.info(f"Existing dataset: {len(df)} rows")
        return df
    except Exception:
        logger.warning(f"Could not load existing dataset '{name}' (first run?)")
        return pd.DataFrame()


def push(name: str, df: pd.DataFrame, repo_id: str | None = None, token: str | None = None):
    """Push a DataFrame to HuggingFace as a dataset config."""
    repo_id = repo_id or os.environ.get("HF_REPO_ID")
    token = token or os.environ.get("HF_TOKEN")

    if not repo_id:
        raise ValueError("HF_REPO_ID is not set")

    logger.info(f"Pushing config '{name}' to HuggingFace ({len(df)} rows)")
    start = time.time()
    Dataset.from_pandas(df).push_to_hub(
        repo_id, config_name=name, token=token, private=False
    )
    logger.info(f"Pushed in {time.time() - start:.1f}s")
