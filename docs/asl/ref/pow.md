@@@ atlas-signature
TimeSeriesExpr
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a power b)` where `a`
and `b` are the corresponding intervals in the input time series.

Examples:

@@@ atlas-example { hilite=:pow }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,42,:pow
@@@

@@@ atlas-example { hilite=:pow }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:pow
@@@