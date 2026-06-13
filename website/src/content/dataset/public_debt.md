---
title: "Public Debt"
description: "Monthly public debt (domestic and external)"
source: "Central Bank of Kenya"
endpoint: "GET /centralbank/public_debt"
rows: 930
category: "centralbank"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/565446111_Public%20Debt.csv"
---

Monthly public debt (domestic and external)

- **Source:** Central Bank of Kenya
- **API endpoint:** `GET /centralbank/public_debt`
- **Rows:** 930
- **Source URL:** [https://www.centralbank.go.ke/uploads/government_finance_statistics/565446111_Public%20Debt.csv](https://www.centralbank.go.ke/uploads/government_finance_statistics/565446111_Public%20Debt.csv)

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 27 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Debt component (domestic debt, external debt, total) | No | 0 | 3 |
| value | float64 | Debt in KES millions (comma-formatted number) | No | 0 | 929 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 930 | 2012.57 | 7.47 | 1999.00 | 2006.00 | 2013.00 | 2019.00 | 2025.00 |
| value | 930 | 2.405e+06 | 2.633e+06 | 183417.00 | 532894.31 | 1.184e+06 | 3.657e+06 | 1.23e+07 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1999 | September | domestic debt | 183417.0 |
| 1999 | December | domestic debt | 190300.0 |
| 2000 | March | domestic debt | 201463.22 |
| 2000 | June | domestic debt | 206127.0 |
| 2000 | July | domestic debt | 202362.0 |
