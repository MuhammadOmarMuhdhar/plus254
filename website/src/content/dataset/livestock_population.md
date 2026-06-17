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
<td data-label="Unique">14</td>
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
<td data-label="Unique">1</td>
</tr>
<tr>
<td data-label="Column"><code>item</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Specific item or commodity being measured (lowercased)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">25</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the indicator</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">6498</td>
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
<td data-label="Count">8381</td>
<td data-label="Mean">289555.58</td>
<td data-label="Std">1.9e+06</td>
<td data-label="Min">1.00</td>
<td data-label="25%">3728.00</td>
<td data-label="50%">22195.00</td>
<td data-label="75%">149671.00</td>
<td data-label="Max">6.341e+07</td>
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
    &quot;item&quot;: &quot;guinea fowl&quot;,
    &quot;value&quot;: 461.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;dairy cattle&quot;,
    &quot;value&quot;: 159945.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;hair sheep&quot;,
    &quot;value&quot;: 371871.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;log hives&quot;,
    &quot;value&quot;: 181080.0
  },
  {
    &quot;year&quot;: &quot;2025&quot;,
    &quot;area_level&quot;: &quot;county&quot;,
    &quot;area_name&quot;: &quot;baringo&quot;,
    &quot;metric&quot;: &quot;livestock&quot;,
    &quot;item&quot;: &quot;kenya top bar hive (ktbh)&quot;,
    &quot;value&quot;: 35544.0
  }
]</code></pre>
