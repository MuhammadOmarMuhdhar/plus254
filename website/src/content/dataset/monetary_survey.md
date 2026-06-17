---
title: "Depository Corporation Survey"
description: "Monetary aggregates from the Depository Corporation Survey"
source: "Central Bank of Kenya"
endpoint: "GET /economy/monetary_survey"
rows: 12325
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/monetary_and_finance_statistics/274043565_Depository%20Corporation%20Survey%20-%20CSV.csv"
---

## Columns

<table class="dataset-table">
<thead>
<tr><th>Column</th><th>Type</th><th>Description</th><th>Nullable</th><th>Null count</th><th>Unique</th></tr>
</thead>
<tbody>
<tr>
<td data-label="Column"><code>section</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Sub-survey section (Central Bank of Kenya, Other Depository Corporation Survey, Depository Corporation Survey)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">3</td>
</tr>
<tr>
<td data-label="Column"><code>metric</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Monetary indicator name (e.g., Excess reserves, Required reserves, Broad Money M3)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">33</td>
</tr>
<tr>
<td data-label="Column"><code>year</code></td>
<td data-label="Type">int64</td>
<td data-label="Description">Calendar year</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">13</td>
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
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Monetary value in KES millions</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">11065</td>
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
<td data-label="Count">12325</td>
<td data-label="Mean">2019.77</td>
<td data-label="Std">3.47</td>
<td data-label="Min">2014.00</td>
<td data-label="25%">2017.00</td>
<td data-label="50%">2020.00</td>
<td data-label="75%">2023.00</td>
<td data-label="Max">2026.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">12325</td>
<td data-label="Mean">521115.29</td>
<td data-label="Std">1.258e+06</td>
<td data-label="Min">-2.445e+06</td>
<td data-label="25%">0.05</td>
<td data-label="50%">5796.00</td>
<td data-label="75%">323274.30</td>
<td data-label="Max">8.002e+06</td>
</tr>
</tbody>
</table>

## Sample Data

<table class="dataset-table">
<thead>
<tr><th>section</th><th>metric</th><th>year</th><th>month</th><th>value</th></tr>
</thead>
<tbody>
<tr>
<td data-label="section">central bank of kenya</td>
<td data-label="metric">    excess reserves</td>
<td data-label="year">2014</td>
<td data-label="month">january</td>
<td data-label="value">4792.0</td>
</tr>
<tr>
<td data-label="section">central bank of kenya</td>
<td data-label="metric">    required reserves</td>
<td data-label="year">2014</td>
<td data-label="month">january</td>
<td data-label="value">100001.0</td>
</tr>
<tr>
<td data-label="section">central bank of kenya</td>
<td data-label="metric">banks reserves at cbk</td>
<td data-label="year">2014</td>
<td data-label="month">january</td>
<td data-label="value">104793.0</td>
</tr>
<tr>
<td data-label="section">central bank of kenya</td>
<td data-label="metric">county government (net)</td>
<td data-label="year">2014</td>
<td data-label="month">january</td>
<td data-label="value">0.0</td>
</tr>
<tr>
<td data-label="section">central bank of kenya</td>
<td data-label="metric">credit to other depository corporations</td>
<td data-label="year">2014</td>
<td data-label="month">january</td>
<td data-label="value">4014.0</td>
</tr>
</tbody>
</table>
