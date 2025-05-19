@@@ atlas-signature
max:Double
min:Double
Query
-->
TimeSeriesExpr
@@@

Used for percentile timers or percentile distribution summaries to compute the approximate
rate of updates within a given range based on the distribution of recorded samples. For
percentile timers, the min and max will be in seconds. For percentile distribution summaries,
the min and max will match the unit of the recorded samples.

@@@ atlas-example { hilite=:sample-count }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq,0,500,:sample-count
@@@
