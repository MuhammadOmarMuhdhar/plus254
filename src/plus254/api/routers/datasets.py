from fastapi import APIRouter, Depends
import difflib
import json as json_lib
from pathlib import Path
from ..config import DATASETS
from ..exceptions import APIErrorResponse
from ..models import (
    DatasetInfo,
    DatasetListResponse,
    DatasetDataResponse,
    MetadataWrapper,
    ResultSetMetadata,
)
from ..data import get_dataset_slice
from ..dependencies import PaginationParams


router = APIRouter()


def validate_config(config_name: str):
    """Validates that the config_name exists in DATASETS. Raises APIErrorResponse if not found."""
    if config_name not in DATASETS:
        close = difflib.get_close_matches(config_name, DATASETS.keys(), n=1, cutoff=0.6)
        suggestion = f" Did you mean '{close[0]}'?" if close else ""
        raise APIErrorResponse(
            status_code=404,
            code="not_found",
            message=f"Dataset '{config_name}' not found.{suggestion} "
                    f"See https://plus254.co.ke/datasets for available datasets.",
            link="https://plus254.co.ke/api-docs/errors#not_found",
        )
    return DATASETS[config_name]


@router.get("/datasets", response_model=DatasetListResponse)
def list_datasets(
    pagination: PaginationParams = Depends(),
    category: str | None = None,
):
    all_items = []
    for config_name, info in DATASETS.items():
        if category and info["category"] != category:
            continue
        all_items.append(
            DatasetInfo(
                config=config_name,
                name=info["name"],
                description=info["description"],
                source=info["source"],
                url=info["url"],
                category=info["category"],
                last_updated=info.get("last_updated"),
                update_frequency=info.get("update_frequency"),
            )
        )

    total = len(all_items)
    paginated = all_items[pagination.offset : pagination.offset + pagination.limit]

    return DatasetListResponse(
        metadata=MetadataWrapper(
            resultset=ResultSetMetadata(
                count=total,
                offset=pagination.offset,
                limit=pagination.limit,
            )
        ),
        results=paginated,
    )


@router.get("/datasets/{config_name}", response_model=DatasetDataResponse)
def get_dataset_data(
    config_name: str,
    info: dict = Depends(validate_config),
    pagination: PaginationParams = Depends(),
):
    rows, total = get_dataset_slice(
        config_name,
        limit=pagination.limit,
        offset=pagination.offset,
    )

    return DatasetDataResponse(
        metadata=MetadataWrapper(
            resultset=ResultSetMetadata(
                count=total,
                offset=pagination.offset,
                limit=pagination.limit,
            )
        ),
        category=info["category"],
        source=info["source"],
        description=info["description"],
        url=info["url"],
        results=rows,
    )


@router.get("/datasets/{config_name}/schema")
def get_dataset_schema(config_name: str, info: dict = Depends(validate_config)):
    schema_dir = Path(__file__).resolve().parent.parent / "schema"
    schema_path = schema_dir / f"{config_name}.json"

    if not schema_path.exists():
        raise APIErrorResponse(
            status_code=404,
            code="not_found",
            message=f"Schema not found for dataset '{config_name}'.",
            link="https://plus254.co.ke/api-docs/errors#not_found",
        )

    with open(schema_path) as f:
        return json_lib.load(f)


@router.get("/datasets/{config_name}/info", response_model=DatasetInfo)
def get_dataset_info(config_name: str, info: dict = Depends(validate_config)):
    return DatasetInfo(
        config=config_name,
        name=info["name"],
        category=info["category"],
        description=info["description"],
        source=info["source"],
        url=info["url"],
        last_updated=info.get("last_updated"),
        update_frequency=info.get("update_frequency"),
    )
