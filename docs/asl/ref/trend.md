@@@ atlas-signature
window: Duration
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

!!! Warning
    **Deprecated:** Use [:rolling-mean](rolling-mean.md) instead.

Computes a moving average over the input window. Until there is at least one sample
for the whole window it will emit `NaN`. If the input line has `NaN` values, then they
will be treated as zeros. Example:

Input | 2m,:trend | 5m,:trend |
------|-----------|-----------|
0     |  NaN      | NaN       |
1     |  0.5      | NaN       |
-1    |  0.0      | NaN       |
NaN   |   -0.5    | NaN       |
0     |  0.0      | 0.0       |
1     |  0.5      | 0.2       |
2     |  1.5      | 0.4       |
1     |  1.5      | 0.8       |
1     |  1.0      | 1.0       |
0     |  0.5      | 1.0       |

The window size is specified as a range of time. If the window size is not evenly
divisible by the [step size](../../concepts/time-series.md#step-size), then the window size will be rounded
down. So a 5m window with a 2m step would result in a 4m window with two datapoints
per average. A step size larger than the window will result in the trend being a no-op.

Examples:

@@@ atlas-example { hilite=:trend }
5 Minutes: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,PT5M,:trend
20 Minutes: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,20m,:trend
@@@