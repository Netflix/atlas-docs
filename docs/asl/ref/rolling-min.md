@@@ atlas-signature
TimeSeriesExpr
n: Integer
-->
TimeSeriesExpr
@@@

Mean of the values within a specified window. The mean will only be emitted
if there are at least a minimum number of actual values (not `NaN`) within
the window. Otherwise `NaN` will be emitted for that time period.

Input | 3,2,:rolling-mean   |
-------|---------------------|
0     | NaN                 |
1     | 0.5                 |
-1    | 0.0                 |
NaN   | 0.0                 |
NaN   | NaN                 |
0     | NaN                 |
1     | 0.5                 |
1     | 0.667               |
1     | 1                   |
0     | 0.667               |

The window size, `n`, is the number of datapoints to consider including the current
value. There must be at least `minNumValues` non-NaN values within that window before
it will emit a mean. Note that it is based on datapoints, not a specific amount of time.
As a result the number of occurrences will be reduced when transitioning to a larger time
frame that causes consolidation.

Since: 1.6

@@@ atlas-example { hilite=:rolling-mean }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,5
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,5,3,:rolling-mean
@@@
