@@@ atlas-signature
<empty>
-->
TimeSeriesExpr
@@@

Filter helper that represents the average statistic of the input time series. This is a
placeholder that gets automatically replaced with `avg,:stat` when used with [:filter](filter.md).
It allows filtering based on the average value of each time series without having to duplicate
the input expression.

## Examples

Filtering series by average value range:

@@@ atlas-example { hilite=:stat-avg }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-avg,5e3,:gt,:stat-avg,20e3,:lt,:and,:filter
@@@

This filters to show only time series where the average value is between 5,000 and 20,000.

## Related Operations

* [:stat](stat.md) - Base statistics operation (stat-avg represents `avg,:stat`)
* [:filter](filter.md) - Filtering operation that uses stat helpers
* [:stat-max](stat-max.md) - Filter by maximum values
* [:stat-min](stat-min.md) - Filter by minimum values

