@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Sum the values across the evaluation context. This is typically used to approximate the
distinct number of events that occurred. If the input is non-negative, then each datapoint
for the output line will represent the area under the input line from the start of the
graph to the time for that datapoint. Missing values, `NaN`, will be treated as zeroes.
For example:

Input | :integral |
-------|-----------|
0     | 0         |
1     | 1         |
-1    | 0         |
NaN   | 0         |
0     | 0         |
1     | 1         |
2     | 3         |
1     | 4         |
1     | 5         |
0     | 5         |

For a [counter](http://netflix.github.io/spectator/en/latest/intro/counter/), each data
point represents the average rate per second over the step interval. To compute the total
amount incremented, the value first needs to be converted to a rate per step interval.
This conversion can be performed using the [:per-step](per-step.md) operation.

Examples: 

@@@ atlas-example { hilite=:integral }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:integral
@@@

@@@ atlas-example { hilite=:integral }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,:per-step
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,:per-step,:integral
@@@