class APIErrorResponse(Exception):
    """Custom exception class for API error responses."""
    def __init__(
            self, 
            status_code: int, 
            code: str,
            message: str,
            link: str = ""):
        
        self.status_code = status_code
        self.code = code
        self.message = message
        self.link = link
