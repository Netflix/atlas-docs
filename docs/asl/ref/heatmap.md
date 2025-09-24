@@@ atlas-signature
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Plot the time series as a heatmap visualization. This is useful for displaying multiple time series
with high cardinality where individual lines would be difficult to distinguish. The heatmap uses
color intensity to represent the magnitude of values across time and series.

Heatmaps work best with data that has been grouped by a dimension that produces many series, such
as grouping by node.

## Parameters

* **expr**: A time series expression, typically the result of a group-by operation that produces multiple series

## Examples

Basic heatmap showing multiple series grouped by cluster:

@@@ atlas-example { hilite=:heatmap }
Default: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,:heatmap
@@@

## Related Operations

* [:by](by.md) - Group data to create multiple series suitable for heatmap display
* [:percentiles-heatmap](percentiles-heatmap.md) - Create heatmap from percentile distribution data

## See Also

See [heatmap API documentation](../../api/graph/heatmap.md) for detailed configuration options
and color mapping behavior.

Since: 1.8
