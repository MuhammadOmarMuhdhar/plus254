---
title: "Crop Area"
description: "Area under crop cultivation across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/crop_area"
rows: 5186
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
<td data-label="Unique">125</td>
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
<td data-label="Unique">48</td>
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
<td data-label="Unique">24</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the indicator</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">3231</td>
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
<td data-label="Count">5186</td>
<td data-label="Mean">44480.63</td>
<td data-label="Std">183212.45</td>
<td data-label="Min">0.00</td>
<td data-label="25%">136.00</td>
<td data-label="50%">1929.10</td>
<td data-label="75%">24454.25</td>
<td data-label="Max">2.407e+06</td>
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
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">baringo</td>
<td data-label="metric">crops</td>
<td data-label="item">sunflower</td>
<td data-label="value">9.0</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">baringo</td>
<td data-label="metric">crops</td>
<td data-label="item">canola (rapeseed)</td>
<td data-label="value">105.0</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">baringo</td>
<td data-label="metric">crops</td>
<td data-label="item">ground nuts</td>
<td data-label="value">117.0</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">baringo</td>
<td data-label="metric">crops</td>
<td data-label="item">macadamia nuts</td>
<td data-label="value">345.8</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">baringo</td>
<td data-label="metric">crops</td>
<td data-label="item">sunflower</td>
<td data-label="value">9.0</td>
</tr>
</tbody>
</table>
