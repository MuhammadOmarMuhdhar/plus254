---
title: "Monthly Exchange Rates (End Period)"
description: "Monthly exchange rates of major currencies against KES (end period)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/forex_end_period"
rows: 7970
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/exchange_rates/677633335_Monthly%20exchange%20rate%20(end%20period).csv"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | int64 | Calendar year | No | 0 | 34 |
| month | object | Calendar month name (e.g., January) | No | 0 | 12 |
| metric | object | Foreign currency name (e.g., united states dollar, sterling pound) | No | 0 | 29 |
| value | float64 | End-period exchange rate in KES per unit of foreign currency (comma-formatted number) | No | 0 | 4817 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| year | 7970 | 2009.71 | 9.58 | 1993.00 | 2026.00 |
| value | 7970 | 41.65 | 40.29 | 1.08 | 203.79 |

## Sample Data

| year | month | metric | value |
|---|---|---|---|
| 1993 | January | united states dollar | 35.92 |
| 1993 | January | sterling pound | 54.48 |
| 1993 | January | deutch mark | 22.67 |
| 1993 | January | canadian dollar | 28.3 |
| 1993 | January | french franc | 6.69 |
