---
title: "Monthly Exchange Rates (End Period)"
description: "Monthly exchange rates of major currencies against KES (end period)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/forex_end_period"
rows: 7970
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/exchange_rates/677633335_Monthly%20exchange%20rate%20(end%20period).csv"
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
<td data-label="Description">Calendar month name (e.g., January)</td>
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
<td data-label="Description">End-period exchange rate in KES per unit of foreign currency (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">4817</td>
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
<td data-label="Count">7970</td>
<td data-label="Mean">2009.71</td>
<td data-label="Std">9.58</td>
<td data-label="Min">1993.00</td>
<td data-label="25%">2001.00</td>
<td data-label="50%">2010.00</td>
<td data-label="75%">2018.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">7970</td>
<td data-label="Mean">41.65</td>
<td data-label="Std">40.29</td>
<td data-label="Min">1.08</td>
<td data-label="25%">11.25</td>
<td data-label="50%">21.70</td>
<td data-label="75%">70.34</td>
<td data-label="Max">203.79</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;united states dollar&quot;,
    &quot;value&quot;: 35.92
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;sterling pound&quot;,
    &quot;value&quot;: 54.48
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;deutch mark&quot;,
    &quot;value&quot;: 22.67
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;canadian dollar&quot;,
    &quot;value&quot;: 28.3
  },
  {
    &quot;year&quot;: 1993,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;french franc&quot;,
    &quot;value&quot;: 6.69
  }
]</code></pre>
