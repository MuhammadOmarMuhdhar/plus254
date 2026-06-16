---
title: "Apparent Consumption"
description: "Apparent consumption of agricultural commodities across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/apparent_consumption"
rows: 62
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 59 |
| area_level | object | Geographic level (always county) | No | 0 | 2 |
| area_name | object | County name (lowercased) | No | 0 | 2 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 2 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 3 |
| value | float64 | Numeric value of the indicator | No | 0 | 61 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 62 | 1.555e+07 | 1.033e+07 | 20.00 | 4.047e+07 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2024 | country | kenya | crops | tea( green leaf tea) | 37502000.0 |
| 2024 | country | kenya | land, inputs and sustainability | fertilizer | 723637.0 |
| 2023 | country | kenya | crops | tea( green leaf tea) | 37303000.0 |
| 2022 | country | kenya | crops | tea( green leaf tea) | 36352809.0 |
| 2022 | county | narok | crops | cowpeas | 20.0 |
