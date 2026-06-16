---
title: "GOK Fertilizer Subsidy Funds Allocated"
description: "Funds allocated for the government fertilizer subsidy program across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/gok_fertilizer_subsidy_funds_allocated"
rows: 12
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 12 |
| area_level | object | Geographic level (always county) | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 1 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 1 |
| value | float64 | Numeric value of the indicator | No | 0 | 12 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 12 | 3.76e+09 | 1.808e+09 | 0.00 | 6.3e+09 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2020 | country | kenya | land, inputs and sustainability | fertilizer | 0.0 |
| 2019 | country | kenya | land, inputs and sustainability | fertilizer | 6300000000.0 |
| 2018 | country | kenya | land, inputs and sustainability | fertilizer | 5569300200.0 |
| 2017 | country | kenya | land, inputs and sustainability | fertilizer | 4598000000.0 |
| 2016 | country | kenya | land, inputs and sustainability | fertilizer | 5459662652.0 |
