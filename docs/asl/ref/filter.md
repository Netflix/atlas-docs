@@@ atlas-signature
TimeSeriesExpr
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Filters the results of a [grouped expression](by.md) by another expression. The filter expression
is a set of [signal time series](../alerting-expressions.md#signal-line) indicating if the
corresponding time series from the original expression should be shown. Simple example that
suppresses all lines:

@@@ atlas-example { hilite=:filter }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,0,:filter
@@@

Filtering is most commonly performed using the [summary statistics](stat.md) for the original
expression. For example, to show only the lines that have an average value across the query
window greater than 5k and less than 20k:

@@@ atlas-example { hilite=:filter }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:dup,avg,:stat,5e3,:gt,:over,avg,:stat,20e3,:lt,:and,:filter
@@@

There are helpers, `:stat-$(name)`, to express this common pattern more easily for filters. They
act as place holders for the specified statistic on the input time series. The filter operator
will automatically fill in the input when used so the user does not need to repeat the input
expression for the filtering criteria. See the [:stat](stat.md) operator for more details on
available statistics. For this example, [:stat-avg](stat-avg.md) would be used:

@@@ atlas-example { hilite=:filter }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-avg,5e3,:gt,:stat-avg,20e3,:lt,:and,:filter
@@@
