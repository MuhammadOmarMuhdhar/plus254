import os
import requests
from .exceptions import APIErrorResponse

HF_REPO_ID = os.environ.get("HF_REPO_ID")
HF_TOKEN = os.environ.get("HF_TOKEN")


def get_dataset_slice(config_name: str, limit: int, offset: int):
    """
    Fetch a slice of rows from the HuggingFace Dataset Viewer API.
    True remote pagination — no full download to our server.
    """
    url = "https://datasets-server.huggingface.co/rows"
    headers = {}
    if HF_TOKEN:
        headers["Authorization"] = f"Bearer {HF_TOKEN}"

    params = {
        "dataset": HF_REPO_ID,
        "config": config_name,
        "split": "train",
        "offset": offset,
        "length": limit,
    }

    try:
        r = requests.get(url, headers=headers, params=params, timeout=30)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        if status == 404:
            raise APIErrorResponse(
                status_code=404,
                code="not_found",
                message=f"Dataset '{config_name}' not found on HuggingFace.",
                link="https://plus254.co.ke/api-docs/errors#not_found",
            )
        elif status == 422:
            raise APIErrorResponse(
                status_code=400,
                code="invalid_parameter",
                message="Invalid pagination parameters. Offset/length may be out of range.",
                link="https://plus254.co.ke/api-docs/errors#invalid_parameter",
            )
        else:
            raise APIErrorResponse(
                status_code=502,
                code="upstream_error",
                message="Data source temporarily unavailable. Please retry.",
                link="https://plus254.co.ke/api-docs/errors#upstream_error",
            )
    except requests.exceptions.Timeout:
        raise APIErrorResponse(
            status_code=504,
            code="gateway_timeout",
            message="Data source took too long to respond. Please retry.",
            link="https://plus254.co.ke/api-docs/errors#upstream_error",
        )
    except requests.exceptions.RequestException:
        raise APIErrorResponse(
            status_code=502,
            code="upstream_error",
            message="Failed to reach data source. Please retry.",
            link="https://plus254.co.ke/api-docs/errors#upstream_error",
        )

    data = r.json()
    rows = [item["row"] for item in data.get("rows", [])]
    total = data.get("num_rows_total", len(rows))

    return rows, total
