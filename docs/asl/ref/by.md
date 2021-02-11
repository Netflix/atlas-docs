Group by operator. There are two variants of the `:by` operator.

## Aggregation

@@@ atlas-signature
keys: List[String]
AggregationFunction
-->
DataExpr
@@@

Groups the matching time series by a set of keys and applies an aggregation to matches of the
group.

@@@ atlas-stacklang { hilite=:by }
/api/v1/graph?q=name,ssCpu,:re,(,name,),:by
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the aggregate result:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th><th>Data</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td><strong>ssCpu</strong>User</td>
    <td>alerttest</td>
    <td>i-0123</td>
    <td>[1.0, 2.0, NaN]</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>System</td>
    <td>alerttest</td>
    <td>i-0123</td>
    <td>[3.0, 4.0, 5.0]</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>User</td>
    <td>nccp</td>
    <td>i-0abc</td>
    <td>[8.0, 7.0, 6.0]</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>System</td>
    <td>nccp</td>
    <td>i-0abc</td>
    <td>[6.0, 7.0, 8.0]</td>
  </tr><tr>
    <td>numRequests</td>
    <td>nccp</td>
    <td>i-0abc</td>
    <td>[1.0, 2.0, 4.0]</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>User</td>
    <td>api</td>
    <td>i-0456</td>
    <td>[1.0, 2.0, 2.0]</td>
  </tr>
  </tbody>
</table>

The aggregation function will be applied independently for each group. In this example above
there are two matching values for the group by key `name`. This leads to a final result of:

<table>
  <thead>
  <th>Name</th><th>Data</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td><strong>ssCpuSystem</strong></td>
    <td>[9.0, 11.0, 13.0]</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>[10.0, 11.0, 8.0]</td>
  </tr>
  </tbody>
</table>

The `name` tag is included in the result set since it is used for the grouping.

## Math

@@@ atlas-signature
keys: List[String]
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Groups the time series from the input expression by a set of keys and applies an aggregation
to matches of the group. The keys used for this grouping must be a subset of keys from the
initial group by clause. Example:

@@@ atlas-example { hilite=:by }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,(,nf.cluster,nf.node,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,(,nf.cluster,nf.node,),:by,:count,(,nf.cluster,),:by
@@@
