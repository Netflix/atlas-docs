@@@ atlas-signature
n: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Limit the number of time series to the first N series. This is an alias for the
[:limit](limit.md) operator that exists primarily for historical reasons and backwards
compatibility. It's useful for focusing on the top results when dealing with large result sets.

## Parameters

* **expr**: A time series expression that may contain multiple series
* **n**: The maximum number of time series to keep (integer)

## Examples

Limit grouped results to show only the first 2 clusters:

@@@ atlas-example { hilite=:head }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,2,:head
@@@

This takes all the series grouped by cluster and keeps only the first 2 series in the result.

## Related Operations

* [:limit](limit.md) - Equivalent operation (`:head` is an alias for `:limit`)
* [:tail](tail.md) - Take the last N series instead of the first N
* [:sort](sort.md) - Order series before limiting (often used together)
* [:by](by.md) - Group series (commonly used before limiting)
* [:top-k](top-k.md) - Select top N based on values rather than position
