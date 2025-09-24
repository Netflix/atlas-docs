@@@ atlas-signature
<empty>
-->
TimeSeriesExpr
@@@

Filter helper that represents the minimum statistic of the input time series. This is a
placeholder that gets automatically replaced with `min,:stat` when used with [:filter](filter.md).
It allows filtering based on the minimum value of each time series without having to duplicate
the input expression.

## Examples

Filtering series by minimum value range:

@@@ atlas-example { hilite=:stat-min }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-min,5e3,:gt,:stat-min,20e3,:lt,:and,:filter
@@@

This filters to show only time series where the minimum value is between 5,000 and 20,000.

## Related Operations

* [:stat](stat.md) - Base statistics operation (stat-min represents `min,:stat`)
* [:filter](filter.md) - Filtering operation that uses stat helpers
* [:stat-max](stat-max.md) - Filter by maximum values
* [:stat-avg](stat-avg.md) - Filter by average values

