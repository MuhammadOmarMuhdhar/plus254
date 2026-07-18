# +254

Kenya's data. Open and accessible.

Data about Kenya is buried in PDFs, messy Excel files, poorly documented, and hard to access. Getting it ready for analysis or development is a headache. +254 extracts data from Kenyan institutions, cleans and processes it, and serves it through a plug-and-play API.

## Quick start

All endpoints are open and require no authentication.

```bash
curl "https://api.plus254.co.ke/v1/datasets"
```

```python
import requests
response = requests.get("https://api.plus254.co.ke/v1/datasets")
print(response.json())
```

```javascript
fetch("https://api.plus254.co.ke/v1/datasets")
  .then(r => r.json())
  .then(console.log);
```

That gives you the full catalog. Now here's how to fetch actual data, get metadata, or inspect a dataset's schema:

| Endpoint | Description |
|---|---|
| `GET /v1/datasets` | List all available datasets |
| `GET /v1/datasets/{name}` | Fetch dataset records |
| `GET /v1/datasets/{name}/info` | Get dataset metadata |
| `GET /v1/datasets/{name}/schema` | Get dataset column schema |

All endpoints accept `limit` and `offset` for pagination. Responses include a `total` field indicating the full number of records matching your query.

Browse available datasets and the full API reference at [plus254.co.ke](https://plus254.co.ke).
