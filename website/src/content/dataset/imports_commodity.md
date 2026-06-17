---
title: "Value of Imports by Commodity"
description: "Monthly value of direct imports classified by SITC sections"
source: "Central Bank of Kenya"
endpoint: "GET /economy/imports_commodity"
rows: 3320
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1126743207_Value%20of%20Direct%20Imports%20by%20Commodities.csv"
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
<td data-label="Description">SITC commodity section (e.g., food and live animals, chemicals, machinery and transport equipment, total)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">10</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Import value in KES millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">3320</td>
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
<td data-label="Count">3320</td>
<td data-label="Mean">2011.92</td>
<td data-label="Std">8.00</td>
<td data-label="Min">1998.00</td>
<td data-label="25%">2005.00</td>
<td data-label="50%">2012.00</td>
<td data-label="75%">2019.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">3320</td>
<td data-label="Mean">22462.59</td>
<td data-label="Std">42207.78</td>
<td data-label="Min">36.09</td>
<td data-label="25%">2277.22</td>
<td data-label="50%">7664.27</td>
<td data-label="75%">23063.78</td>
<td data-label="Max">332367.64</td>
</tr>
</tbody>
</table>

## Sample Data

<table class="dataset-table">
<thead>
<tr><th>year</th><th>month</th><th>metric</th><th>value</th></tr>
</thead>
<tbody>
<tr>
<td data-label="year">1998</td>
<td data-label="month">august</td>
<td data-label="metric">food and live animals</td>
<td data-label="value">1413.87</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">september</td>
<td data-label="metric">food and live animals</td>
<td data-label="value">533.13</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">october</td>
<td data-label="metric">food and live animals</td>
<td data-label="value">586.56</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">november</td>
<td data-label="metric">food and live animals</td>
<td data-label="value">522.81</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">december</td>
<td data-label="metric">food and live animals</td>
<td data-label="value">717.97</td>
</tr>
</tbody>
</table>
