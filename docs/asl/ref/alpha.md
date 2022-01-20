
@@@ atlas-signature
String
TimeSeriesExpr
-->
StyleExpr
@@@

Set the alpha value for the colors on the line. The value should be a two digit hex number
where `00` is transparent and `ff` is opague. This setting will be ignored if the
[color](color.md) setting is used for the same line.

@@@ atlas-example { hilite=:alpha }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack,40,:alpha
@@@

@@@ atlas-example { hilite=:alpha }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack,f00,:color
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack,f00,:color,40,:alpha
@@@