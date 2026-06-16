---
title: "GOK Subsidized Fertilizer Quantity"
description: "Quantity of government-subsidized fertilizer distributed across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/quantity_of_gok_subsidized_fertilizer"
rows: 13
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 13 |
| area_level | object | Geographic level (always county) | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 1 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 1 |
| value | float64 | Numeric value of the indicator | No | 0 | 13 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 13 | 101542.15 | 69993.53 | 1268.00 | 205955.00 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2021 | country | kenya | land, inputs and sustainability | fertilizer | 7598.0 |
| 2020 | country | kenya | land, inputs and sustainability | fertilizer | 1268.0 |
| 2019 | country | kenya | land, inputs and sustainability | fertilizer | 44250.0 |
| 2018 | country | kenya | land, inputs and sustainability | fertilizer | 160900.0 |
| 2017 | country | kenya | land, inputs and sustainability | fertilizer | 177600.0 |
