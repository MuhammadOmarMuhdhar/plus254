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

<table class="dataset-table">
<thead>
<tr><th>Column</th><th>Type</th><th>Description</th><th>Nullable</th><th>Null count</th><th>Unique</th></tr>
</thead>
<tbody>
<tr>
<td data-label="Column"><code>year</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Calendar year</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">59</td>
</tr>
<tr>
<td data-label="Column"><code>area_level</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Geographic level</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2</td>
</tr>
<tr>
<td data-label="Column"><code>area_name</code></td>
<td data-label="Type">object</td>
<td data-label="Description">County name (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2</td>
</tr>
<tr>
<td data-label="Column"><code>metric</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Sub-domain or category within the indicator (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2</td>
</tr>
<tr>
<td data-label="Column"><code>item</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Specific item or commodity being measured (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">3</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the indicator</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">61</td>
</tr>
</tbody>
</table>

## Summary Statistics

<table class="dataset-table">
<thead>
<tr><th>Column</th><th>Count</th><th>Mean</th><th>Std</th><th>Min</th><th>25%</th><th>50%</th><th>75%</th><th>Max</th></tr>
</thead>
<tbody>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">62</td>
<td data-label="Mean">1.555e+07</td>
<td data-label="Std">1.033e+07</td>
<td data-label="Min">20.00</td>
<td data-label="25%">8.446e+06</td>
<td data-label="50%">1.385e+07</td>
<td data-label="75%">1.771e+07</td>
<td data-label="Max">4.047e+07</td>
</tr>
</tbody>
</table>

## Sample Data

<table class="dataset-table">
<thead>
<tr><th>year</th><th>area_level</th><th>area_name</th><th>metric</th><th>item</th><th>value</th></tr>
</thead>
<tbody>
<tr>
<td data-label="year">2024</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">crops</td>
<td data-label="item">tea( green leaf tea)</td>
<td data-label="value">37502000.0</td>
</tr>
<tr>
<td data-label="year">2024</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">land, inputs and sustainability</td>
<td data-label="item">fertilizer</td>
<td data-label="value">723637.0</td>
</tr>
<tr>
<td data-label="year">2023</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">crops</td>
<td data-label="item">tea( green leaf tea)</td>
<td data-label="value">37303000.0</td>
</tr>
<tr>
<td data-label="year">2022</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">crops</td>
<td data-label="item">tea( green leaf tea)</td>
<td data-label="value">36352809.0</td>
</tr>
<tr>
<td data-label="year">2022</td>
<td data-label="area_level">county</td>
<td data-label="area_name">narok</td>
<td data-label="metric">crops</td>
<td data-label="item">cowpeas</td>
<td data-label="value">20.0</td>
</tr>
</tbody>
</table>
