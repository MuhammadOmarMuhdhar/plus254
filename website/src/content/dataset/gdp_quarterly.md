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

<table class="dataset-table">
<thead>
<tr><th>year</th><th>quarter</th><th>metric</th><th>value</th></tr>
</thead>
<tbody>
<tr>
<td data-label="year">2009</td>
<td data-label="quarter">q1</td>
<td data-label="metric">accommodation &amp; restaurant</td>
<td data-label="value">20371.0</td>
</tr>
<tr>
<td data-label="year">2009</td>
<td data-label="quarter">q1</td>
<td data-label="metric">agriculture</td>
<td data-label="value">312740.0</td>
</tr>
<tr>
<td data-label="year">2009</td>
<td data-label="quarter">q1</td>
<td data-label="metric">all industries at basic prices</td>
<td data-label="value">1231237.0</td>
</tr>
<tr>
<td data-label="year">2009</td>
<td data-label="quarter">q1</td>
<td data-label="metric">construction</td>
<td data-label="value">50218.0</td>
</tr>
<tr>
<td data-label="year">2009</td>
<td data-label="quarter">q1</td>
<td data-label="metric">education</td>
<td data-label="value">61140.0</td>
</tr>
</tbody>
</table>
