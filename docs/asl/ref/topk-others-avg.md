
@@@ atlas-signature
k: Int
stat: String
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Since: 1.7

Restrict the output for a grouped expression to the `k` time series with the largest value
for the specified [summary statistic](stat.md) and computes an average aggregate for the other
time series. Example of usage:

@@@ atlas-example { hilite=:topk-others-avg }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:topk-others-avg
@@@
