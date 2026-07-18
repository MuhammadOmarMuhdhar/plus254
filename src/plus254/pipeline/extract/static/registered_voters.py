import logging
from pathlib import Path
import pandas as pd
from plus254.utils.config import load_dataset_spec
from plus254.utils.extractors import pdf

logger = logging.getLogger(__name__)

def extract() -> pd.DataFrame:
    slug = Path(__file__).stem
    spec = load_dataset_spec("src/plus254/datasets.yaml", slug)
    return pdf.get_table(spec["url"], pdf_name="Registered Voters per Polling Station")
