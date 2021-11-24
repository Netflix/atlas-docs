@@@ atlas-signature
TimeSeriesExpr
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a addNaN b)` where `a`
and `b` are the corresponding intervals in the input time series. Sample:

:add    | 3.0 | 0.0 | 1.0 | 1.0 | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 1.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 2.0 | 0.0 | 0.0 | NaN | NaN |

Use the [fadd](fadd.md) operator to get strict floating point behavior.

Examples

Example adding a constant:

@@@ atlas-example { hilite=:add }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3,:add
@@@

Example adding two series:

@@@ atlas-example { hilite=:add }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:add
@@@
