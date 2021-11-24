@@@ atlas-signature
TimeSeriesExpr
String
-->
StyleExpr
@@@

Set the line style. The value should be one of:

* `line`: this is the default, draws a normal line.
* `area`: fill in the space between the line value and 0 on the Y-axis.
* `stack`: stack the filled area on to the previous stacked lines on the same axis.
* `vspan`: non-zero datapoints will be drawn as a vertical span.

See the [line style examples](../../api/graph/line-styles.md) page for more information.

Example:

@@@ atlas-example { hilite=:ls }
Line: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,line,:ls
Area: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,area,:ls
@@@

@@@ atlas-example { hilite=:ls }
Stack: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,stack,:ls
VSpan: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,200e3,:gt,vspan,:ls
@@@
