@@@ atlas-signature
TimeSeriesExpr
n: Integer
-->
TimeSeriesExpr
@@@

Delays the values by the window size. This is similar to the `:offset` operator
except that it can be applied to any input line instead of just changing the time
window fetched with a DataExpr. Short delays can be useful for alerting to detect
changes in slightly shifted trend lines.

Since: 1.6

@@@ atlas-example { hilite=:clamp-min }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,5,:delay
Combined: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,:dup,5,:delay
@@@