@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Opposite of [:integral](integral.md). Computes the rate of change per step of the
input time series.

@@@ atlas-example { hilite=:derivative }
Derivative: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:derivative
Integral: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:integral
Integral Then Derivative: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:integral,:derivative
@@@