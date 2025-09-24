@@@ atlas-signature
sortKey: String
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Sort time series results for display in the legend and affect stacking order. The sort can be
based on summary statistics computed over the time window or by the legend text. This operation
primarily affects visual presentation - the order in which series appear in legends and the
stacking order for area charts.

## Parameters

* **expr**: The time series expression to sort
* **sortKey**: What to sort by - either a [summary statistic](stat.md) name or `legend` for text

## Sort Criteria

* **Summary statistics**: `max`, `min`, `avg`, `count`, `total`, `last`, etc.
* **Legend text**: Use `legend` to sort alphabetically by the series legend text
* **Default behavior**: If no sort key is specified, defaults to sorting by legend text

The sort direction is ascending by default. Use [:order](order.md) to specify descending order.

## Examples

Sorting by maximum value (highest values first when combined with `desc` order):

@@@ atlas-example { hilite=:sort }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,max,:sort
@@@

## Related Operations

* [:order](order.md) - Control sort direction (ascending/descending)
* [:limit](limit.md) - Restrict results after sorting (e.g., top N)
* [:by](by.md) - Group data that can then be sorted
* [Summary statistics](stat.md) - Available sort criteria

Since: 1.5