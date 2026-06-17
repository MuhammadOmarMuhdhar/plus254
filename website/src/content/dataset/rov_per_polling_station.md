---
title: "Registered Voters per Polling Station"
description: "Number of registered voters per polling station across all 47 counties for the 2022 General Election"
source: "Independent Electoral and Boundaries Commission (IEBC) Kenya"
endpoint: "GET /governance/rov_per_polling_station"
rows: 37250
topic: "governance"
sourceUrl: "https://www.iebc.or.ke/docs/rov_per_polling_station.pdf"
---

## Columns

<table class="dataset-table">
<thead>
<tr><th>Column</th><th>Type</th><th>Description</th><th>Nullable</th><th>Null count</th><th>Unique</th></tr>
</thead>
<tbody>
<tr>
<td data-label="Column"><code>county_code</code></td>
<td data-label="Type">object</td>
<td data-label="Description">3-digit numeric county code</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">50</td>
</tr>
<tr>
<td data-label="Column"><code>county_name</code></td>
<td data-label="Type">object</td>
<td data-label="Description">County name</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">49</td>
</tr>
<tr>
<td data-label="Column"><code>const_code</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Constituency code</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">292</td>
</tr>
<tr>
<td data-label="Column"><code>const_name</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Constituency name</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">292</td>
</tr>
<tr>
<td data-label="Column"><code>caw_code</code></td>
<td data-label="Type">object</td>
<td data-label="Description">County Assembly Ward code</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">1461</td>
</tr>
<tr>
<td data-label="Column"><code>caw_name</code></td>
<td data-label="Type">object</td>
<td data-label="Description">County Assembly Ward name</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">1418</td>
</tr>
<tr>
<td data-label="Column"><code>reg_centre_code</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Registration Centre code</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">259</td>
</tr>
<tr>
<td data-label="Column"><code>reg_centre_name</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Registration Centre name</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">20475</td>
</tr>
<tr>
<td data-label="Column"><code>polling_station_code</code></td>
<td data-label="Type">object</td>
<td data-label="Description">Unique polling station code</td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">37249</td>
</tr>
<tr>
<td data-label="Column"><code>polling_station_name_name</code></td>
<td data-label="Type">object</td>
<td data-label="Description"></td>
<td data-label="Nullable">Yes</td>
<td data-label="Null count">1</td>
<td data-label="Unique">20475</td>
</tr>
<tr>
<td data-label="Column"><code>value</code></td>
<td data-label="Type">float64</td>
<td data-label="Description">Number of registered voters at the polling station</td>
<td data-label="Nullable">No</td>
<td data-label="Null count">0</td>
<td data-label="Unique">555</td>
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
<td data-label="Column"><code>value</code></td>
<td data-label="Count">37250</td>
<td data-label="Mean">1082.80</td>
<td data-label="Std">114609.82</td>
<td data-label="Min">1.00</td>
<td data-label="25%">389.00</td>
<td data-label="50%">510.00</td>
<td data-label="75%">628.00</td>
<td data-label="Max">2.212e+07</td>
</tr>
</tbody>
</table>

## Sample Data

<table class="dataset-table">
<thead>
<tr><th>county_code</th><th>county_name</th><th>const_code</th><th>const_name</th><th>caw_code</th><th>caw_name</th><th>reg_centre_code</th><th>reg_centre_name</th><th>polling_station_code</th><th>polling_station_name_name</th><th>value</th></tr>
</thead>
<tbody>
<tr>
<td data-label="county_code">001</td>
<td data-label="county_name">mombasa</td>
<td data-label="const_code">001</td>
<td data-label="const_name">changamwe</td>
<td data-label="caw_code">0001</td>
<td data-label="caw_name">port reitz</td>
<td data-label="reg_centre_code">001</td>
<td data-label="reg_centre_name">bomu primary school</td>
<td data-label="polling_station_code">001001000100101</td>
<td data-label="polling_station_name_name">bomu primary school</td>
<td data-label="value">673.0</td>
</tr>
<tr>
<td data-label="county_code">001</td>
<td data-label="county_name">mombasa</td>
<td data-label="const_code">001</td>
<td data-label="const_name">changamwe</td>
<td data-label="caw_code">0001</td>
<td data-label="caw_name">port reitz</td>
<td data-label="reg_centre_code">001</td>
<td data-label="reg_centre_name">bomu primary school</td>
<td data-label="polling_station_code">001001000100102</td>
<td data-label="polling_station_name_name">bomu primary school</td>
<td data-label="value">673.0</td>
</tr>
<tr>
<td data-label="county_code">001</td>
<td data-label="county_name">mombasa</td>
<td data-label="const_code">001</td>
<td data-label="const_name">changamwe</td>
<td data-label="caw_code">0001</td>
<td data-label="caw_name">port reitz</td>
<td data-label="reg_centre_code">001</td>
<td data-label="reg_centre_name">bomu primary school</td>
<td data-label="polling_station_code">001001000100103</td>
<td data-label="polling_station_name_name">bomu primary school</td>
<td data-label="value">673.0</td>
</tr>
<tr>
<td data-label="county_code">001</td>
<td data-label="county_name">mombasa</td>
<td data-label="const_code">001</td>
<td data-label="const_name">changamwe</td>
<td data-label="caw_code">0001</td>
<td data-label="caw_name">port reitz</td>
<td data-label="reg_centre_code">001</td>
<td data-label="reg_centre_name">bomu primary school</td>
<td data-label="polling_station_code">001001000100104</td>
<td data-label="polling_station_name_name">bomu primary school</td>
<td data-label="value">672.0</td>
</tr>
<tr>
<td data-label="county_code">001</td>
<td data-label="county_name">mombasa</td>
<td data-label="const_code">001</td>
<td data-label="const_name">changamwe</td>
<td data-label="caw_code">0001</td>
<td data-label="caw_name">port reitz</td>
<td data-label="reg_centre_code">001</td>
<td data-label="reg_centre_name">bomu primary school</td>
<td data-label="polling_station_code">001001000100105</td>
<td data-label="polling_station_name_name">bomu primary school</td>
<td data-label="value">672.0</td>
</tr>
</tbody>
</table>
