import logging
from pathlib import Path
from plus254.utils.extractors import manifest

logger = logging.getLogger(__name__)


def extract(slugs=None):
    return manifest.extract_from_manifest(
        manifest_path=Path(__file__).parent / "manifest.yaml",
        base_url="https://www.ca.go.ke/statistics",
        slugs=slugs,
    )