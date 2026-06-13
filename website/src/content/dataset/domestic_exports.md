---
title: "Value of Selected Domestic Exports"
description: "Monthly value of selected domestic export commodities"
source: "Central Bank of Kenya"
endpoint: "GET /centralbank/domestic_exports"
rows: 2987
category: "centralbank"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1306010805_Value%20of%20Selected%20Domestic%20Exports%20-%20Selected%20Comms.csv"
---

Monthly value of selected domestic export commodities

- **Source:** Central Bank of Kenya
- **API endpoint:** `GET /centralbank/domestic_exports`
- **Rows:** 2987
- **Source URL:** [https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1306010805_Value%20of%20Selected%20Domestic%20Exports%20-%20Selected%20Comms.csv](https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1306010805_Value%20of%20Selected%20Domestic%20Exports%20-%20Selected%20Comms.csv)

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 29 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Export commodity (e.g., coffee, tea, petroleum, horticulture, total) | No | 0 | 9 |
| value | float64 | Export value in KES millions (comma-formatted number) | No | 0 | 2970 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 2987 | 2011.92 | 8.00 | 1998.00 | 2005.00 | 2012.00 | 2019.00 | 2026.00 |
| value | 2987 | 8078.08 | 13787.33 | 4.98 | 503.81 | 2527.26 | 9460.50 | 91579.94 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | August | coffee | 500.47 |
| 1998 | September | coffee | 536.21 |
| 1998 | October | coffee | 584.32 |
| 1998 | November | coffee | 578.74 |
| 1998 | December | coffee | 574.54 |
