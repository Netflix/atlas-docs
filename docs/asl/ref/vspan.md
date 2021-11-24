@@@ atlas-signature
TimeSeriesExpr
-->
StyleExpr
@@@

Change the line style to be a vertical span. In this mode any non-zero datapoints on the
line will be shown as a span. This is frequently used to visualize when an alert would
have fired.

See the [line style examples](../../api/graph/line-styles.md) page for more information.

Example:

@@@ atlas-example { hilite=:vspan }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:dup,20e3,:gt
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:dup,20e3,:gt,:vspan
@@@
