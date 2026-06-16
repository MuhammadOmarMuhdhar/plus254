---
title: "Principal Exports — Volume, Value, Unit Prices"
description: "Monthly volume, value, and average unit prices of principal exports (coffee, tea, horticulture)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/principal_exports"
rows: 2988
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/766913717_Principal%20Exports_Volume,%20Value%20and%20Unit%20Prices.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 29 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Commodity and measure (coffee volume, coffee value, coffee average, tea volume, tea value, tea average, horticulture volume, horticulture value, horticulture average) | No | 0 | 9 |
| value | float64 | Volume in Kgs, value in KES millions, or average price in KES per kg (comma-formatted number; see Metric for unit) | No | 0 | 2985 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 2988 | 2011.92 | 8.00 | 1998.00 | 2005.00 | 2012.00 | 2019.00 | 2026.00 |
| value | 2988 | 99304.28 | 157096.24 | 130.21 | 4437.56 | 21906.24 | 162741.88 | 1.085e+06 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | august | coffee volume | 2759.82 |
| 1998 | september | coffee volume | 3243.7 |
| 1998 | october | coffee volume | 4158.57 |
| 1998 | november | coffee volume | 3958.47 |
| 1998 | december | coffee volume | 3565.01 |
