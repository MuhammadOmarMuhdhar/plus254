---
title: "Balance of Payments (Annual)"
description: "Annual balance of payments statement"
source: "Central Bank of Kenya"
endpoint: "GET /centralbank/bop_annual"
rows: 357
category: "centralbank"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1657248905_Balance%20of%20Payments%20Statement%20(Annual%20Calender%20Year).csv"
---

Annual balance of payments statement

- **Source:** Central Bank of Kenya
- **API endpoint:** `GET /centralbank/bop_annual`
- **Rows:** 357
- **Source URL:** [https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1657248905_Balance%20of%20Payments%20Statement%20(Annual%20Calender%20Year).csv](https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1657248905_Balance%20of%20Payments%20Statement%20(Annual%20Calender%20Year).csv)

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| category | object | BPM6 balance of payments category (e.g., A. Current Account, n.i.e., General government) | No | 0 | 41 |
| year | int64 | Calendar year | No | 0 | 7 |
| value | float64 | Value in USD millions (comma-formatted number) | No | 0 | 291 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 357 | 2022.00 | 2.00 | 2019.00 | 2020.00 | 2022.00 | 2024.00 | 2025.00 |
| value | 357 | 111566.80 | 512985.75 | -1.401e+06 | -306.70 | 9230.00 | 133316.00 | 3.063e+06 |

## Sample Data

| category | year | value |
|---|---|---|
| a. current account, n.i.e. | 2019 | -507653.0 |
| other debt instruments | 2019 | 57834.0 |
| central bank | 2019 | 0.0 |
| deposit-taking corporations, except the central bank | 2019 | 55710.0 |
| general government | 2019 | 0.0 |
