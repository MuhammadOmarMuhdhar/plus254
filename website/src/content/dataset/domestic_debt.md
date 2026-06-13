---
title: "Domestic Debt by Instrument"
description: "Monthly domestic debt breakdown by instrument (T-bills, bonds, etc.)"
source: "Central Bank of Kenya"
endpoint: "GET /centralbank/domestic_debt"
rows: 2191
category: "centralbank"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/1263030173_Domestic%20Debt%20by%20Instrument.csv"
---

Monthly domestic debt breakdown by instrument (T-bills, bonds, etc.)

- **Source:** Central Bank of Kenya
- **API endpoint:** `GET /centralbank/domestic_debt`
- **Rows:** 2191
- **Source URL:** [https://www.centralbank.go.ke/uploads/government_finance_statistics/1263030173_Domestic%20Debt%20by%20Instrument.csv](https://www.centralbank.go.ke/uploads/government_finance_statistics/1263030173_Domestic%20Debt%20by%20Instrument.csv)

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 3 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Debt instrument (treasury bills, treasury bonds, government stocks, advances from commercial banks, total domestic debt) | No | 0 | 7 |
| value | float64 | Debt in KES millions | No | 0 | 1820 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 2191 | 2000.96 | 0.22 | 1999.00 | 2001.00 | 2001.00 | 2001.00 | 2001.00 |
| value | 2191 | 527793.29 | 1.165e+06 | -575.96 | 1252.71 | 29769.47 | 390643.75 | 7.15e+06 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1999 | September | treasury bills | 115068.55 |
| 1999 | December | treasury bills | 121658.53 |
| 2000 | March | treasury bills | 131224.49 |
| 2000 | June | treasury bills | 131029.45 |
| 2000 | July | treasury bills | 132167.45 |
