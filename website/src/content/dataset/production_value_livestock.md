---
title: "Production Value (Livestock)"
description: "Value of livestock production across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/production_value_livestock"
rows: 2156
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
<td data-label="Unique">5</td>
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
<td data-label="Unique">47</td>
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
<td data-label="Unique">14</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the indicator</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2003</td>
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
<td data-label="Count">2156</td>
<td data-label="Mean">2.502e+09</td>
<td data-label="Std">9.458e+09</td>
<td data-label="Min">4004.00</td>
<td data-label="25%">3.365e+07</td>
<td data-label="50%">3.306e+08</td>
<td data-label="75%">1.475e+09</td>
<td data-label="Max">1.9e+11</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;pork&quot;,
    &quot;value&quot;: 6562080.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;honey&quot;,
    &quot;value&quot;: 698504400.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;crops&quot;,
    &quot;item&quot;: &quot;wool&quot;,
    &quot;value&quot;: 378936.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;wax&quot;,
    &quot;value&quot;: 30479155.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;meat goat (chevon)&quot;,
    &quot;value&quot;: 703983150.0
  }
]</code></pre>
