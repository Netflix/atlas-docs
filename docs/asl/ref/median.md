@@@ atlas-signature
query: Query
-->
TimeSeriesExpr
@@@

Compute the median (50th percentile) from histogram data for timer and distribution summary metrics.
This is a convenience operator that is equivalent to `(,50,),:percentiles` but provides a clearer
semantic meaning when you specifically need the median value.

## Parameters

* **query**: Query for timer or distribution summary metrics with histogram data

## Data Requirements

The metrics must be published with histogram information that supports percentile estimation.
If using [Spectator][spectator], use these helper classes:

* **[PercentileTimer][PercentileTimer]** - For timing measurements
* **[PercentileDistributionSummary][PercentileDistributionSummary]** - For distribution measurements

## Examples

Computing median request latency:

@@@ atlas-example { hilite=:median }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq,:median
@@@

## Equivalent Expression

This operator is syntactic sugar for the 50th percentile:

```
# These expressions are equivalent:
name,requestLatency,:eq,:median
name,requestLatency,:eq,(,50,),:percentiles
```

## Related Operations

* [:percentiles](percentiles.md) - Compute arbitrary percentiles (more general case)
* [:dist-avg](dist-avg.md) - Average for timer/distribution metrics
* [:max](max.md) - Maximum values across time series
* [:min](min.md) - Minimum values across time series

## See Also

* [Percentile Timer][PercentileTimer] - Spectator class for timing with percentiles
* [Percentile Distribution Summary][PercentileDistributionSummary] - Spectator class for distributions

[spectator]: ../../spectator/index.md
[PercentileTimer]: ../../spectator/patterns/percentile-timer.md
[PercentileDistributionSummary]: ../../spectator/core/meters/dist-summary.md