
@@@ atlas-signature
k: Int
stat: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Select the bottom K time series based on a summary statistic and include an average aggregate
of all other excluded series. This combines [:bottomk](bottomk.md) with an additional "others"
series showing the average of the time series that were not in the bottom K.

## Parameters

* **expr**: The grouped time series expression to select from
* **stat**: The [summary statistic](stat.md) to rank by (`max`, `min`, `avg`, `count`, `total`, `last`)
* **k**: Number of lowest-ranking series to keep (positive integer)

## Behavior

1. **Selection**: Performs the same selection as [:bottomk](bottomk.md)
2. **Aggregation**: Computes the average of all remaining (excluded) time series
3. **Output**: Returns the bottom K series plus one additional "others" series

## Examples

Bottom 2 clusters with average of the rest:

@@@ atlas-example { hilite=:bottomk-others-avg }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:bottomk-others-avg
@@@

## Related Operations

* [:bottomk](bottomk.md) - Bottom K selection without others aggregation
* [:bottomk-others-max](bottomk-others-max.md) - Bottom K with maximum of others
* [:bottomk-others-min](bottomk-others-min.md) - Bottom K with minimum of others
* [:bottomk-others-sum](bottomk-others-sum.md) - Bottom K with sum of others
* [:topk-others-avg](topk-others-avg.md) - Top K with average of others

Since: 1.7
