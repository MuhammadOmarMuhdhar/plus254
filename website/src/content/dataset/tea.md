---
title: "Tea Production and Exports"
description: "Weekly tea auction data — production, export volume, and prices"
source: "Tea Board of Kenya"
endpoint: "GET /agriculture/tea"
rows: 84
topic: "agriculture"
sourceUrl: "https://eatta.co.ke/statistics"
---

## Columns

<table class="dataset-table">
<thead>
<tr><th>Column</th><th>Type</th><th>Description</th><th>Nullable</th><th>Null count</th><th>Unique</th></tr>
</thead>
<tbody>
<tr>
<td data-label="Column"><code>date</code></td>
<td data-label="Type">datetime64[ns]</td>
<td data-label="Description">Auction date (ISO 8601)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">21</td>
</tr>
<tr>
<td data-label="Column"><code>year</code></td>
<td data-label="Type">int64</td>
<td data-label="Description">Calendar year</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">1</td>
</tr>
<tr>
<td data-label="Column"><code>month</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Calendar month name</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">84</td>
<td data-label="Unique">0</td>
</tr>
<tr>
<td data-label="Column"><code>sale_week</code></td>
<td data-label="Type">int64</td>
<td data-label="Description">Sequential auction batch number (starts at 1 each year)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">21</td>
</tr>
<tr>
<td data-label="Column"><code>metric</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Auction metric name (Average price (USD), Tea sold (Kgs), Tea offered (Kgs), Unsold tea (%))</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">4</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Numeric value of the metric</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">69</td>
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
<td data-label="Count">84</td>
<td data-label="Mean">2026.00</td>
<td data-label="Std">0.00</td>
<td data-label="Min">2026.00</td>
<td data-label="25%">2026.00</td>
<td data-label="50%">2026.00</td>
<td data-label="75%">2026.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>sale_week</code></td>
<td data-label="Count">84</td>
<td data-label="Mean">11.00</td>
<td data-label="Std">6.09</td>
<td data-label="Min">1.00</td>
<td data-label="25%">6.00</td>
<td data-label="50%">11.00</td>
<td data-label="75%">16.00</td>
<td data-label="Max">21.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">84</td>
<td data-label="Mean">4.964e+06</td>
<td data-label="Std">5.068e+06</td>
<td data-label="Min">2.09</td>
<td data-label="25%">5.82</td>
<td data-label="50%">3.763e+06</td>
<td data-label="75%">9.667e+06</td>
<td data-label="Max">1.283e+07</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;date&quot;: &quot;2026-01-01 00:00:00&quot;,
    &quot;year&quot;: 2026,
    &quot;month&quot;: null,
    &quot;sale_week&quot;: 1,
    &quot;metric&quot;: &quot;average price (usd)&quot;,
    &quot;value&quot;: 2.13
  },
  {
    &quot;date&quot;: &quot;2026-01-01 00:00:00&quot;,
    &quot;year&quot;: 2026,
    &quot;month&quot;: null,
    &quot;sale_week&quot;: 1,
    &quot;metric&quot;: &quot;tea offered (kgs)&quot;,
    &quot;value&quot;: 9575196.0
  },
  {
    &quot;date&quot;: &quot;2026-01-01 00:00:00&quot;,
    &quot;year&quot;: 2026,
    &quot;month&quot;: null,
    &quot;sale_week&quot;: 1,
    &quot;metric&quot;: &quot;tea sold (kgs)&quot;,
    &quot;value&quot;: 8243508.0
  },
  {
    &quot;date&quot;: &quot;2026-01-01 00:00:00&quot;,
    &quot;year&quot;: 2026,
    &quot;month&quot;: null,
    &quot;sale_week&quot;: 1,
    &quot;metric&quot;: &quot;unsold tea (%)&quot;,
    &quot;value&quot;: 14.0
  },
  {
    &quot;date&quot;: &quot;2026-01-08 00:00:00&quot;,
    &quot;year&quot;: 2026,
    &quot;month&quot;: null,
    &quot;sale_week&quot;: 2,
    &quot;metric&quot;: &quot;average price (usd)&quot;,
    &quot;value&quot;: 2.19
  }
]</code></pre>
