---
title: "Monthly Exchange Rates (Period Average)"
description: "Monthly exchange rates of major currencies against KES (period average)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/forex_period_average"
rows: 7980
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/exchange_rates/2034093818_Monthly%20Exchange%20rate%20(period%20average).csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 34 |
| month | object | Calendar month name | No | 0 | 12 |
| metric | object | Foreign currency name (e.g., united states dollar, sterling pound) | No | 0 | 29 |
| value | float64 | Period-average exchange rate in KES per unit of foreign currency (comma-formatted number) | No | 0 | 4807 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| year | 7980 | 2009.70 | 9.58 | 1993.00 | 2001.00 | 2010.00 | 2018.00 | 2026.00 |
| value | 7980 | 41.55 | 40.21 | 1.08 | 11.25 | 21.72 | 70.09 | 202.88 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1993 | january | united states dollar | 36.23 |
| 1993 | january | sterling pound | 55.62 |
| 1993 | january | deutch mark | 22.44 |
| 1993 | january | canadian dollar | 28.36 |
| 1993 | january | french franc | 6.62 |
