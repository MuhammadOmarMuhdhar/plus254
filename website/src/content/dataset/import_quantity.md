---
title: "Import Quantity"
description: "Quantity of agricultural imports across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/import_quantity"
rows: 10
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
<td data-label="Unique">8</td>
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
<td data-label="Unique">2</td>
</tr>
<tr>
<td data-label="Column"><code>item</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Specific item or commodity being measured (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the indicator</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">9</td>
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
<td data-label="Count">10</td>
<td data-label="Mean">569349.80</td>
<td data-label="Std">272834.70</td>
<td data-label="Min">284169.00</td>
<td data-label="25%">361092.25</td>
<td data-label="50%">450512.00</td>
<td data-label="75%">777921.00</td>
<td data-label="Max">989619.00</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: &quot;2024&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;crops&quot;,
    &quot;item&quot;: &quot;sugarcane&quot;,
    &quot;value&quot;: 339345.0
  },
  {
    &quot;year&quot;: &quot;2024&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;trade&quot;,
    &quot;item&quot;: &quot;fertilizer&quot;,
    &quot;value&quot;: 834502.0
  },
  {
    &quot;year&quot;: &quot;2023&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;crops&quot;,
    &quot;item&quot;: &quot;sugarcane&quot;,
    &quot;value&quot;: 608178.0
  },
  {
    &quot;year&quot;: &quot;2022&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;crops&quot;,
    &quot;item&quot;: &quot;sugarcane&quot;,
    &quot;value&quot;: 320708.0
  },
  {
    &quot;year&quot;: &quot;2021&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;crops&quot;,
    &quot;item&quot;: &quot;sugarcane&quot;,
    &quot;value&quot;: 426334.0
  }
]</code></pre>
