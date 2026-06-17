---
title: "Value of Imports from Rest of World"
description: "Monthly value of direct imports from selected countries outside Africa"
source: "Central Bank of Kenya"
endpoint: "GET /economy/imports_global"
rows: 4371
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1436491729_Value%20of%20Direct%20Imports%20from%20Selected%20Rest%20of%20the%20World%20Countries.csv"
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
<td data-label="Description">Origin country (e.g., u.k, u.s.a, china, india, total)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">13</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Import value in KES millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">4340</td>
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
<td data-label="Count">4371</td>
<td data-label="Mean">2011.73</td>
<td data-label="Std">8.11</td>
<td data-label="Min">1998.00</td>
<td data-label="25%">2005.00</td>
<td data-label="50%">2012.00</td>
<td data-label="75%">2019.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">4371</td>
<td data-label="Mean">17128.71</td>
<td data-label="Std">38763.90</td>
<td data-label="Min">88.27</td>
<td data-label="25%">1739.97</td>
<td data-label="50%">3845.89</td>
<td data-label="75%">12251.81</td>
<td data-label="Max">332367.64</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1870.74
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;february&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1725.03
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;march&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1986.62
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;april&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1581.62
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;may&quot;,
    &quot;metric&quot;: &quot;u.k&quot;,
    &quot;value&quot;: 1835.51
  }
]</code></pre>
