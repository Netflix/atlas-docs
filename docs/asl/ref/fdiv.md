@@@ atlas-signature
q2: Query
q1: Query
-->
(q1 * q2): Query
@@@

Compute a new time series where each interval has the value `(a productNaN b)` where `a`
and `b` are the corresponding intervals in the input time series. A `NaN` present
in any series will cause the result for the interval to be `NaN`. Sample:

:add    | 6.0 | 0.0 | 5.0 | NaN | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 3.0 | 4.0 | 5.0 | NaN | NaN |

Example subtracting a constant:

@@@ atlas-example { hilite=:fmul }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,1024,:fmul
@@@

Example adding two series:

@@@ atlas-example { hilite=:fmul }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestsPerSecond,:eq,name,sps,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestsPerSecond,:eq,name,sps,:eq,:fmul
@@@