@@@ atlas-signature
-->
TimeSeriesExpr
@@@

Represents the `count,:stat` of the input time series when used with the [filter](filter.md)
operation. The filter operator will automatically fill in the input when used so the user
does not need to repeat the input expression for the filtering criteria.

Example of restricting to lines where the count value is greater than 50:

@@@ atlas-example { hilite=:stat-count }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-count,50,:gt,:filter
@@@

