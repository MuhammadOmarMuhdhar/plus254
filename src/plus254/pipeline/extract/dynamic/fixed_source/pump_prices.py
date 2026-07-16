import logging
from pathlib import Path
import pandas as pd
import yaml
from plus254.utils.extractors import html

logger = logging.getLogger(__name__)

def extract(datasets: dict | None = None) -> pd.DataFrame:
    slug = Path(__file__).stem
    if datasets is None:
        with open('src/plus254/datasets.yaml', 'r') as f:
            datasets = yaml.safe_load(f)
    url = datasets[slug]['url']
    return html._get_table(url)
