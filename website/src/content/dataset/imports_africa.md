---
title: "Value of Imports from Africa"
description: "Monthly value of direct imports from selected African countries"
source: "Central Bank of Kenya"
endpoint: "GET /economy/imports_africa"
rows: 2710
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1764709360_Value%20of%20Direct%20Imports%20from%20Selected%20African%20Countries.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 29 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Origin African country (e.g., uganda, tanzania, south africa, total) | No | 0 | 8 |
| value | float64 | Import value in KES millions (comma-formatted number) | No | 0 | 2685 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| year | 2710 | 2011.64 | 8.16 | 1998.00 | 2026.00 |
| value | 2710 | 2762.03 | 4387.60 | 0.00 | 28475.48 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | January | uganda | 2.06 |
| 1998 | February | uganda | 3.52 |
| 1998 | March | uganda | 5.72 |
| 1998 | April | uganda | 5.43 |
| 1998 | May | uganda | 11.65 |
