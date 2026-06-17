---
title: "Quarterly GDP"
description: "Quarterly GDP estimates by sector"
source: "Central Bank of Kenya"
endpoint: "GET /economy/gdp_quarterly"
rows: 2725
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/national_accounts_statistics/1084903161_Quarterly%20GDP.csv"
---

## Columns

<table class="dataset-table">
<thead>
<tr><th>Column</th><th>Type</th><th>Description</th><th>Nullable</th><th>Null count</th><th>Unique</th></tr>
</thead>
<tbody>
<tr>
<td data-label="Column"><code>year</code></td>
<td data-label="Type">int64</td>
<td data-label="Description">Calendar year</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">17</td>
</tr>
<tr>
<td data-label="Column"><code>quarter</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Calendar quarter (Q1, Q2, Q3, Q4)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">4</td>
</tr>
<tr>
<td data-label="Column"><code>metric</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Economic sector or activity (e.g., Agriculture, Manufacturing, Construction, Total GDP)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">22</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">GDP value in KES millions</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2318</td>
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
<td data-label="Column"><code>year</code></td>
<td data-label="Count">2725</td>
<td data-label="Mean">2017.23</td>
<td data-label="Std">4.77</td>
<td data-label="Min">2009.00</td>
<td data-label="25%">2013.00</td>
<td data-label="50%">2017.00</td>
<td data-label="75%">2021.00</td>
<td data-label="Max">2025.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">2725</td>
<td data-label="Mean">197844.95</td>
<td data-label="Std">525256.08</td>
<td data-label="Min">-86324.78</td>
<td data-label="25%">4.92</td>
<td data-label="50%">2023.00</td>
<td data-label="75%">127815.00</td>
<td data-label="Max">2.948e+06</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: 2009,
    &quot;quarter&quot;: &quot;q1&quot;,
    &quot;metric&quot;: &quot;accommodation &amp; restaurant&quot;,
    &quot;value&quot;: 20371.0
  },
  {
    &quot;year&quot;: 2009,
    &quot;quarter&quot;: &quot;q1&quot;,
    &quot;metric&quot;: &quot;agriculture&quot;,
    &quot;value&quot;: 312740.0
  },
  {
    &quot;year&quot;: 2009,
    &quot;quarter&quot;: &quot;q1&quot;,
    &quot;metric&quot;: &quot;all industries at basic prices&quot;,
    &quot;value&quot;: 1231237.0
  },
  {
    &quot;year&quot;: 2009,
    &quot;quarter&quot;: &quot;q1&quot;,
    &quot;metric&quot;: &quot;construction&quot;,
    &quot;value&quot;: 50218.0
  },
  {
    &quot;year&quot;: 2009,
    &quot;quarter&quot;: &quot;q1&quot;,
    &quot;metric&quot;: &quot;education&quot;,
    &quot;value&quot;: 61140.0
  }
]</code></pre>
