Average or mean aggregation operator. There are two variants of the `:avg` operator.

## Aggregation

@@@ atlas-signature
query: Query
-->
AggregationFunction
@@@

Compute the average (arithmetic mean) of all matching time series. This is a helper method
that uses the [count](./count.md) aggregate to determine how many time series have data at
each interval and divides the sum of the values by the count. This avoids issues where some
time series are missing data at specific times, which would result in an artificially low
average.

### Parameters

* **query**: A query expression that selects the time series to aggregate

### Examples

Find the average CPU usage across all matching nodes:

@@@ atlas-stacklang { hilite=:avg }
/api/v1/graph?q=name,ssCpuUser,:eq,:avg
@@@

when matching against the sample data in the table below, the highlighted time series would be
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
the sample data above the values are `1.0`, `8.0`, and `1.0`. The arithmetic mean of these non-NaN
values is calculated (10.0/3 = 3.33). This leads to a final result of:

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
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the average of all the time series from the input expression. This variant is typically
used when you need to apply a different aggregation function for grouping first, then find the
average across the groups.

### Parameters

* **expr**: A time series expression that may contain multiple series to average

### Examples

First group by cluster using max aggregation, then find the average across all groups:

@@@ atlas-example { hilite=:avg }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:max,(,nf.cluster,),:by,:avg
@@@

## Related Operations

* [:sum](sum.md) - Sum aggregation function
* [:max](max.md) - Maximum aggregation function
* [:min](min.md) - Minimum aggregation function
* [:count](count.md) - Count aggregation function
* [:node-avg](node-avg.md) - Average normalized by instance count
* [:eureka-avg](eureka-avg.md) - Average using active instances in Eureka service discovery
* [:dist-avg](dist-avg.md) - Average for timer/distribution metrics
