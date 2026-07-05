import os
import time
import logging
from datetime import datetime
from pathlib import Path

import yaml
import pandas as pd
from datasets import Dataset, load_dataset
from huggingface_hub import HfApi
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


def save_to_hf(df, repo_id=None, token=None, config_name="default",
               strategy="upsert", save_csv=False, csv_filename="data.csv",
               yaml_path=None):
    """
    Save a DataFrame to HuggingFace Datasets.

    Parameters
    ----------
    df : pd.DataFrame
        The data to save.
    repo_id, token : str, optional
        HF repo and token (falls back to env vars).
    config_name : str
        Dataset config / subset name.
    strategy : {"upsert", "replace"}
        - "upsert" (default): merge into existing data by natural_keys.
        - "replace": overwrite the entire config.
    save_csv : bool
        Also upload a CSV copy to the repo.
    csv_filename : str
        Name of the CSV file inside the config folder.
    yaml_path : Path or str, optional
        Path to the collector's datasets.yaml. Used to read natural_keys
        and update the last_updated timestamp.
    """
    repo_id = repo_id or os.environ.get("HF_REPO_ID")
    token = token or os.environ.get("HF_TOKEN")

    if not repo_id:
        raise ValueError("HF_REPO_ID is not set")

    # Validate against datasets.yaml contract before merge/upload
    if yaml_path:
        from plus254.pipeline.contracts import validate
        df = validate(df, config_name, yaml_path)

    if strategy == "replace":
        logger.info(f"Replacing config '{config_name}'")
        combined = df
    elif strategy == "upsert":
        try:
            logger.info(f"Loading existing config '{config_name}' from HuggingFace")
            existing = load_dataset(repo_id, config_name, token=token, split="train")
            existing_df = existing.to_pandas()
            logger.info(f"Existing dataset: {len(existing_df)} rows")
        except Exception:
            logger.warning("Could not load existing dataset (first run?)")
            existing_df = pd.DataFrame()

        natural_keys = None
        if yaml_path:
            yaml_path_obj = Path(yaml_path)
            if yaml_path_obj.exists():
                with open(yaml_path_obj) as f:
                    raw = yaml.safe_load(f)
                spec = raw.get(config_name, {}) if raw else {}
                natural_keys = spec.get("natural_keys")

        if existing_df.empty:
            combined = df
        elif not natural_keys:
            logger.warning(
                f"No natural_keys found for '{config_name}' — falling back to append"
            )
            combined = pd.concat([existing_df, df], ignore_index=True)
        else:
            from plus254.pipeline.merge import upsert
            combined = upsert(existing_df, df, natural_keys=natural_keys)
    else:
        raise ValueError(f"Unknown strategy: {strategy!r}. Use 'upsert' or 'replace'.")

    logger.info(f"Pushing config '{config_name}' to HuggingFace ({len(combined)} rows)")
    start = time.time()
    Dataset.from_pandas(combined).push_to_hub(
        repo_id, config_name=config_name, token=token, private=False
    )
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

    if yaml_path:
        yaml_path_obj = Path(yaml_path)
        if yaml_path_obj.exists():
            now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            with open(yaml_path_obj) as f:
                raw = yaml.safe_load(f)
            if raw and config_name in raw:
                raw[config_name]["last_updated"] = now
                with open(yaml_path_obj, "w") as f:
                    yaml.dump(raw, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
                logger.info(f"Updated last_updated in {yaml_path_obj} for '{config_name}'")
