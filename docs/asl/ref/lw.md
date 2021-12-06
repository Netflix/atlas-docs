@@@ atlas-signature
TimeSeriesExpr
String
-->
StyleExpr
@@@

The width of the stroke used when drawing the line.

Example:

@@@ atlas-example { hilite=:lw }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,2,:lw
@@@
