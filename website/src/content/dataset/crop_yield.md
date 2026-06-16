---
title: "Crop Yield"
description: "Crop yield per unit area across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/crop_yield"
rows: 4263
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 125 |
| area_level | object | Geographic level | No | 0 | 2 |
| area_name | object | County name (lowercased) | No | 0 | 48 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 2 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 23 |
| value | float64 | Numeric value of the indicator | No | 0 | 1605 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 4263 | 112.75 | 3240.45 | 0.00 | 0.54 | 1.00 | 3.00 | 146562.00 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | baringo | crops | canola (rapeseed) | 3.0 |
| 2025 | county | baringo | crops | sunflower | 1.0 |
| 2025 | county | bomet | crops | sunflower | 1.3968253968254 |
| 2025 | county | bungoma | crops | canola (rapeseed) | 3.0 |
| 2025 | county | bungoma | crops | ground nuts | 1.05328258801142 |
