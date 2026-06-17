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
<td data-label="Unique">13</td>
</tr>
<tr>
<td data-label="Column"><code>area_level</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Geographic level</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">1</td>
</tr>
<tr>
<td data-label="Column"><code>area_name</code></td>
<td data-label="Type">object</td>
<td data-label="Description">County name (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">1</td>
</tr>
<tr>
<td data-label="Column"><code>metric</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Sub-domain or category within the indicator (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">1</td>
</tr>
<tr>
<td data-label="Column"><code>item</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Specific item or commodity being measured (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">1</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the indicator</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">13</td>
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
<td data-label="Count">13</td>
<td data-label="Mean">101542.15</td>
<td data-label="Std">69993.53</td>
<td data-label="Min">1268.00</td>
<td data-label="25%">44250.00</td>
<td data-label="50%">96000.00</td>
<td data-label="75%">160900.00</td>
<td data-label="Max">205955.00</td>
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
<td data-label="year">2021</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">land, inputs and sustainability</td>
<td data-label="item">fertilizer</td>
<td data-label="value">7598.0</td>
</tr>
<tr>
<td data-label="year">2020</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">land, inputs and sustainability</td>
<td data-label="item">fertilizer</td>
<td data-label="value">1268.0</td>
</tr>
<tr>
<td data-label="year">2019</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">land, inputs and sustainability</td>
<td data-label="item">fertilizer</td>
<td data-label="value">44250.0</td>
</tr>
<tr>
<td data-label="year">2018</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">land, inputs and sustainability</td>
<td data-label="item">fertilizer</td>
<td data-label="value">160900.0</td>
</tr>
<tr>
<td data-label="year">2017</td>
<td data-label="area_level">country</td>
<td data-label="area_name">kenya</td>
<td data-label="metric">land, inputs and sustainability</td>
<td data-label="item">fertilizer</td>
<td data-label="value">177600.0</td>
</tr>
</tbody>
</table>
