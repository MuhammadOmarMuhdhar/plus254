# +254 Data Pipeline

> Core data engineering layer for extract, validate, transform, and load.

## Current Directory Structure

```
pipeline/
├── __init__.py
├── README.md              # This file
├── contracts.py           # Phase 1 
├── merge.py               # Phase 2 
├── hf.py                  # Phase 2 
├── core.py                # Phase 3 - to be done
└── quality.py             # Phase 4 - to be done
```

---

## Phase 1: Data Contracts COMPLETE

**Goal:** Enforce `datasets.yaml` schemas programmatically so bad data never reaches database.

**What was built:**
- `pipeline/contracts.py` with `validate(df, config_name, yaml_path)`
- Maps YAML types (`integer`, `float`, `string`, `date`, `datetime`) to Pandera `DataFrameSchema`
- Enforces exact column match (`strict=True`)
- `natural_keys` columns are non-nullable
- Raises `ContractViolation` with all failures if anything is wrong
- Wired into `pipeline/hf.py` — validation runs before every merge/upload

**Key function:**
```python
from plus254.pipeline.contracts import validate, ContractViolation

validated_df = validate(df, "pump_prices", "src/plus254/collectors/epra/datasets.yaml")
```

---

## Phase 2: Idempotent Upserts - COMPLETE

**Goal:** Re-running a collector must not create duplicates.

**What was built:**
- `pipeline/merge.py` with `upsert(existing, new, natural_keys)`
- Uses pandas anti-join filter 
- `pipeline/hf.py` refactored:
  - `overwrite` parameter replaced with `strategy` (`"upsert"` | `"replace"`)
  - Reads `natural_keys` automatically from `yaml_path`
  - Falls back to `pd.concat` with warning if no natural_keys found
- All collectors updated to `strategy="upsert"`
- `utils/hf.py` deleted — `pipeline/hf.py` is the canonical location

**Key function:**
```python
from plus254.pipeline.merge import upsert

combined = upsert(existing_df, new_df, natural_keys=["year", "quarter", "operator", "item"])
```

---

## Phase 3: Pipeline Orchestration -  PENDING

**Goal:** Abstract `fetch → validate → transform → load` into a reusable class.

**What it will do:**
- `Pipeline` dataclass with `name`, `extract`, `transform`, `yaml_path`
- `Pipeline.run()` executes the full flow:
  1. Standardized logging + timing
  2. `extract()` → raw DataFrame
  3. `transform()` → cleaned DataFrame
  4. `validate()` → schema validation (Phase 1)
  5. `save_to_hf()` → upsert + upload (Phase 2)
  6. Log completion
- Removes duplicated boilerplate from every collector's `main.py`:
  - `logging.basicConfig`
  - `load_dotenv`
  - `try/except` + timing

**Implementation steps:**
1. Build `pipeline/core.py` with `Pipeline` class
2. Refactor EPRA as proof of concept
3. Roll out to other simple collectors
4. Remove duplicated boilerplate

---

## Phase 4: Data Quality Checks - PENDING

**Goal:** Catch data drift, anomalies, and regressions automatically.

**What it will do:**
- `pipeline/quality.py` with check functions:
  - `check_freshness(df, config_name)` - latest row within expected recency
  - `check_ranges(df, config_name)` - values within historical percentiles
  - `check_completeness(df, config_name)` — null rate per column
  - `check_totals(df, config_name)` - category sums match declared totals
- Wire into `Pipeline.run()` as a gate after `transform()`, before `load()`
- Raise `QualityError` if any check fails

**Tests to add:**
- `tests/unit/test_contracts.py` — bad DataFrames → assert `ContractViolation`
- `tests/unit/test_merge.py` — overlapping DataFrames → assert no duplicates
- `tests/unit/test_quality.py` — stale dates / out-of-range values → assert failure

---