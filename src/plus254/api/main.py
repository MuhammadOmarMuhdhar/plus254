from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from .exceptions import APIErrorResponse
from .routers import datasets

app = FastAPI(title="Plus254 API", version="1.0.0")

@app.exception_handler(APIErrorResponse)
def handle_api_error(request, exc: APIErrorResponse):
    """Handles APIErrorResponse exceptions and returns a structured JSON response."""
    from fastapi.responses import JSONResponse
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": exc.code,
                "message": exc.message,
                "link": exc.link,
            }
        },
    )

@app.exception_handler(RequestValidationError)
def handle_validation_error(request, exc: RequestValidationError):
    # Build a custom message from each validation error
    parts = []
    for err in exc.errors():
        loc = ".".join(str(x) for x in err["loc"])
        msg = err["msg"]
        parts.append(f"Parameter '{loc}' is invalid: {msg}")

    message = "; ".join(parts) if parts else "Invalid request parameters."

    return JSONResponse(
        status_code=422,
        content={
            "error": {
                "code": "invalid_parameter",
                "message": message,
                "link": "https://plus254.co.ke/api-docs/errors#invalid_parameter",
            }
        },
    )

@app.exception_handler(StarletteHTTPException)
def handle_http_exception(request, exc: StarletteHTTPException):
    code = "not_found" if exc.status_code == 404 else "invalid_parameter"
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "code": code,
                "message": str(exc.detail),
                "link": f"https://plus254.co.ke/api-docs/errors#{code}",
            }
        },
    )

@app.exception_handler(Exception)
def handle_generic_exception(request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={
            "error": {
                "code": "internal_error",
                "message": "An unexpected error occurred. Please retry.",
                "link": "https://plus254.co.ke/api-docs/errors#internal_error",
            }
        },
    )


@app.get("/v1/health")
def health():
    return {"status": "ok"}

app.include_router(datasets.router, prefix="/v1")