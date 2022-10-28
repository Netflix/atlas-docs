@@@ atlas-signature
n: Int
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Sum of the values within a specified window.

Input | 3,:rolling-sum    |
-------|---------------------|
0     | 0.0                 |
1     | 1.0                 |
-1    | 0.0                 |
NaN   | 0.0                 |
NaN   | -1.0                |
NaN   | NaN                 |
1     | 1.0                 |
1     | 2.0                 |
1     | 3.0                 |
0     | 2.0                 |

The window size, `n`, is the number of datapoints to consider including the current
value. Note that it is based on datapoints, not a specific amount of time.
As a result the number of occurrences will be reduced when transitioning to a larger time
frame that causes consolidation.

Since: 1.6

@@@ atlas-example { hilite=:rolling-sum }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,5,:rolling-sum
@@@