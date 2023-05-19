@@@ atlas-signature
TimeSeriesExpr
-->
StyleExpr
@@@

Since 1.8.

Group the metric by the `percentiles` tag and plot the data as a heatmap. Requires 
that the metric to be recorded as a [percentile](../../spectator/patterns/percentile-timer.md).

See [heatmap](../../api/graph/heatmap.md#percentiles) for more information.

Shorthand equivalent of writing `name,requestLatency,:eq,(,percentile,),:by,:heatmap`

Example:

@@@ atlas-example { hilite=:percentiles-heatmap }
Default: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,requestLatency,:eq,:percentiles-heatmap
@@@
