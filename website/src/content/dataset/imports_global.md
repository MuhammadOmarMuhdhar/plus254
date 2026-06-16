---
title: "Value of Imports from Rest of World"
description: "Monthly value of direct imports from selected countries outside Africa"
source: "Central Bank of Kenya"
endpoint: "GET /economy/imports_global"
rows: 4371
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1436491729_Value%20of%20Direct%20Imports%20from%20Selected%20Rest%20of%20the%20World%20Countries.csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 29 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Origin country (e.g., u.k, u.s.a, china, india, total) | No | 0 | 13 |
| value | float64 | Import value in KES millions (comma-formatted number) | No | 0 | 4340 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 4371 | 2011.73 | 8.11 | 1998.00 | 2005.00 | 2012.00 | 2019.00 | 2026.00 |
| value | 4371 | 17128.71 | 38763.90 | 88.27 | 1739.97 | 3845.89 | 12251.81 | 332367.64 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1998 | january | u.k | 1870.74 |
| 1998 | february | u.k | 1725.03 |
| 1998 | march | u.k | 1986.62 |
| 1998 | april | u.k | 1581.62 |
| 1998 | may | u.k | 1835.51 |
