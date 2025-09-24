@@@ atlas-signature
<empty>
-->
TimeSeriesExpr
@@@

Filter helper that represents the total (sum) statistic of the input time series. This is a
placeholder that gets automatically replaced with `total,:stat` when used with [:filter](filter.md).
It allows filtering based on the sum of all datapoints in each time series without having to
duplicate the input expression.

## Examples

Filtering series by cumulative volume:

@@@ atlas-example { hilite=:stat-total }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-total,1e6,:gt,:stat-total,4e6,:lt,:and,:filter
@@@

This filters to show only time series where the sum of all datapoints is between 1,000,000 and 4,000,000.

## Related Operations

* [:stat](stat.md) - Base statistics operation (stat-total represents `total,:stat`)
* [:filter](filter.md) - Filtering operation that uses stat helpers
* [:stat-count](stat-count.md) - Filter by number of datapoints
* [:stat-avg](stat-avg.md) - Filter by average values

