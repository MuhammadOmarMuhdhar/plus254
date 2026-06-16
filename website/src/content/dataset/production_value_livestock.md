---
title: "Production Value (Livestock)"
description: "Value of livestock production across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/production_value_livestock"
rows: 2156
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 5 |
| area_level | object | Geographic level | No | 0 | 2 |
| area_name | object | County name (lowercased) | No | 0 | 47 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 2 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 14 |
| value | float64 | Numeric value of the indicator | No | 0 | 2003 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 2156 | 2.502e+09 | 9.458e+09 | 4004.00 | 3.365e+07 | 3.306e+08 | 1.475e+09 | 1.9e+11 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | baringo | livestock | pork | 6562080.0 |
| 2025 | county | baringo | livestock | honey | 698504400.0 |
| 2025 | county | baringo | crops | wool | 378936.0 |
| 2025 | county | baringo | livestock | wax | 30479155.0 |
| 2025 | county | baringo | livestock | meat goat (chevon) | 703983150.0 |
