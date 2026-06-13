---
title: "Value of Exports to Rest of World"
description: "Monthly value of exports to selected countries outside Africa"
source: "Central Bank of Kenya"
endpoint: "GET /centralbank/exports_global"
rows: 4067
category: "centralbank"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/310335175_Value%20of%20Exports%20to%20Selected%20Rest%20of%20World%20Countries.csv"
---

Monthly value of exports to selected countries outside Africa

- **Source:** Central Bank of Kenya
- **API endpoint:** `GET /centralbank/exports_global`
- **Rows:** 4067
- **Source URL:** [https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/310335175_Value%20of%20Exports%20to%20Selected%20Rest%20of%20World%20Countries.csv](https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/310335175_Value%20of%20Exports%20to%20Selected%20Rest%20of%20World%20Countries.csv)

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 29 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Destination country or region (e.g., u.k, germany, u.s.a, total) | No | 0 | 12 |
| value | float64 | Export value in KES millions (comma-formatted number) | No | 0 | 4048 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 4067 | 2011.63 | 8.16 | 1998.00 | 2005.00 | 2012.00 | 2019.00 | 2026.00 |
| value | 4067 | 7964.64 | 17945.01 | 9.58 | 715.54 | 2060.13 | 4958.42 | 178625.91 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | January | u.k | 1420.32 |
| 1998 | February | u.k | 1465.24 |
| 1998 | March | u.k | 1570.5 |
| 1998 | April | u.k | 1372.71 |
| 1998 | May | u.k | 1721.72 |
