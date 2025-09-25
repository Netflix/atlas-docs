@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the standard deviation across multiple time series from a grouped expression.
This statistical measure shows how much variation exists from the average value within
each group, useful for understanding data spread and identifying outliers.

## Parameters

* **expr**: A grouped time series expression (typically the result of [:by](by.md))

## Behavior

* **Group processing**: Operates on multiple time series within each group
* **Statistical calculation**: Computes population standard deviation across series
* **Variance measure**: Shows spread around the mean value for each timestamp
* **NaN handling**: Excludes NaN values from calculation

## Algorithm

For each timestamp, calculates the standard deviation across all non-NaN values
from the different time series in the group using the computational formula:

```
σ = √((N * sum(x²) - sum(x)²) / N²)
```

Where:

- `N` = number of non-NaN values at that timestamp
- `sum(x)` = sum of all time series values at that timestamp
- `sum(x²)` = sum of squared time series values at that timestamp

This formula is mathematically equivalent to the standard definition but is computed
using aggregated statistics rather than storing individual samples.

## Examples

Computing standard deviation for request rates grouped by cluster:

@@@ atlas-example { hilite=:stddev }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by,:stddev
@@@

## Alternative for Distribution Metrics

For timer and distribution summary metrics, use [:dist-stddev](dist-stddev.md) instead,
which calculates standard deviation from the recorded samples rather than across multiple
time series.

## Related Operations

* [:dist-stddev](dist-stddev.md) - Standard deviation for timer/distribution metrics (recommended for those types)
* [:avg](avg.md) - Mean value across time series (center measure)
* [:max](max.md) / [:min](min.md) - Range measures (spread indicators)
* [:by](by.md) - Group time series for statistical analysis
* [:sum](sum.md) - Total aggregation across series

Since: 1.6