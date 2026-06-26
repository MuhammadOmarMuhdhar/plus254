from fastapi import Query

class PaginationParams:
    """Class to handle pagination parameters for API endpoints."""
    def __init__(
        self,
        limit: int = Query(100, ge =1, le=100, 
                           description="Maximum number of records to return"),
        offset: int = Query(0, ge=0, 
                            description="Number of records to skip")
    ): 
        self.limit = limit
        self.offset = offset
