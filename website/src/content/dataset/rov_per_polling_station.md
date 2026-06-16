---
title: "Registered Voters per Polling Station"
description: "Number of registered voters per polling station across all 47 counties for the 2022 General Election"
source: "Independent Electoral and Boundaries Commission (IEBC) Kenya"
endpoint: "GET /governance/rov_per_polling_station"
rows: 37250
topic: "governance"
sourceUrl: "https://www.iebc.or.ke/docs/rov_per_polling_station.pdf"
---

## Columns

| Column | Type | Description | Nullable | Null count | Unique |
|--------|------|-------------|----------|------------|--------|
| county_code | object | 3-digit numeric county code | No | 0 | 50 |
| county_name | object | County name | Yes | 1 | 49 |
| const_code | object | Constituency code | Yes | 1 | 292 |
| const_name | object | Constituency name | Yes | 1 | 292 |
| caw_code | object | County Assembly Ward code | Yes | 1 | 1461 |
| caw_name | object | County Assembly Ward name | Yes | 1 | 1418 |
| reg_centre_code | object | Registration Centre code | Yes | 1 | 259 |
| reg_centre_name | object | Registration Centre name | Yes | 1 | 20475 |
| polling_station_code | object | Unique polling station code | Yes | 1 | 37249 |
| polling_station_name_name | object |  | Yes | 1 | 20475 |
| value | float64 | Number of registered voters at the polling station | No | 0 | 555 |

## Summary Statistics

| Column | Count | Mean | Std | Min | Max |
|--------|-------|------|-----|-----|-----|
| value | 37250 | 1082.80 | 114609.82 | 1.00 | 2.212e+07 |

## Sample Data

| county_code | county_name | const_code | const_name | caw_code | caw_name | reg_centre_code | reg_centre_name | polling_station_code | polling_station_name_name | value |
|---|---|---|---|---|---|---|---|---|---|---|
| 001 | mombasa | 001 | changamwe | 0001 | port reitz | 001 | bomu primary school | 001001000100101 | bomu primary school | 673.0 |
| 001 | mombasa | 001 | changamwe | 0001 | port reitz | 001 | bomu primary school | 001001000100102 | bomu primary school | 673.0 |
| 001 | mombasa | 001 | changamwe | 0001 | port reitz | 001 | bomu primary school | 001001000100103 | bomu primary school | 673.0 |
| 001 | mombasa | 001 | changamwe | 0001 | port reitz | 001 | bomu primary school | 001001000100104 | bomu primary school | 672.0 |
| 001 | mombasa | 001 | changamwe | 0001 | port reitz | 001 | bomu primary school | 001001000100105 | bomu primary school | 672.0 |
