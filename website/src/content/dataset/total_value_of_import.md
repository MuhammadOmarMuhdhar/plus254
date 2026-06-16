---
title: "Total Value of Imports"
description: "Total value of agricultural imports across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/total_value_of_import"
rows: 8
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 6 |
| area_level | object | Geographic level (always county) | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 1 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 1 |
| value | float64 | Numeric value of the indicator | No | 0 | 6 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 8 | 3.496e+10 | 1.803e+10 | 1.565e+10 | 5.659e+10 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2024 | country | kenya | crops | sugarcane | 30386987370.0 |
| 2023 | country | kenya | crops | sugarcane | 54460090849.0 |
| 2021 | country | kenya | crops | sugarcane | 25860198189.0 |
| 2020 | country | kenya | crops | sugarcane | 24467315258.0 |
| 2018 | country | kenya | crops | sugarcane | 15650673725.0 |
