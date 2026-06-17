---
title: "GOK Fertilizer Subsidy Funds Allocated"
description: "Funds allocated for the government fertilizer subsidy program across Kenyan counties"
source: "Kenya Agricultural Observatory Platform (Kilimo)"
endpoint: "GET /agriculture/gok_fertilizer_subsidy_funds_allocated"
rows: 12
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
<td data-label="Unique">12</td>
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
<td data-label="Unique">12</td>
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
<td data-label="Count">12</td>
<td data-label="Mean">3.76e+09</td>
<td data-label="Std">1.808e+09</td>
<td data-label="Min">0.00</td>
<td data-label="25%">3.158e+09</td>
<td data-label="50%">3.943e+09</td>
<td data-label="75%">4.813e+09</td>
<td data-label="Max">6.3e+09</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: &quot;2020&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;land, inputs and sustainability&quot;,
    &quot;item&quot;: &quot;fertilizer&quot;,
    &quot;value&quot;: 0.0
  },
  {
    &quot;year&quot;: &quot;2019&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;land, inputs and sustainability&quot;,
    &quot;item&quot;: &quot;fertilizer&quot;,
    &quot;value&quot;: 6300000000.0
  },
  {
    &quot;year&quot;: &quot;2018&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;land, inputs and sustainability&quot;,
    &quot;item&quot;: &quot;fertilizer&quot;,
    &quot;value&quot;: 5569300200.0
  },
  {
    &quot;year&quot;: &quot;2017&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;land, inputs and sustainability&quot;,
    &quot;item&quot;: &quot;fertilizer&quot;,
    &quot;value&quot;: 4598000000.0
  },
  {
    &quot;year&quot;: &quot;2016&quot;,
    &quot;area_level&quot;: &quot;country&quot;,
    &quot;area_name&quot;: &quot;kenya&quot;,
    &quot;metric&quot;: &quot;land, inputs and sustainability&quot;,
    &quot;item&quot;: &quot;fertilizer&quot;,
    &quot;value&quot;: 5459662652.0
  }
]</code></pre>
