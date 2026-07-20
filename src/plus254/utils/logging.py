"""Centralized logging configuration for +254.

Call ``setup_logging()`` once at every entry point
(seed.py, tasks.py, deploy.py, etc.) before any other imports.
"""

import logging

NOISY_LOGGERS = [
    "datasets",
    "datasets.packaged_modules.cache.cache",
    "httpx",
    "httpcore",
    "huggingface_hub",
    "urllib3",
    "urllib3.connectionpool",
    "fsspec",
    "filelock",
    "pdfminer",
]

_FORMAT = "%(asctime)s | %(levelname)-7s | %(name)-36s | %(message)s"
_DATEFMT = "%Y-%m-%d %H:%M:%S"


def setup_logging(level: int = logging.INFO) -> None:
    """Configure root logger with uniform format and suppress third-party noise."""
    logging.basicConfig(level=level, format=_FORMAT, datefmt=_DATEFMT)
    for name in NOISY_LOGGERS:
        logging.getLogger(name).setLevel(logging.ERROR)
