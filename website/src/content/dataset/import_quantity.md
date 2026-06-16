---
title: "Import Quantity"
description: "Quantity of agricultural imports across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/import_quantity"
rows: 10
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 8 |
| area_level | object | Geographic level | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 1 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 2 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 2 |
| value | float64 | Numeric value of the indicator | No | 0 | 9 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 10 | 569349.80 | 272834.70 | 284169.00 | 361092.25 | 450512.00 | 777921.00 | 989619.00 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2024 | country | kenya | crops | sugarcane | 339345.0 |
| 2024 | country | kenya | trade | fertilizer | 834502.0 |
| 2023 | country | kenya | crops | sugarcane | 608178.0 |
| 2022 | country | kenya | crops | sugarcane | 320708.0 |
| 2021 | country | kenya | crops | sugarcane | 426334.0 |
