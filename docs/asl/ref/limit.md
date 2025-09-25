@@@ atlas-signature
n: Int
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Limit the number of time series displayed to the first N series from the input expression.
The selection is based on the current sort order determined by [:sort](sort.md) and
[:order](order.md) operations. This is useful for focusing on the most important series
when dealing with large result sets.

## Parameters

* **expr**: The time series expression to limit
* **n**: Maximum number of series to display (positive integer)

## Selection Behavior

The limit operation selects the first N series based on the current ordering:

- If no sort is specified, series are ordered by legend text (alphabetical)
- If [:sort](sort.md) is used, series are ordered by the specified statistic
- The [:order](order.md) operation controls ascending vs. descending sort direction

## Examples

Limiting results to the top 3 series:

@@@ atlas-example { hilite=:limit }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,3,:limit
@@@

## Related Operations

* [:sort](sort.md) - Specify what to sort by before limiting
* [:order](order.md) - Control sort direction (ascending/descending)
* [:head](head.md) - Alias for limit (historical compatibility)
* [:by](by.md) - Group data that might need limiting