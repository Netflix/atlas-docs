@@@ atlas-signature
<empty>
-->
TimeSeriesExpr
@@@

Filter helper that represents the count statistic of the input time series. This is a
placeholder that gets automatically replaced with `count,:stat` when used with [:filter](filter.md).
It allows filtering based on the number of non-NaN datapoints in each time series without having
to duplicate the input expression.

## Examples

Filtering series by data completeness:

@@@ atlas-example { hilite=:stat-count }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-count,50,:gt,:filter
@@@

This filters to show only time series that have more than 50 valid datapoints.

## Related Operations

* [:stat](stat.md) - Base statistics operation (stat-count represents `count,:stat`)
* [:filter](filter.md) - Filtering operation that uses stat helpers
* [:stat-avg](stat-avg.md) - Filter by average values
* [:stat-total](stat-total.md) - Filter by sum of all values

