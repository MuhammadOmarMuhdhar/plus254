---
title: "Government Expenditure"
description: "Monthly government expenditure breakdown"
source: "Central Bank of Kenya"
endpoint: "GET /economy/fiscal_expenditure"
rows: 2656
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/2118703754_Revenue%20and%20Expenditure.csv"
---

## Columns

<table class="dataset-table">
<thead>
<tr><th>Column</th><th>Type</th><th>Description</th><th>Nullable</th><th>Null count</th><th>Unique</th></tr>
</thead>
<tbody>
<tr>
<td data-label="Column"><code>fiscal_year</code></td>
<td data-label="Type">int64</td>
<td data-label="Description">Fiscal year (e.g., 1999 means FY 1999/2000)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">28</td>
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
<td data-label="Description">Expenditure category (e.g., domestic interest, wages salaries, development expenditure, total expenditure)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">9</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Expenditure in KES millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2627</td>
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
<td data-label="Column"><code>fiscal_year</code></td>
<td data-label="Count">2656</td>
<td data-label="Mean">2013.09</td>
<td data-label="Std">7.54</td>
<td data-label="Min">1999.00</td>
<td data-label="25%">2007.00</td>
<td data-label="50%">2013.00</td>
<td data-label="75%">2020.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">2656</td>
<td data-label="Mean">236916.46</td>
<td data-label="Std">426253.67</td>
<td data-label="Min">0.00</td>
<td data-label="25%">21307.58</td>
<td data-label="50%">85394.30</td>
<td data-label="75%">249362.48</td>
<td data-label="Max">3.968e+06</td>
</tr>
</tbody>
</table>

## Sample Data

<pre class="code-block"><code>[
  {
    &quot;fiscal_year&quot;: 1999,
    &quot;month&quot;: &quot;september&quot;,
    &quot;metric&quot;: &quot;domestic interest&quot;,
    &quot;value&quot;: 3816.0
  },
  {
    &quot;fiscal_year&quot;: 1999,
    &quot;month&quot;: &quot;december&quot;,
    &quot;metric&quot;: &quot;domestic interest&quot;,
    &quot;value&quot;: 8935.0
  },
  {
    &quot;fiscal_year&quot;: 2000,
    &quot;month&quot;: &quot;march&quot;,
    &quot;metric&quot;: &quot;domestic interest&quot;,
    &quot;value&quot;: 15784.0
  },
  {
    &quot;fiscal_year&quot;: 2000,
    &quot;month&quot;: &quot;june&quot;,
    &quot;metric&quot;: &quot;domestic interest&quot;,
    &quot;value&quot;: 20752.0
  },
  {
    &quot;fiscal_year&quot;: 2000,
    &quot;month&quot;: &quot;july&quot;,
    &quot;metric&quot;: &quot;domestic interest&quot;,
    &quot;value&quot;: 2739.0
  }
]</code></pre>
