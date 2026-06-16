---
title: "Production Value (Crops)"
description: "Value of crop production across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/production_value_crops"
rows: 647
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 11 |
| area_level | object | Geographic level | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 38 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 10 |
| value | float64 | Numeric value of the indicator | No | 0 | 545 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 647 | 1.882e+08 | 5.366e+08 | 0.00 | 3.505e+06 | 2.654e+07 | 1.359e+08 | 5.148e+09 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | baringo | crops | macadamia nuts | 465000000.0 |
| 2025 | county | bomet | crops | sunflower | 4900000.0 |
| 2025 | county | bungoma | crops | sesame | 900000.0 |
| 2025 | county | bungoma | crops | ground nuts | 210000000.0 |
| 2025 | county | bungoma | crops | sunflower | 58000000.0 |
