---
title: "Monthly Exchange Rates (Period Average)"
description: "Monthly exchange rates of major currencies against KES (period average)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/forex_period_average"
rows: 7980
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/exchange_rates/2034093818_Monthly%20Exchange%20rate%20(period%20average).csv"
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
<td data-label="Unique">34</td>
</tr>
<tr>
<td data-label="Column"><code>month</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Calendar month name</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">12</td>
</tr>
<tr>
<td data-label="Column"><code>metric</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Foreign currency name (e.g., united states dollar, sterling pound)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">29</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Period-average exchange rate in KES per unit of foreign currency (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">4807</td>
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
<td data-label="Count">7980</td>
<td data-label="Mean">2009.70</td>
<td data-label="Std">9.58</td>
<td data-label="Min">1993.00</td>
<td data-label="25%">2001.00</td>
<td data-label="50%">2010.00</td>
<td data-label="75%">2018.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">7980</td>
<td data-label="Mean">41.55</td>
<td data-label="Std">40.21</td>
<td data-label="Min">1.08</td>
<td data-label="25%">11.25</td>
<td data-label="50%">21.72</td>
<td data-label="75%">70.09</td>
<td data-label="Max">202.88</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;united states dollar&quot;,
    &quot;value&quot;: 36.23
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;sterling pound&quot;,
    &quot;value&quot;: 55.62
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;deutch mark&quot;,
    &quot;value&quot;: 22.44
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;canadian dollar&quot;,
    &quot;value&quot;: 28.36
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;french franc&quot;,
    &quot;value&quot;: 6.62
  }
]</code></pre>
