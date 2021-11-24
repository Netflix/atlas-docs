@@@ atlas-signature
q2: Query
q1: Query
-->
(q1 / q2): Query
@@@

Compute a new time series where each interval has the value `(a / b)` where `a`
and `b` are the corresponding intervals in the input time series. Note that for 
intervals where there is a `0` in the denominator, a `NaN` will be returned _unless
both_ series have a `0`. In that case a `0` will be returned.

:div    | 0.5 | 0.0 | NaN | NaN | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 1.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 2.0 | 0.0 | 0.0 | NaN | NaN |

Use the [fdiv](fdiv.md) operator to get strict floating point behavior where a `NaN` in any
series returns a `NaN` for the interval.

Example dividing a constant:

@@@ atlas-example { hilite=:div }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,1024,:div
@@@

Example dividing two series:

@@@ atlas-example { hilite=:div }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestsPerSecond,:eq,name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestsPerSecond,:eq,name,requestLatency,:eq,:div
@@@