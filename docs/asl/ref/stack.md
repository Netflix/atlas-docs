@@@ atlas-signature
TimeSeriesExpr
-->
StyleExpr
@@@

Change the line style to be stack. In this mode the line will be filled to the
previous stacked line on the same axis.

See the [line style examples](../../api/graph/line-styles.md) page for more information.

Example:

@@@ atlas-example { hilite=:stack }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,:stack
@@@
