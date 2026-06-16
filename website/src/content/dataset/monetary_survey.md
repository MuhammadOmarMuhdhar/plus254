---
title: "Depository Corporation Survey"
description: "Monetary aggregates from the Depository Corporation Survey"
source: "Central Bank of Kenya"
endpoint: "GET /economy/monetary_survey"
rows: 12325
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/monetary_and_finance_statistics/274043565_Depository%20Corporation%20Survey%20-%20CSV.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| section | object | Sub-survey section (Central Bank of Kenya, Other Depository Corporation Survey, Depository Corporation Survey) | No | 0 | 3 |
| metric | object | Monetary indicator name (e.g., Excess reserves, Required reserves, Broad Money M3) | No | 0 | 33 |
| year | int64 | Calendar year | No | 0 | 13 |
| month | object | Calendar month name | No | 0 | 12 |
| value | float64 | Monetary value in KES millions | No | 0 | 11065 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 12325 | 2019.77 | 3.47 | 2014.00 | 2017.00 | 2020.00 | 2023.00 | 2026.00 |
| value | 12325 | 521115.29 | 1.258e+06 | -2.445e+06 | 0.05 | 5796.00 | 323274.30 | 8.002e+06 |

## Sample Data

| section | metric | year | month | value |
|---|---|---|---|---|
| central bank of kenya |     excess reserves | 2014 | january | 4792.0 |
| central bank of kenya |     required reserves | 2014 | january | 100001.0 |
| central bank of kenya | banks reserves at cbk | 2014 | january | 104793.0 |
| central bank of kenya | county government (net) | 2014 | january | 0.0 |
| central bank of kenya | credit to other depository corporations | 2014 | january | 4014.0 |
