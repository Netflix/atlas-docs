@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the negated value of the input time series.

Example:

@@@ atlas-example { hilite=:neg }
0: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=0,:neg
64: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=64,:neg
-64: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=-64,:neg
@@@
