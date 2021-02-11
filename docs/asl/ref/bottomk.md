!!! warning
    This operation is still incubating and may change.

@@@ atlas-signature
TimeSeriesExpr
stat: String
k: Int
-->
TimeSeriesExpr
@@@

Since: 1.7

Restrict the output for a grouped expression to the `k` time series with the smallest value
for the specified [summary statistic](stat.md). Example of usage:

@@@ atlas-example { hilite=:bottomk }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:bottomk
@@@

In some cases it can be useful to see an aggregate summary of the other time series that were not
part of the bottom set. This can be accomplished using the `:bottomk-others-$(aggr)` operators.
Permitted aggregations are `avg`, `max`, `min`, and `sum`. For more details see:

- [:bottomk-others-avg](bottomk-others-avg.md)
- [:bottomk-others-max](bottomk-others-max.md)
- [:bottomk-others-min](bottomk-others-min.md)
- [:bottomk-others-sum](bottomk-others-sum.md)
