---
title: "GOK Fertilizer Subsidy Beneficiaries"
description: "Beneficiaries of the government fertilizer subsidy program across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/gok_fertilizer_subsidy_beneficiaries"
rows: 13
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 12 |
| area_level | object | Geographic level | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 1 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 1 |
| value | float64 | Numeric value of the indicator | No | 0 | 12 |

## Summary Statistics

| Column | Count | Mean | Std | Min | 25% | 50% | 75% | Max |
|--------|-------|------|-----|-----|-----|-----|-----|-----|
| value | 13 | 377617.54 | 241184.74 | 0.00 | 220919.00 | 432485.00 | 507000.00 | 770000.00 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2020 | country | kenya | land, inputs and sustainability | fertilizer | 0.0 |
| 2019 | country | kenya | land, inputs and sustainability | fertilizer | 81298.0 |
| 2018 | country | kenya | land, inputs and sustainability | fertilizer | 700000.0 |
| 2017 | country | kenya | land, inputs and sustainability | fertilizer | 770000.0 |
| 2016 | country | kenya | land, inputs and sustainability | fertilizer | 507000.0 |
