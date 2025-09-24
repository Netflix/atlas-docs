
@@@ atlas-signature
k: Int
stat: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Select the bottom K time series based on a summary statistic and aggregate all remaining series
into a single "others" line using maximum aggregation. This provides a way to focus on the lowest
performers while showing the peak value among all excluded series.

## Parameters

* **expr**: A grouped time series expression (typically the result of [:by](by.md))
* **stat**: Summary statistic to rank by (see [:stat](stat.md) for available options)
* **k**: Number of bottom-performing time series to display individually

## Behavior

1. **Ranking**: Evaluates all time series using the specified summary statistic
2. **Selection**: Selects the K series with the smallest statistic values
3. **Aggregation**: Combines all remaining series using `:max` aggregation
4. **Output**: Returns K+1 time series (K individual + 1 "others" maximum)

## Examples

Show bottom 2 clusters by maximum value, with maximum of others:

@@@ atlas-example { hilite=:bottomk-others-max }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:bottomk-others-max
@@@

## Related Operations

* [:bottomk](bottomk.md) - Bottom K selection without "others" aggregation
* [:bottomk-others-avg](bottomk-others-avg.md) - Bottom K with average aggregation for others
* [:bottomk-others-min](bottomk-others-min.md) - Bottom K with minimum aggregation for others
* [:bottomk-others-sum](bottomk-others-sum.md) - Bottom K with sum aggregation for others
* [:topk-others-max](topk-others-max.md) - Top K equivalent with maximum aggregation

Since: 1.7
