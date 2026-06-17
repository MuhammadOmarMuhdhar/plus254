---
title: "Public Debt"
description: "Monthly public debt (domestic and external)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/public_debt"
rows: 930
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/565446111_Public%20Debt.csv"
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
<td data-label="Unique">27</td>
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
<td data-label="Description">Debt component (domestic debt, external debt, total)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">3</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Debt in KES millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">929</td>
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
<td data-label="Count">930</td>
<td data-label="Mean">2012.57</td>
<td data-label="Std">7.47</td>
<td data-label="Min">1999.00</td>
<td data-label="25%">2006.00</td>
<td data-label="50%">2013.00</td>
<td data-label="75%">2019.00</td>
<td data-label="Max">2025.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">930</td>
<td data-label="Mean">2.405e+06</td>
<td data-label="Std">2.633e+06</td>
<td data-label="Min">183417.00</td>
<td data-label="25%">532894.31</td>
<td data-label="50%">1.184e+06</td>
<td data-label="75%">3.657e+06</td>
<td data-label="Max">1.23e+07</td>
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
<td data-label="year">1999</td>
<td data-label="month">september</td>
<td data-label="metric">domestic debt</td>
<td data-label="value">183417.0</td>
</tr>
<tr>
<td data-label="year">1999</td>
<td data-label="month">december</td>
<td data-label="metric">domestic debt</td>
<td data-label="value">190300.0</td>
</tr>
<tr>
<td data-label="year">2000</td>
<td data-label="month">march</td>
<td data-label="metric">domestic debt</td>
<td data-label="value">201463.22</td>
</tr>
<tr>
<td data-label="year">2000</td>
<td data-label="month">june</td>
<td data-label="metric">domestic debt</td>
<td data-label="value">206127.0</td>
</tr>
<tr>
<td data-label="year">2000</td>
<td data-label="month">july</td>
<td data-label="metric">domestic debt</td>
<td data-label="value">202362.0</td>
</tr>
</tbody>
</table>
