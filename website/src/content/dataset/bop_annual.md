---
title: "Balance of Payments (Annual)"
description: "Annual balance of payments statement"
source: "Central Bank of Kenya"
endpoint: "GET /economy/bop_annual"
rows: 357
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1657248905_Balance%20of%20Payments%20Statement%20(Annual%20Calender%20Year).csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 7 |
| metric | object | BPM6 balance of payments category (e.g., A. Current Account, n.i.e., General government) | No | 0 | 41 |
| value | float64 | Value in USD millions (comma-formatted number) | No | 0 | 291 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| year | 357 | 2022.00 | 2.00 | 2019.00 | 2025.00 |
| value | 357 | 111566.80 | 512985.75 | -1.401e+06 | 3.063e+06 |

## Sample Data

| year | metric | value |
|---|---|---|
| 2019 | a. current account, n.i.e. | -507653.0 |
| 2019 | other debt instruments | 57834.0 |
| 2019 | central bank | 0.0 |
| 2019 | deposit-taking corporations, except the central bank | 55710.0 |
| 2019 | general government | 0.0 |
