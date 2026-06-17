---
title: "Value of Exports to Africa"
description: "Monthly value of exports to selected African countries"
source: "Central Bank of Kenya"
endpoint: "GET /economy/exports_africa"
rows: 4067
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1216083243_Value%20of%20Exports%20to%20Selected%20Africa%20Countries.csv"
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
<td data-label="Description">Destination African country (e.g., uganda, tanzania, egypt, total)</td>
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
<td data-label="Unique">4043</td>
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
<td data-label="Mean">4053.11</td>
<td data-label="Std">10355.69</td>
<td data-label="Min">0.00</td>
<td data-label="25%">338.96</td>
<td data-label="50%">1056.55</td>
<td data-label="75%">2765.26</td>
<td data-label="Max">120186.87</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 1386.42
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;february&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 1204.81
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;march&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 1478.77
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;april&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 1629.02
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;may&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 1466.8
  }
]</code></pre>
