---
title: "Production Area"
description: "Area under agricultural production across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/production_area"
rows: 1146
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 6 |
| area_level | object | Geographic level (always county) | No | 0 | 1 |
| area_name | object | County name (lowercased) | No | 0 | 26 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 42 |
| value | float64 | Numeric value of the indicator | No | 0 | 657 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 1146 | 109266.68 | 1.784e+06 | 0.20 | 4.25e+07 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | embu | livestock | rhodes grass | 429.0 |
| 2025 | county | embu | livestock | columbus grass | 14.0 |
| 2025 | county | embu | livestock | sesbania | 6.0 |
| 2025 | county | embu | livestock | nappier grass | 12177.0 |
| 2025 | county | embu | livestock | acacia | 14.0 |
