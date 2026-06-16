---
title: "Government Revenue"
description: "Monthly government revenue breakdown"
source: "Central Bank of Kenya"
endpoint: "GET /economy/fiscal_revenue"
rows: 2326
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| fiscal_year | int64 | Fiscal year (e.g., 1999 means FY 1999/2000) | No | 0 | 28 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Revenue category (e.g., import duty, excise duty, income tax, vat, total revenue) | No | 0 | 8 |
| value | float64 | Revenue in KES millions (comma-formatted number) | No | 0 | 2323 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| fiscal_year | 2326 | 2013.13 | 7.57 | 1999.00 | 2026.00 |
| value | 2326 | 215787.29 | 355462.34 | 987.00 | 2.957e+06 |

## Sample Data

| fiscal_year | month | metric | value |
|---|---|---|---|
| 1999 | September | import duty | 7157.0 |
| 1999 | December | import duty | 13912.0 |
| 2000 | March | import duty | 21407.0 |
| 2000 | June | import duty | 28605.0 |
| 2000 | July | import duty | 2813.0 |
