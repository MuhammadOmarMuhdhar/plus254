---
title: "Value of Selected Domestic Exports"
description: "Monthly value of selected domestic export commodities"
source: "Central Bank of Kenya"
endpoint: "GET /economy/domestic_exports"
rows: 2987
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1306010805_Value%20of%20Selected%20Domestic%20Exports%20-%20Selected%20Comms.csv"
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
<td data-label="Description">Export commodity (e.g., coffee, tea, petroleum, horticulture, total)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">9</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Export value in KES millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2970</td>
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
<td data-label="Count">2987</td>
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
<td data-label="Count">2987</td>
<td data-label="Mean">8078.08</td>
<td data-label="Std">13787.33</td>
<td data-label="Min">4.98</td>
<td data-label="25%">503.81</td>
<td data-label="50%">2527.26</td>
<td data-label="75%">9460.50</td>
<td data-label="Max">91579.94</td>
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
<td data-label="metric">coffee</td>
<td data-label="value">500.47</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">september</td>
<td data-label="metric">coffee</td>
<td data-label="value">536.21</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">october</td>
<td data-label="metric">coffee</td>
<td data-label="value">584.32</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">november</td>
<td data-label="metric">coffee</td>
<td data-label="value">578.74</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">december</td>
<td data-label="metric">coffee</td>
<td data-label="value">574.54</td>
</tr>
</tbody>
</table>
