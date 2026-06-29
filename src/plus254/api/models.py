from pydantic import BaseModel

class ResultSetMetadata(BaseModel):
    """Metadata about the result set."""
    count: int
    offset: int
    limit: int


class MetadataWrapper(BaseModel):
    """Wraps resultset to allow future expansion (filters, query info, etc.)."""
    resultset: ResultSetMetadata

class DatasetInfo(BaseModel):
    """A single dataset in the list view."""
    config: str
    name: str
    category: str
    description: str
    source: str
    url: str
    last_updated: str | None = None
    update_frequency: str | None = None

class DatasetListResponse(BaseModel):
    """Response shape for GET /datasets"""
    metadata: MetadataWrapper
    results: list[DatasetInfo]


class DatasetDataResponse(BaseModel):
    """Response shape for GET /datasets/{config_name}"""
    metadata: MetadataWrapper
    category: str
    source: str
    description: str
    url: str
    results: list[dict]