---
title: "Value of Imports from Africa"
description: "Monthly value of direct imports from selected African countries"
source: "Central Bank of Kenya"
endpoint: "GET /economy/imports_africa"
rows: 2710
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1764709360_Value%20of%20Direct%20Imports%20from%20Selected%20African%20Countries.csv"
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
<td data-label="Description">Origin African country (e.g., uganda, tanzania, south africa, total)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">8</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Import value in KES millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2685</td>
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
<td data-label="Count">2710</td>
<td data-label="Mean">2011.64</td>
<td data-label="Std">8.16</td>
<td data-label="Min">1998.00</td>
<td data-label="25%">2005.00</td>
<td data-label="50%">2012.00</td>
<td data-label="75%">2019.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">2710</td>
<td data-label="Mean">2762.03</td>
<td data-label="Std">4387.60</td>
<td data-label="Min">0.00</td>
<td data-label="25%">181.89</td>
<td data-label="50%">1131.81</td>
<td data-label="75%">3329.29</td>
<td data-label="Max">28475.48</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;january&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 2.06
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;february&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 3.52
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;march&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 5.72
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;april&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 5.43
  },
  {
    &quot;year&quot;: 1998,
    &quot;month&quot;: &quot;may&quot;,
    &quot;metric&quot;: &quot;uganda&quot;,
    &quot;value&quot;: 11.65
  }
]</code></pre>
