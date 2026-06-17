---
title: "Domestic Debt by Instrument"
description: "Monthly domestic debt breakdown by instrument (T-bills, bonds, etc.)"
source: "Central Bank of Kenya"
endpoint: "GET /economy/domestic_debt"
rows: 2191
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/government_finance_statistics/1263030173_Domestic%20Debt%20by%20Instrument.csv"
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
<td data-label="Unique">3</td>
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
<td data-label="Description">Debt instrument (treasury bills, treasury bonds, government stocks, advances from commercial banks, total domestic debt)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">7</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Debt in KES millions</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">1820</td>
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
<td data-label="Count">2191</td>
<td data-label="Mean">2000.96</td>
<td data-label="Std">0.22</td>
<td data-label="Min">1999.00</td>
<td data-label="25%">2001.00</td>
<td data-label="50%">2001.00</td>
<td data-label="75%">2001.00</td>
<td data-label="Max">2001.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">2191</td>
<td data-label="Mean">527793.29</td>
<td data-label="Std">1.165e+06</td>
<td data-label="Min">-575.96</td>
<td data-label="25%">1252.71</td>
<td data-label="50%">29769.47</td>
<td data-label="75%">390643.75</td>
<td data-label="Max">7.15e+06</td>
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
<td data-label="metric">treasury bills</td>
<td data-label="value">115068.55</td>
</tr>
<tr>
<td data-label="year">1999</td>
<td data-label="month">december</td>
<td data-label="metric">treasury bills</td>
<td data-label="value">121658.53</td>
</tr>
<tr>
<td data-label="year">2000</td>
<td data-label="month">march</td>
<td data-label="metric">treasury bills</td>
<td data-label="value">131224.49</td>
</tr>
<tr>
<td data-label="year">2000</td>
<td data-label="month">june</td>
<td data-label="metric">treasury bills</td>
<td data-label="value">131029.45</td>
</tr>
<tr>
<td data-label="year">2000</td>
<td data-label="month">july</td>
<td data-label="metric">treasury bills</td>
<td data-label="value">132167.45</td>
</tr>
</tbody>
</table>
