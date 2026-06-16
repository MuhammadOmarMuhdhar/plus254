---
title: "Total Value of Exports"
description: "Total value of agricultural exports across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/total_value_of_export"
rows: 94
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 73 |
| area_level | object | Geographic level | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 1 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 5 |
| value | float64 | Numeric value of the indicator | No | 0 | 89 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 94 | 3.019e+10 | 4.553e+10 | 8.2e+07 | 3.516e+08 | 5.844e+09 | 3.435e+10 | 1.817e+11 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2024 | country | kenya | crops | cashew nuts | 296770000.0 |
| 2024 | country | kenya | crops | sisal | 5737942389.16 |
| 2024 | country | kenya | crops | tea( green leaf tea) | 181690088120.0 |
| 2023/24 | country | kenya | crops | coffee | 39950000000.0 |
| 2023 | country | kenya | crops | sisal | 5343490000.0 |
