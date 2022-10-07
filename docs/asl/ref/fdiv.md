@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 / ts2): TimeSeriesExpr
@@@

Floating point division operator. Compute a new time series where each interval has the
value `(a / b)` where `a` and `b` are the corresponding intervals in the input time
series.

:fdiv   | 2.0 | NaN | Inf | NaN | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 1.0 | 0.0 | 0.0 | NaN | NaN |

Note in many cases `NaN` will appear in data, e.g., if a node was brought up and started
reporting in the middle of the time window for the graph. Zero divided by zero can also
occur due to lack of activity in some windows. Unless you really need strict floating
point behavior, use the [div](div.md) operator to get behavior more appropriate for
graphs.

Example dividing a constant:

@@@ atlas-example { hilite=:fdiv }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,1024,:fdiv
@@@

Example dividing two series:

@@@ atlas-example { hilite=:fdiv }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:fdiv
@@@