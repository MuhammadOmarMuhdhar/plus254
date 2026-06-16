---
title: "Export Quantity"
description: "Quantity of agricultural exports across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/export_quantity"
rows: 111
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 72 |
| area_level | object | Geographic level (always county) | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 1 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 2 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 9 |
| value | float64 | Numeric value of the indicator | No | 0 | 103 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 111 | 1.339e+08 | 1.783e+08 | 97.00 | 5.945e+08 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2024 | country | kenya | crops | pyrethrum | 30584.0 |
| 2024 | country | kenya | crops | bixa | 65100.0 |
| 2024 | country | kenya | crops | miraa | 4776964.0 |
| 2024 | country | kenya | crops | tea( green leaf tea) | 594503000.0 |
| 2024 | country | kenya | crops | cashew nuts | 419.79 |
