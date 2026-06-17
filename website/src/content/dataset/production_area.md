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
<td data-label="Unique">6</td>
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
<td data-label="Unique">26</td>
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
<td data-label="Unique">42</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the indicator</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">657</td>
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
<td data-label="Count">1146</td>
<td data-label="Mean">109266.68</td>
<td data-label="Std">1.784e+06</td>
<td data-label="Min">0.20</td>
<td data-label="25%">13.00</td>
<td data-label="50%">124.50</td>
<td data-label="75%">2592.50</td>
<td data-label="Max">4.25e+07</td>
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
<td data-label="area_name">embu</td>
<td data-label="metric">livestock</td>
<td data-label="item">rhodes grass</td>
<td data-label="value">429.0</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">embu</td>
<td data-label="metric">livestock</td>
<td data-label="item">columbus grass</td>
<td data-label="value">14.0</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">embu</td>
<td data-label="metric">livestock</td>
<td data-label="item">sesbania</td>
<td data-label="value">6.0</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">embu</td>
<td data-label="metric">livestock</td>
<td data-label="item">nappier grass</td>
<td data-label="value">12177.0</td>
</tr>
<tr>
<td data-label="year">2025</td>
<td data-label="area_level">county</td>
<td data-label="area_name">embu</td>
<td data-label="metric">livestock</td>
<td data-label="item">acacia</td>
<td data-label="value">14.0</td>
</tr>
</tbody>
</table>
