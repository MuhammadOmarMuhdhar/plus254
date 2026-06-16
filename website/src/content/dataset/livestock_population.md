---
title: "Livestock Population"
description: "Livestock population counts across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/livestock_population"
rows: 8381
topic: "agriculture"
sourceUrl: "https://statistics.kilimo.go.ke"
lastUpdated: "2026-06-15T12:42:19"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| year | object | Calendar year | No | 0 | 14 |
| area_level | object | Geographic level (always county) | No | 0 | 2 |
| area_name | object | County name (lowercased) | No | 0 | 47 |
| metric | object | Sub-domain or category within the indicator (lowercased) | No | 0 | 1 |
| item | object | Specific item or commodity being measured (lowercased) | No | 0 | 25 |
| value | float64 | Numeric value of the indicator | No | 0 | 6498 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 8381 | 289555.58 | 1.9e+06 | 1.00 | 6.341e+07 |

## Sample Data

| year | area_level | area_name | metric | item | value |
|---|---|---|---|---|---|
| 2025 | county | baringo | livestock | guinea fowl | 461.0 |
| 2025 | county | baringo | livestock | dairy cattle | 159945.0 |
| 2025 | county | baringo | livestock | hair sheep | 371871.0 |
| 2025 | county | baringo | livestock | log hives | 181080.0 |
| 2025 | county | baringo | livestock | kenya top bar hive (ktbh) | 35544.0 |
