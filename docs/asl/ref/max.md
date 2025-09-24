Max aggregation operator. There are two variants of the `:max` operator.

## Aggregation

@@@ atlas-signature
query: Query
-->
AggregationFunction
@@@

Select the maximum value for corresponding times across all matching time series.

### Parameters

* **query**: A query expression that selects the time series to aggregate

### Examples

Find the maximum CPU usage across all matching nodes:

@@@ atlas-stacklang { hilite=:max }
/api/v1/graph?q=name,ssCpuUser,:eq,:max
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
the sample data above the values are `1.0`, `8.0`, and `1.0`. The maximum of these non-NaN
values is selected. This leads to a final result of:

<table>
  <thead>
  <th>Name</th><th>Data</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>[8.0, 7.0, 6.0]</td>
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

Select the maximum value for corresponding times across the time series resulting from the
input expression. This variant is typically used when you need to apply a different aggregation
function for grouping first, then find the maximum across the groups.

### Parameters

* **expr**: A time series expression that may contain multiple series to find the maximum across

### Examples

First group by cluster using sum aggregation, then find the maximum across all groups:

@@@ atlas-example { hilite=:max }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,(,nf.cluster,),:by,:max
@@@

## Related Operations

* [:min](min.md) - Minimum aggregation function
* [:sum](sum.md) - Sum aggregation function
* [:avg](avg.md) - Average aggregation function
* [:count](count.md) - Count aggregation function
* [:by](by.md) - Group time series by tag values before aggregating
