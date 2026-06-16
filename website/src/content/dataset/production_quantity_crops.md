---
title: "Production Quantity (Crops)"
description: "Quantity of crop production across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/production_quantity_crops"
rows: 5352
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 126 |
| area_level | object | Geographic level | No | 0 | 2 |
| area_name | object | County name (lowercased) | No | 0 | 48 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 2 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 26 |
| value | float64 | Numeric value of the indicator | No | 0 | 3846 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 5352 | 1.803e+06 | 1.719e+07 | 0.00 | 105.75 | 2449.18 | 26799.50 | 3.731e+08 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | bungoma | crops | bambara groundnuts | 94.0 |
| 2025 | county | bungoma | crops | sesame | 7.0 |
| 2025 | county | busia | crops | sesame | 29.0 |
| 2025 | county | busia | crops | sunflower | 132.0 |
| 2025 | county | busia | crops | bambara groundnuts | 82.0 |
