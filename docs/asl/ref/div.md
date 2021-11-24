@@@ atlas-signature
q2: Query
q1: Query
-->
(q1 / q2): Query
@@@

Compute a new time series where each interval has the value `(a / b)` where `a`
and `b` are the corresponding intervals in the input time series. If `a` and `b` are 0,
then 0 will be returned for the interval. If only `b` is 0, then NaN will be returned as
the value for the interval. Sample data:

:div    | 0.5 | 0.0 | NaN | NaN | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 1.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 2.0 | 0.0 | 0.0 | NaN | NaN |

Use the [fdiv](fdiv.md) operator to get strict floating point behavior.

Example dividing a constant:

@@@ atlas-example { hilite=:div }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,42
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,42,:div
@@@

Example adding two series:

@@@ atlas-example { hilite=:div }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:div
@@@