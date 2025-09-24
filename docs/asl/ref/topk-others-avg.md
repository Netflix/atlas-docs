
@@@ atlas-signature
k: Int
stat: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Select the top K time series based on a summary statistic and include an average aggregate
of all other excluded series. This combines [:topk](topk.md) with an additional "others"
series showing the average of the time series that were not in the top K.

## Parameters

* **expr**: The grouped time series expression to select from
* **stat**: The [summary statistic](stat.md) to rank by (`max`, `min`, `avg`, `count`, `total`, `last`)
* **k**: Number of highest-ranking series to keep (positive integer)

## Behavior

1. **Selection**: Performs the same selection as [:topk](topk.md)
2. **Aggregation**: Computes the average of all remaining (excluded) time series
3. **Output**: Returns the top K series plus one additional "others" series

## Examples

Top 2 clusters with average of the rest:

@@@ atlas-example { hilite=:topk-others-avg }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:topk-others-avg
@@@

## Related Operations

* [:topk](topk.md) - Top K selection without others aggregation
* [:topk-others-max](topk-others-max.md) - Top K with maximum of others
* [:topk-others-min](topk-others-min.md) - Top K with minimum of others
* [:topk-others-sum](topk-others-sum.md) - Top K with sum of others
* [:bottomk-others-avg](bottomk-others-avg.md) - Bottom K with average of others

Since: 1.7
