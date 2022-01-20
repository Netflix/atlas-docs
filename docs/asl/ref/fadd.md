@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 + ts2): TimeSeriesExpr
@@@

Floating point addition operator. Compute a new time series where each interval has the
value `(a + b)` where `a` and `b` are the corresponding intervals in the input time
series.

:fadd   | 3.0 | 0.0 | 1.0 | NaN | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 1.0 | 0.0 | 0.0 | NaN | NaN |

Note in many cases `NaN` will appear in data, e.g., if a node was brought up and started
reporting in the middle of the time window for the graph. This can lead to confusing
behavior if added to a line that does have data as the result will be `NaN`. Use the
[add](add.md) operator to treat `NaN` values as zero for combining with other time
series.

Example adding a constant:

@@@ atlas-example { hilite=:fadd }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3,:fadd
@@@

Example adding two series:

@@@ atlas-example { hilite=:fadd }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:fadd
@@@