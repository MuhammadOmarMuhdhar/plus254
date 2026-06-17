---
title: "Value of Exports to Rest of World"
description: "Monthly value of exports to selected countries outside Africa"
source: "Central Bank of Kenya"
endpoint: "GET /economy/exports_global"
rows: 4067
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/310335175_Value%20of%20Exports%20to%20Selected%20Rest%20of%20World%20Countries.csv"
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
<td data-label="Unique">29</td>
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
<td data-label="Description">Destination country or region (e.g., u.k, germany, u.s.a, total)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">12</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Export value in KES millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">4048</td>
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
<td data-label="Count">4067</td>
<td data-label="Mean">2011.63</td>
<td data-label="Std">8.16</td>
<td data-label="Min">1998.00</td>
<td data-label="25%">2005.00</td>
<td data-label="50%">2012.00</td>
<td data-label="75%">2019.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">4067</td>
<td data-label="Mean">7964.64</td>
<td data-label="Std">17945.01</td>
<td data-label="Min">9.58</td>
<td data-label="25%">715.54</td>
<td data-label="50%">2060.13</td>
<td data-label="75%">4958.42</td>
<td data-label="Max">178625.91</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1420.32
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;february&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1465.24
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;march&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1570.5
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;april&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1372.71
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;may&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1721.72
  }
]</code></pre>
