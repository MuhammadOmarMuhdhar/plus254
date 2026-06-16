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

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| year | 4067 | 2011.63 | 8.16 | 1998.00 | 2026.00 |
| value | 4067 | 4053.11 | 10355.69 | 0.00 | 120186.87 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | January | uganda | 1386.42 |
| 1998 | February | uganda | 1204.81 |
| 1998 | March | uganda | 1478.77 |
| 1998 | April | uganda | 1629.02 |
| 1998 | May | uganda | 1466.8 |
