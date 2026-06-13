---
title: "Government Expenditure"
description: "Monthly government expenditure breakdown"
source: "Central Bank of Kenya"
endpoint: "GET /centralbank/fiscal_expenditure"
rows: 2656
category: "centralbank"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv"
---

Monthly government expenditure breakdown

- **Source:** Central Bank of Kenya
- **API endpoint:** `GET /centralbank/fiscal_expenditure`
- **Rows:** 2656
- **Source URL:** [https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv](https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv)

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| fiscal_year | int64 | Fiscal year (e.g., 1999 means FY 1999/2000) | No | 0 | 28 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Expenditure category (e.g., domestic interest, wages salaries, development expenditure, total expenditure) | No | 0 | 9 |
| value | float64 | Expenditure in KES millions (comma-formatted number) | No | 0 | 2627 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| fiscal_year | 2656 | 2013.09 | 7.54 | 1999.00 | 2007.00 | 2013.00 | 2020.00 | 2026.00 |
| value | 2656 | 236916.46 | 426253.67 | 0.00 | 21307.58 | 85394.30 | 249362.48 | 3.968e+06 |

## Sample Data

| fiscal_year | month | metric | value |
|---|---|---|---|
| 1999 | September | domestic interest | 3816.0 |
| 1999 | December | domestic interest | 8935.0 |
| 2000 | March | domestic interest | 15784.0 |
| 2000 | June | domestic interest | 20752.0 |
| 2000 | July | domestic interest | 2739.0 |
