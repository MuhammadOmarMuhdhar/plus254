---
title: "Cane Deliveries"
description: "Sugarcane deliveries to millers across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/cane_deliveries"
rows: 125
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 9 |
| area_level | object | Geographic level | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 14 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 1 |
| value | float64 | Numeric value of the indicator | No | 0 | 117 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 125 | 433140.00 | 393154.40 | 1598.00 | 120519.00 | 316415.00 | 633130.00 | 1.648e+06 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2023 | county | bungoma | crops | sugarcane | 1086003.0 |
| 2023 | county | bungoma | crops | sugarcane | 1086003.0 |
| 2023 | county | busia | crops | sugarcane | 479136.0 |
| 2023 | county | homa-bay | crops | sugarcane | 306987.0 |
| 2023 | county | kakamega | crops | sugarcane | 1026746.0 |
