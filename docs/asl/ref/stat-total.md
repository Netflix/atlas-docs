@@@ atlas-signature
-->
TimeSeriesExpr
@@@

Represents the `total,:stat` of the input time series when used with the [filter](filter.md)
operation. The filter operator will automatically fill in the input when used so the user
does not need to repeat the input expression for the filtering criteria.

Example of restricting to lines where the sum of all data points for the line is greater than
1M and less than 4M:

@@@ atlas-example { hilite=:stat-total }
Input: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
Output: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-total,1e6,:gt,:stat-total,4e6,:lt,:and,:filter
@@@

