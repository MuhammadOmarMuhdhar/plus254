---
title: "Crop Area"
description: "Area under crop cultivation across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/crop_area"
rows: 5186
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 125 |
| area_level | object | Geographic level (always county) | No | 0 | 2 |
| area_name | object | County name (lowercased) | No | 0 | 48 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 24 |
| value | float64 | Numeric value of the indicator | No | 0 | 3231 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 5186 | 44480.63 | 183212.45 | 0.00 | 2.407e+06 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | baringo | crops | sunflower | 9.0 |
| 2025 | county | baringo | crops | canola (rapeseed) | 105.0 |
| 2025 | county | baringo | crops | ground nuts | 117.0 |
| 2025 | county | baringo | crops | macadamia nuts | 345.8 |
| 2025 | county | baringo | crops | sunflower | 9.0 |
