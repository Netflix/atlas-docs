@@@ atlas-signature
n: Int
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Minimum value within a specified window. This operation can be used in
alerting expressions to find a lower bound for noisy data based on recent
samples. For example:

```
name,sps,:eq,:sum,
:dup,
5,:rolling-min
```

Missing values, `NaN`, will be ignored when computing the min. If all values
within the window are `NaN`, then `NaN` will be emitted. For example:

Input | 3,:rolling-min   |
-------|------------------|
0     | 0                |
1     | 0                |
-1    | -1               |
NaN   | -1               |
0     | -1               |
1     | 0                |
1     | 0                |
1     | 1                |
1     | 1                |
0     | 0                |

The window size, `n`, is the number of datapoints to consider including the current
value. Note that it is based on datapoints not a specific amount of time. As a result the
number of occurrences will be reduced when transitioning to a larger time frame that
causes consolidation.

Since: 1.6

@@@ atlas-example { hilite=:rolling-min }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,5,:rolling-min
@@@