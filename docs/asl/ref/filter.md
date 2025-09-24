@@@ atlas-signature
condition: TimeSeriesExpr
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Filter time series from a grouped expression based on a condition. The condition must evaluate
to signal time series (boolean-like values) that determine which time series from the original
expression should be included in the output. This is essential for focusing on specific subsets
of data that meet certain criteria.

## Parameters

* **expr**: The grouped time series expression to filter (typically from [:by](by.md))
* **condition**: Signal time series indicating which series to keep (non-zero = keep, zero = exclude)

## How It Works

1. **Evaluation**: The condition expression is evaluated for each time series in the input
2. **Signal interpretation**: Non-zero values in the condition signal mean "keep this series"
3. **Filtering**: Only time series where the condition evaluates to non-zero are included
4. **Output**: Returns the filtered subset with their original data

## Examples

Suppress all time series (condition always evaluates to 0):

@@@ atlas-example { hilite=:filter }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,0,:filter
@@@

Manual filtering using statistics (verbose approach) - show only lines with average value between 5k and 20k:

@@@ atlas-example { hilite=:filter }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:dup,avg,:stat,5e3,:gt,:over,avg,:stat,20e3,:lt,:and,:filter
@@@

Simplified filtering using stat helpers (recommended approach) - same filter condition as above:

@@@ atlas-example { hilite=:filter }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:stat-avg,5e3,:gt,:stat-avg,20e3,:lt,:and,:filter
@@@

## Stat Helper Integration

The most common filtering pattern uses [summary statistics](stat.md) with helper operators that
automatically substitute the input expression:

* **[:stat-avg](stat-avg.md)** - Filter by average values
* **[:stat-max](stat-max.md)** - Filter by maximum values
* **[:stat-min](stat-min.md)** - Filter by minimum values
* **[:stat-count](stat-count.md)** - Filter by datapoint count
* **[:stat-total](stat-total.md)** - Filter by sum of values
* **[:stat-last](stat-last.md)** - Filter by most recent values

These helpers eliminate the need to manually duplicate the input expression in filtering conditions.

## Related Operations

* [:by](by.md) - Group data for filtering (often used together)
* [:topk](topk.md) / [:bottomk](bottomk.md) - Alternative selection methods
* [:stat](stat.md) - Base statistics for filtering criteria
* [:and](and.md) / [:or](or.md) - Combine multiple filtering conditions
