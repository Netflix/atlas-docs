Average or mean aggregation operator. There are two variants of the `:avg` operator.

## Aggregation

@@@ atlas-signature
Query
-->
AggregationFunction
@@@

A helper method that computes the average or mean from one or more time series using the 
[count](count) aggregate to determine how many time series are present at a time and 
dividing the sum of the values by the count. This avoids issues where one or time series
are missing data at a specific time resulting in an artificially low average. E.g. the 
expression:

@@@ atlas-stacklang
/api/v1/graph?q=name,ssCpuUser,:eq,:dup,:dup,:sum,:swap,:count,:div,avg,:named-rewrite
@@@

becomes:

@@@ atlas-stacklang { hilite=:avg }
/api/v1/graph?q=name,ssCpuUser,:eq,:avg
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the aggregate result:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th><th>Data</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>alerttest</td>
    <td>i-0123</td>
    <td>[1.0, 2.0, NaN]</td>
  </tr><tr>
    <td>ssCpuSystem</td>
    <td>alerttest</td>
    <td>i-0123</td>
    <td>[3.0, 4.0, 5.0]</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>nccp</td>
    <td>i-0abc</td>
    <td>[8.0, 7.0, 6.0]</td>
  </tr><tr>
    <td>ssCpuSystem</td>
    <td>nccp</td>
    <td>i-0abc</td>
    <td>[6.0, 7.0, 8.0]</td>
  </tr><tr>
    <td>numRequests</td>
    <td>nccp</td>
    <td>i-0abc</td>
    <td>[1.0, 2.0, 4.0]</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>api</td>
    <td>i-0456</td>
    <td>[1.0, 2.0, 2.0]</td>
  </tr>
  </tbody>
</table>

The values from the corresponding intervals will be aggregated. For the first interval using
the sample data above the values are `1.0`, `8.0`, and `1.0`. Each value other than `NaN`
contributes one to the average. This leads to a final result of:

<table>
  <thead>
  <th>Name</th><th>Data</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>[3.33, 3.66, 4.0]</td>
  </tr>
  </tbody>
</table>

The only tags for the aggregated result are those that are matched exactly ([:eq](eq.md) clause)
as part of the choosing criteria or are included in a [group by](by.md).

## Math

@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the average of all the time series from the input expression. This is typically used when
there is a need to use some other aggregation for the grouping. Example:

@@@ atlas-example { hilite=:avg }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:max,(,nf.cluster,),:by,:avg
@@@
