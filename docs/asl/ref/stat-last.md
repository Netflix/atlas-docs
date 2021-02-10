@@@ atlas-signature
-->
TimeSeriesExpr
@@@

Represents the `last,:stat` of the input time series when used with the [filter](filter.md)
operation. The filter operator will automatically fill in the input when used so the user
does not need to repeat the input expression for the filtering criteria.

Example of restricting to lines where the last value is greater than 5k and less than 20k:

@@@ atlas-example { hilite=:stat-last }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-last,5e3,:gt,:stat-last,20e3,:lt,:and,:filter
@@@

