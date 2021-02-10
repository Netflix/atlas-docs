@@@ atlas-signature
TimeSeriesExpr
stat: String
k: Int
-->
TimeSeriesExpr
@@@

Restrict the output for a grouped expression to the `k` time series with the largest value
for the specified [summary statistic](stat.md) and computes a max aggregate for the other
time series. Example of usage:

@@@ atlas-example { hilite=:topk-others-max }
Input: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
Output: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:topk-others-max
@@@
