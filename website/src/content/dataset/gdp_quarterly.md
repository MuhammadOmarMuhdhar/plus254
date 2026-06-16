---
title: "Quarterly GDP"
description: "Quarterly GDP estimates by sector"
source: "Central Bank of Kenya"
endpoint: "GET /economy/gdp_quarterly"
rows: 2725
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/national_accounts_statistics/1084903161_Quarterly%20GDP.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 17 |
| quarter | object | Calendar quarter (Q1, Q2, Q3, Q4) | No | 0 | 4 |
| metric | object | Economic sector or activity (e.g., Agriculture, Manufacturing, Construction, Total GDP) | No | 0 | 22 |
| value | float64 | GDP value in KES millions | No | 0 | 2318 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 2725 | 2017.23 | 4.77 | 2009.00 | 2013.00 | 2017.00 | 2021.00 | 2025.00 |
| value | 2725 | 197844.95 | 525256.08 | -86324.78 | 4.92 | 2023.00 | 127815.00 | 2.948e+06 |

## Sample Data

| year | quarter | metric | value |
|---|---|---|---|
| 2009 | q1 | accommodation & restaurant | 20371.0 |
| 2009 | q1 | agriculture | 312740.0 |
| 2009 | q1 | all industries at basic prices | 1231237.0 |
| 2009 | q1 | construction | 50218.0 |
| 2009 | q1 | education | 61140.0 |
