
@@@ atlas-signature
k: Int
stat: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Select the top K time series based on a summary statistic and aggregate all remaining series
into a single "others" line using sum aggregation. This provides a way to focus on the highest
performers while still showing the total contribution of all excluded series.

## Parameters

* **expr**: A grouped time series expression (typically the result of [:by](by.md))
* **stat**: Summary statistic to rank by (see [:stat](stat.md) for available options)
* **k**: Number of top-performing time series to display individually

## Behavior

1. **Ranking**: Evaluates all time series using the specified summary statistic
2. **Selection**: Selects the K series with the largest statistic values
3. **Aggregation**: Combines all remaining series using `:sum` aggregation
4. **Output**: Returns K+1 time series (K individual + 1 "others" sum)

## Examples

Show top 2 clusters by maximum value, with sum of others:

@@@ atlas-example { hilite=:topk-others-sum }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:topk-others-sum
@@@

## Related Operations

* [:topk](topk.md) - Top K selection without "others" aggregation
* [:topk-others-avg](topk-others-avg.md) - Top K with average aggregation for others
* [:topk-others-max](topk-others-max.md) - Top K with maximum aggregation for others
* [:topk-others-min](topk-others-min.md) - Top K with minimum aggregation for others
* [:bottomk-others-sum](bottomk-others-sum.md) - Bottom K equivalent with sum aggregation

Since: 1.7
