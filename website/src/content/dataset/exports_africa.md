---
title: "Value of Exports to Africa"
description: "Monthly value of exports to selected African countries"
source: "Central Bank of Kenya"
endpoint: "GET /economy/exports_africa"
rows: 4067
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1216083243_Value%20of%20Exports%20to%20Selected%20Africa%20Countries.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 29 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Destination African country (e.g., uganda, tanzania, egypt, total) | No | 0 | 12 |
| value | float64 | Export value in KES millions (comma-formatted number) | No | 0 | 4043 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 4067 | 2011.63 | 8.16 | 1998.00 | 2005.00 | 2012.00 | 2019.00 | 2026.00 |
| value | 4067 | 4053.11 | 10355.69 | 0.00 | 338.96 | 1056.55 | 2765.26 | 120186.87 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | january | uganda | 1386.42 |
| 1998 | february | uganda | 1204.81 |
| 1998 | march | uganda | 1478.77 |
| 1998 | april | uganda | 1629.02 |
| 1998 | may | uganda | 1466.8 |
