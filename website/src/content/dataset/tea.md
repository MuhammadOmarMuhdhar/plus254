---
title: "Tea Production and Exports"
description: "Weekly tea auction data — production, export volume, and prices"
source: "Tea Board of Kenya"
endpoint: "GET /agriculture/tea"
rows: 84
topic: "agriculture"
sourceUrl: "https://eatta.co.ke/statistics"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| date | datetime64[ns] | Auction date (ISO 8601) | No | 0 | 21 |
| year | int64 | Calendar year | No | 0 | 1 |
| month | object | Calendar month name | Yes | 84 | 0 |
| sale_week | int64 | Sequential auction batch number (starts at 1 each year) | No | 0 | 21 |
| metric | object | Auction metric name (Average price (USD), Tea sold (Kgs), Tea offered (Kgs), Unsold tea (%)) | No | 0 | 4 |
| value | float64 | Numeric value of the metric | No | 0 | 69 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| year | 84 | 2026.00 | 0.00 | 2026.00 | 2026.00 |
| sale_week | 84 | 11.00 | 6.09 | 1.00 | 21.00 |
| value | 84 | 4.964e+06 | 5.068e+06 | 2.09 | 1.283e+07 |

## Sample Data

| date | year | month | sale_week | metric | value |
|---|---|---|---|---|---|
| 2026-01-01 00:00:00 | 2026 | None | 1 | average price (usd) | 2.13 |
| 2026-01-01 00:00:00 | 2026 | None | 1 | tea offered (kgs) | 9575196.0 |
| 2026-01-01 00:00:00 | 2026 | None | 1 | tea sold (kgs) | 8243508.0 |
| 2026-01-01 00:00:00 | 2026 | None | 1 | unsold tea (%) | 14.0 |
| 2026-01-08 00:00:00 | 2026 | None | 2 | average price (usd) | 2.19 |
