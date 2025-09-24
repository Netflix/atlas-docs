
@@@ atlas-signature
k: Int
stat: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Select the top K time series based on a summary statistic. This operation keeps only the K
time series with the largest values for the specified statistic, effectively filtering out
all but the highest-performing series according to the chosen criteria.

## Parameters

* **expr**: The grouped time series expression to select from
* **stat**: The [summary statistic](stat.md) to rank by (`max`, `min`, `avg`, `count`, `total`, `last`)
* **k**: Number of highest-ranking series to keep (positive integer)

## Behavior

1. **Statistical evaluation**: Computes the specified statistic for each time series over the query window
2. **Ranking**: Sorts all series by the statistic values in descending order (largest first)
3. **Selection**: Keeps only the first K series (those with the largest statistic values)
4. **Output**: Returns the selected time series with their original data, not the statistic values

## Examples

Selecting the 2 clusters with the highest maximum values:

@@@ atlas-example { hilite=:topk }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,max,2,:topk
@@@

## Others Aggregation

For including aggregate summaries of the excluded series, use the `:topk-others-*` operators:

* [:topk-others-avg](topk-others-avg.md) - Include average of excluded series
* [:topk-others-max](topk-others-max.md) - Include maximum of excluded series
* [:topk-others-min](topk-others-min.md) - Include minimum of excluded series
* [:topk-others-sum](topk-others-sum.md) - Include sum of excluded series

## Related Operations

* [:bottomk](bottomk.md) - Select bottom K time series (smallest values)
* [:limit](limit.md) - Limit results after sorting (different ranking criteria)
* [:sort](sort.md) - Sort time series by statistics
* [:filter](filter.md) - Filter based on statistical criteria
* [:stat](stat.md) - Compute statistics used for ranking

Since: 1.7
