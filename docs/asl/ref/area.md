@@@ atlas-signature
TimeSeriesExpr
-->
StyleExpr
@@@

Change the line style to be area. In this mode the line will be filled to 0 on the
Y-axis.

See the [line style examples](../../api/graph/line-styles.md) page for more information.

@@@ atlas-example { hilite=:area }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,:area
@@@
