
@@@ atlas-signature
k: Int
stat: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Select the bottom K time series based on a summary statistic and aggregate all remaining series
into a single "others" line using sum aggregation. This provides a way to focus on the lowest
performers while showing the total contribution of all excluded series.

## Parameters

* **expr**: A grouped time series expression (typically the result of [:by](by.md))
* **stat**: Summary statistic to rank by (see [:stat](stat.md) for available options)
* **k**: Number of bottom-performing time series to display individually

## Behavior

1. **Ranking**: Evaluates all time series using the specified summary statistic
2. **Selection**: Selects the K series with the smallest statistic values
3. **Aggregation**: Combines all remaining series using `:sum` aggregation
4. **Output**: Returns K+1 time series (K individual + 1 "others" sum)

## Examples

Show bottom 2 clusters by maximum value, with sum of others:

@@@ atlas-example { hilite=:bottomk-others-sum }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:bottomk-others-sum
@@@

## Related Operations

* [:bottomk](bottomk.md) - Bottom K selection without "others" aggregation
* [:bottomk-others-avg](bottomk-others-avg.md) - Bottom K with average aggregation for others
* [:bottomk-others-max](bottomk-others-max.md) - Bottom K with maximum aggregation for others
* [:bottomk-others-min](bottomk-others-min.md) - Bottom K with minimum aggregation for others
* [:topk-others-sum](topk-others-sum.md) - Top K equivalent with sum aggregation

Since: 1.7
