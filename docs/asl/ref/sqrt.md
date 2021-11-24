@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the square root of the value from the
input time series.

@@@ atlas-example { hilite=:sqrt }
0: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=0,:sqrt
64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=64,:sqrt
-64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=-64,:sqrt
@@@