---
title: "Production Quantity (Livestock)"
description: "Quantity of livestock production across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/production_quantity_livestock"
rows: 2151
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 5 |
| area_level | object | Geographic level (always county) | No | 0 | 2 |
| area_name | object | County name (lowercased) | No | 0 | 47 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 14 |
| value | float64 | Numeric value of the indicator | No | 0 | 1971 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 2151 | 1.593e+07 | 7.242e+07 | 5.70 | 2.409e+09 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | baringo | livestock | hides | 30618.0 |
| 2025 | county | baringo | livestock | milk | 47494407.0 |
| 2025 | county | baringo | livestock | eggs | 810983.0 |
| 2025 | county | baringo | livestock | honey | 1552232.0 |
| 2025 | county | baringo | livestock | pork | 13124.0 |
