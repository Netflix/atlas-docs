@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the standard deviation for the results of a [group by](by.md). If the
underlying data is for a timer or distribution summary, then [dist-stddev](dist-stddev.md)
is likely a better choice.

Since: 1.6

Example:

@@@ atlas-example { hilite=:stddev }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by,:stddev
@@@