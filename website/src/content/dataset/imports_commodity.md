---
title: "Value of Imports by Commodity"
description: "Monthly value of direct imports classified by SITC sections"
source: "Central Bank of Kenya"
endpoint: "GET /centralbank/imports_commodity"
rows: 3320
category: "centralbank"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1126743207_Value%20of%20Direct%20Imports%20by%20Commodities.csv"
---

Monthly value of direct imports classified by SITC sections

- **Source:** Central Bank of Kenya
- **API endpoint:** `GET /centralbank/imports_commodity`
- **Rows:** 3320
- **Source URL:** [https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1126743207_Value%20of%20Direct%20Imports%20by%20Commodities.csv](https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1126743207_Value%20of%20Direct%20Imports%20by%20Commodities.csv)

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 29 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | SITC commodity section (e.g., food and live animals, chemicals, machinery and transport equipment, total) | No | 0 | 10 |
| value | float64 | Import value in KES millions (comma-formatted number) | No | 0 | 3320 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 3320 | 2011.92 | 8.00 | 1998.00 | 2005.00 | 2012.00 | 2019.00 | 2026.00 |
| value | 3320 | 22462.59 | 42207.78 | 36.09 | 2277.22 | 7664.27 | 23063.78 | 332367.64 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | August | food and live animals | 1413.87 |
| 1998 | September | food and live animals | 533.13 |
| 1998 | October | food and live animals | 586.56 |
| 1998 | November | food and live animals | 522.81 |
| 1998 | December | food and live animals | 717.97 |
