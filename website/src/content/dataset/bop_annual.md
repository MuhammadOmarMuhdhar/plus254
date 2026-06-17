---
title: "Balance of Payments (Annual)"
description: "Annual balance of payments statement"
source: "Central Bank of Kenya"
endpoint: "GET /economy/bop_annual"
rows: 357
topic: "economy"
sourceUrl: "https://www.centralbank.go.ke/uploads/balance_of_payment_statistics/1657248905_Balance%20of%20Payments%20Statement%20(Annual%20Calender%20Year).csv"
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
<td data-label="Unique">7</td>
</tr>
<tr>
<td data-label="Column"><code>metric</code></td>
<td data-label="Type">object</td>
<td data-label="Description">BPM6 balance of payments category (e.g., A. Current Account, n.i.e., General government)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">41</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Value in USD millions (comma-formatted number)</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">291</td>
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
<td data-label="Count">357</td>
<td data-label="Mean">2022.00</td>
<td data-label="Std">2.00</td>
<td data-label="Min">2019.00</td>
<td data-label="25%">2020.00</td>
<td data-label="50%">2022.00</td>
<td data-label="75%">2024.00</td>
<td data-label="Max">2025.00</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Count">357</td>
<td data-label="Mean">111566.80</td>
<td data-label="Std">512985.75</td>
<td data-label="Min">-1.401e+06</td>
<td data-label="25%">-306.70</td>
<td data-label="50%">9230.00</td>
<td data-label="75%">133316.00</td>
<td data-label="Max">3.063e+06</td>
</tr>
</tbody>
</table>

## Sample Data

<table class="dataset-table">
<thead>
<tr><th>year</th><th>metric</th><th>value</th></tr>
</thead>
<tbody>
<tr>
<td data-label="year">2019</td>
<td data-label="metric">a. current account, n.i.e.</td>
<td data-label="value">-507653.0</td>
</tr>
<tr>
<td data-label="year">2019</td>
<td data-label="metric">other debt instruments</td>
<td data-label="value">57834.0</td>
</tr>
<tr>
<td data-label="year">2019</td>
<td data-label="metric">central bank</td>
<td data-label="value">0.0</td>
</tr>
<tr>
<td data-label="year">2019</td>
<td data-label="metric">deposit-taking corporations, except the central bank</td>
<td data-label="value">55710.0</td>
</tr>
<tr>
<td data-label="year">2019</td>
<td data-label="metric">general government</td>
<td data-label="value">0.0</td>
</tr>
</tbody>
</table>
