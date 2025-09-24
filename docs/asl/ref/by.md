Group by operator. There are two variants of the `:by` operator.

## Aggregation

@@@ atlas-signature
keys: List[String]
aggregationFunc: AggregationFunction
-->
DataExpr
@@@

Groups the matching time series by a set of tag keys and applies an aggregation function to
each group. This allows you to aggregate data separately for different values of the specified
keys, rather than aggregating everything together.

### Parameters

* **aggregationFunc**: An aggregation function (like `:sum`, `:max`, `:count`) that will be applied to each group
* **keys**: A list of tag key names to group by (e.g., `name`, `nf.app`)

### Examples

Group CPU metrics by name and apply sum aggregation to each group:

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
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Groups the time series from the input expression by a set of tag keys and applies an aggregation
to each group. The keys used for this grouping must be a subset of keys from the initial grouping
operation. This variant allows for hierarchical grouping where you first group by a broader set
of keys, then regroup by a subset.

### Parameters

* **expr**: A time series expression that contains grouped data
* **keys**: A list of tag key names to group by (must be subset of original grouping keys)

### Examples

First group by cluster and node, then regroup by cluster only (counting nodes per cluster):

@@@ atlas-example { hilite=:by }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,(,nf.cluster,nf.node,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,(,nf.cluster,nf.node,),:by,:count,(,nf.cluster,),:by
@@@

## Related Operations

* [:sum](sum.md) - Sum aggregation function (commonly used with grouping)
* [:max](max.md) - Maximum aggregation function
* [:min](min.md) - Minimum aggregation function
* [:avg](avg.md) - Average aggregation function
* [:count](count.md) - Count aggregation function
* [:eq](eq.md) - Equality filter (creates exact tag matches that preserve grouping)
