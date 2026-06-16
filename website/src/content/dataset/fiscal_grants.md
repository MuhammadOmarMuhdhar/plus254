---
title: "Government Grants"
description: "Monthly government grants received"
source: "Central Bank of Kenya"
endpoint: "GET /economy/fiscal_grants"
rows: 893
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| fiscal_year | int64 | Fiscal year (e.g., 1999 means FY 1999/2000) | No | 0 | 28 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Grant type (programme grants, project grants, total grants) | No | 0 | 3 |
| value | float64 | Grants in KES millions (comma-formatted number) | No | 0 | 374 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| fiscal_year | 893 | 2012.63 | 7.73 | 1999.00 | 2006.00 | 2012.00 | 2020.00 | 2026.00 |
| value | 893 | 6818.60 | 8279.77 | 0.00 | 0.00 | 3890.00 | 11204.86 | 76373.33 |

## Sample Data

| fiscal_year | month | metric | value |
|---|---|---|---|
| 1999 | september | programme grants | 6.0 |
| 1999 | december | programme grants | 329.0 |
| 2000 | march | programme grants | 344.0 |
| 2000 | june | programme grants | 0.0 |
| 2000 | july | programme grants | 0.0 |
