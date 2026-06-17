---
title: "Principal Exports — Volume, Value, Unit Prices"
description: "Monthly volume, value, and average unit prices of principal exports (coffee, tea, horticulture)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/principal_exports"
rows: 2988
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/766913717_Principal%20Exports_Volume,%20Value%20and%20Unit%20Prices.csv"
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
<td data-label="Description">Commodity and measure (coffee volume, coffee value, coffee average, tea volume, tea value, tea average, horticulture volume, horticulture value, horticulture average)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">9</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Volume in Kgs, value in KES millions, or average price in KES per kg (comma-formatted number; see Metric for unit)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">2985</td>
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
<td data-label="Count">2988</td>
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
<td data-label="Count">2988</td>
<td data-label="Mean">99304.28</td>
<td data-label="Std">157096.24</td>
<td data-label="Min">130.21</td>
<td data-label="25%">4437.56</td>
<td data-label="50%">21906.24</td>
<td data-label="75%">162741.88</td>
<td data-label="Max">1.085e+06</td>
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
<td data-label="metric">coffee volume</td>
<td data-label="value">2759.82</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">september</td>
<td data-label="metric">coffee volume</td>
<td data-label="value">3243.7</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">october</td>
<td data-label="metric">coffee volume</td>
<td data-label="value">4158.57</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">november</td>
<td data-label="metric">coffee volume</td>
<td data-label="value">3958.47</td>
</tr>
<tr>
<td data-label="year">1998</td>
<td data-label="month">december</td>
<td data-label="metric">coffee volume</td>
<td data-label="value">3565.01</td>
</tr>
</tbody>
</table>
