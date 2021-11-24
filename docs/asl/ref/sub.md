@@@ atlas-signature
TimeSeriesExpr
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a subtractNaN b)` where `a`
and `b` are the corresponding intervals in the input time series.

:sub    | 1.0 | 0.0 | 1.0 | 1.0 | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 1.0 | 0.0 | 0.0 | NaN | NaN |

Use the [fsub](fsub.md) operator to get strict floating point behavior.

Example subtracting a constant:

@@@ atlas-example { hilite=:sub }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3,:sub
@@@

Example subtracting two series:

@@@ atlas-example { hilite=:sub }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:sub
@@@