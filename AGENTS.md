# +254 — Agent Context

> Kenya's data. Open and accessible.
> Lightweight API + data pipeline that extracts, cleans, and serves Kenyan institutional data.

---

## What This Is

+254 is a data platform that scrapes/extracts data from Kenyan institutions (EPRA, Central Bank, IEBC, Tea Board, etc.), cleans and standardizes it, publishes it to HuggingFace Datasets, and serves it through a public FastAPI with zero auth.

Live API: `https://api.plus254.co.ke/v1/`

---

## Tech Stack

- **Python** >= 3.10
- **FastAPI** + Uvicorn (public API)
- **Pandas / NumPy** (data processing)
- **BeautifulSoup / requests / pdfplumber** (scraping & extraction)
- **HuggingFace `datasets` / `huggingface_hub`** (dataset storage & hosting)
- **DuckDB** (local analytics / exploration)
- **YAML** (dataset metadata & configuration)
- **python-dotenv** (env management)
- **Prefect** (workflow orchestration & scheduling)
- **Pandera** (DataFrame schema validation)

---

## Directory Structure

```
plus254/
├── src/plus254/
│   ├── api/                       # FastAPI web service
│   │   ├── main.py                # App factory, exception handlers
│   │   ├── routers/
│   │   │   └── datasets.py        # GET /datasets, /datasets/{name}, /schema, /info
│   │   ├── models.py              # Pydantic response models
│   │   ├── data.py                # HuggingFace Dataset Viewer API client
│   │   ├── config.py              # Loads DATASETS from datasets.yaml
│   │   ├── dependencies.py        # PaginationParams (limit/offset)
│   │   ├── exceptions.py          # APIErrorResponse custom exception
│   │   └── app.py                 # OLD Flask app (legacy, still present)
│   ├── pipeline/                  # ETL pipeline (canonical — replaces collectors/)
│   │   ├── extract/
│   │   │   ├── dynamic/
│   │   │   │   ├── fixed_source/     # CSV/HTML extractors (CBK, EPRA, Tea Board)
│   │   │   │   │   ├── gdp_quarterly.py
│   │   │   │   │   ├── pump_prices.py
│   │   │   │   │   └── ...
│   │   │   │   └── rolling_source/ # PDF extractors (CA, future sources)
│   │   │   │       └── ca/
│   │   │   │           ├── extract.py
│   │   │   │           └── manifest.yaml
│   │   │   └── static/             # One-time extractors (IEBC)
│   │   ├── transform/              # One file per dataset slug
│   │   ├── load/                   # Validate → merge → push to HF
│   │   └── orchestrator/           # Prefect flows, tasks, registry, deploy
│   ├── quality_checks/             # Schema, duplicates, dimensional coverage
│   ├── collectors/                 # LEGACY — per-institution scrapers (deprecated)
│   │   ├── ca/
│   │   ├── central_bank/
│   │   ├── epra/
│   │   ├── iebc/
│   │   ├── kilimo/
│   │   └── teaboard/
│   ├── database/                   # Currently empty (was intended for local DB layer)
│   └── utils/                      # Shared utilities
│       ├── config.py               # Centralized datasets.yaml loader (NEW)
│       ├── extractors/             # csv, html, pdf, manifest
│       ├── loaders/                # huggingface pull/push, merge upsert
│       └── transformers/           # tidy, frame, prune, text
├── src/scripts/                   # Admin / migration scripts
│   ├── docs/
│   └── migrations/
├── data/                          # Local data files / CSVs
├── .env                           # HF_TOKEN, HF_REPO_ID
├── pyproject.toml                 # Package config (setuptools, src layout)
├── Procfile                       # Heroku / container entrypoint
└── README.md
```

---

## Architecture & Data Flow

### ETL Pipeline

1. **Extract** (`src/plus254/pipeline/extract/`) fetches raw data:
   - **Fixed sources**: CSV/HTML tables from institutional websites
   - **Rolling sources**: PDFs parsed via manifest-driven extraction
   - **Static sources**: One-time PDFs or files
2. **Transform** (`src/plus254/pipeline/transform/`) parses, melts, and cleans into canonical format (one file per dataset slug).
3. **Quality Checks** (`src/plus254/quality_checks/`) validates schema (Pandera), checks for duplicates on natural keys, and verifies dimensional coverage.
4. **Load** (`src/plus254/pipeline/load/`) pulls existing data from HuggingFace, upserts on natural keys, pushes merged data back, and bumps `last_updated` in `datasets.yaml`.
5. **Orchestrator** (`src/plus254/pipeline/orchestrator/`) runs the ETL on Prefect Cloud with schedules by frequency (monthly, quarterly, annually).

### API

6. The **FastAPI** (`src/plus254/api/`) does **NOT** store data locally. It fetches slices on-demand from the HuggingFace Dataset Viewer API (`datasets-server.huggingface.co`).
7. API responses are wrapped in a standard metadata envelope with `resultset.count`, `offset`, `limit`.

---

## API Conventions

### Base Path
All routes are under `/v1`.

### Standard Response Shape
```json
{
  "metadata": {
    "resultset": {
      "count": 1000,
      "offset": 0,
      "limit": 100
    }
  },
  "results": [...]
}
```

### Error Format
All errors use `APIErrorResponse` and return:
```json
{
  "error": {
    "code": "not_found",
    "message": "...",
    "link": "https://plus254.co.ke/api-docs/errors#<code>"
  }
}
```

Common codes: `not_found`, `invalid_parameter`, `upstream_error`, `gateway_timeout`, `internal_error`.

### Pagination
`limit` (1–100, default 100) and `offset` (>= 0, default 0) on all list endpoints.

### Dataset Discovery
`GET /v1/datasets` lists all datasets with metadata. Category filter supported via query param.

---

## Key Environment Variables

| Variable | Purpose |
|----------|---------|
| `HF_REPO_ID` | HuggingFace dataset repo (e.g. `muhammadomarmuhdhar/plus254`) |
| `HF_TOKEN` | HuggingFace write token (for uploads; read API is public) |

Stored in `.env` (loaded by `config.py` via `python-dotenv`).

---

## Coding Style & Patterns

- **Modern Python**: type hints, `| None` unions, f-strings.
- **src layout**: package lives under `src/plus254/`.
- **Pydantic models** for all API responses.
- **YAML-driven metadata**: never hardcode dataset lists; read from `datasets.yaml`.
- **Logging**: use `logging.getLogger(__name__)` in utilities; include structured info (rows, columns, bytes).
- **Resilient scraping**: handle mismatched table columns, normalize row lengths.
- **No local DB for API**: API is stateless; data lives on HF.
- **Error links**: every API error includes a `link` to `plus254.co.ke/api-docs/errors#<code>`.

---

## Running / Deployment

### Pipeline

```bash
# Run one dataset manually (dry run)
python -c "from plus254.pipeline.orchestrator.flows import fixed_source_flow; fixed_source_flow(frequency='monthly', dry_run=True)"

# Deploy to Prefect Cloud
python src/plus254/pipeline/orchestrator/deploy.py

# Start local worker for scheduled runs
prefect worker start -p plus254-pool
```

### API — Local dev
```bash
# Install in editable mode
pip install -e ".[dev]"

# Run API
uvicorn plus254.api.main:app --reload --port 8000
# or
python -m plus254.api.main
```

### API — Production
```bash
# Heroku / container
web: uvicorn plus254.api.main:app --host 0.0.0.0 --port ${PORT:-8000}
```

---

## Dataset Catalog (Auto-discovered)

Datasets are loaded at startup from `src/plus254/datasets.yaml`. Each entry contains name, category, source, description, URL, columns, natural keys, and update frequency.

Currently includes:

- **EPRA** — Fuel Pump Prices (`pump_prices`)
- **Central Bank** — GDP, forex, monetary survey, BOP, fiscal, public debt, trade, principal exports
- **Tea Board** — Mombasa Tea Auction
- **IEBC** — Registered Voters per Polling Station
- **CA (Communications Authority)** — Mobile traffic, broadband, internet subscriptions, domain registrations, cybersecurity

To add a new dataset:
1. Create an extractor under `src/plus254/pipeline/extract/<source_type>/`.
2. Write a transform under `src/plus254/pipeline/transform/{slug}.py`.
3. Add the slug to `src/plus254/datasets.yaml` with metadata and natural keys.
4. Upload processed data to the HuggingFace repo.
5. The API will auto-pick it up on restart.

---

## Notes for Agents

- **Legacy Flask app exists**: `src/plus254/api/app.py` is an old Flask version. The canonical app is `src/plus254/api/main.py` (FastAPI). Do not modify Flask app unless explicitly asked.
- **Legacy collectors exist**: `src/plus254/collectors/` is the old scraper architecture. The canonical pipeline is `src/plus254/pipeline/`.
- **Pipeline phases**: extract → transform → quality checks → load. Do not skip quality checks.
- **Centralized config**: `plus254.utils.config.load_dataset_spec()` — use this instead of inline YAML parsing.
- **Prefect orchestration**: flows are in `pipeline/orchestrator/flows.py`, deployments via `deploy.py`.
- **Rolling sources**: one extractor produces multiple datasets (e.g. CA PDF → 11 slugs). The orchestrator filters records by the `dataset` field before passing to transforms.
- **Transform outputs**: some transforms return `dict[str, DataFrame]` (e.g. `fiscal_revenue` → 3 datasets, `roaming_traffic` → 2 datasets). The load phase handles this via `_dispatch_load()`.
- **No local DB for API**: the API is entirely HF-backed. The `database/` directory is currently unused.
- **Schema JSON files**: live in `src/plus254/api/schema/` (e.g. `pump_prices.json`). These are served by `GET /v1/datasets/{name}/schema`.
- **HF_TOKEN is sensitive**: it is in `.env` — do not commit or expose it.
- **Pagination is remote**: `get_dataset_slice()` calls HuggingFace's API with `offset` and `length`; we do not paginate in-memory.
- **Datasets are keyed by `config_name`**: the YAML top-level key becomes the API identifier.
