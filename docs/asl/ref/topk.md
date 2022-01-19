
@@@ atlas-signature
k: Int
stat: String
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Since: 1.7

Restrict the output for a grouped expression to the `k` time series with the largest value
for the specified [summary statistic](stat.md). Example of usage:

@@@ atlas-example { hilite=:topk }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:topk
@@@

In some cases it can be useful to see an aggregate summary of the other time series that were not
part of the top set. This can be accomplished using the `:topk-others-$(aggr)` operators.
For more details see:

- [:topk-others-avg](topk-others-avg.md)
- [:topk-others-max](topk-others-max.md)
- [:topk-others-min](topk-others-min.md)
- [:topk-others-sum](topk-others-sum.md)
