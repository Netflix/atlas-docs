@@@ atlas-signature
max: Double
min: Double
query: Query
-->
TimeSeriesExpr
@@@

Compute the approximate rate of samples that fall within a specified range for timer and
distribution summary metrics. This operator analyzes the distribution of recorded samples
to estimate how many measurements per unit time fall between the minimum and maximum values.

## Parameters

* **query**: Query for timer or distribution summary metrics with histogram data
* **min**: Lower bound of the range (inclusive)
* **max**: Upper bound of the range (exclusive)

## Units

The min and max values must be specified in the appropriate units for the metric type:

* **Percentile Timers**: Values in seconds (e.g., `0.1` for 100ms, `1.0` for 1 second)
* **Percentile Distribution Summaries**: Values in the same unit as the recorded samples

## How It Works

This operator uses the histogram data recorded by percentile timers and distribution summaries
to estimate the rate of samples falling within the specified range. It provides an approximation
based on the distribution buckets rather than exact sample counts.

## Data Requirements

The metrics must be instrumented using percentile timers or distribution summaries that
collect histogram information:

* **[PercentileTimer](../../spectator/patterns/percentile-timer.md)** - For timing measurements
* **[PercentileDistributionSummary](../../spectator/patterns/percentile-dist-summary.md)** - For distribution measurements

## Examples

Count samples in the 0-500ms latency range:

@@@ atlas-example { hilite=:sample-count }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq,0,0.5,:sample-count
@@@

Count high-latency requests (above 1 second):

```asl
name,requestLatency,:eq,1,10,:sample-count
```

## Related Operations

* [:percentiles](percentiles.md) - Extract specific percentile values from same data
* [:median](median.md) - Get 50th percentile value
* [:dist-avg](dist-avg.md) - Average for timer/distribution metrics

## See Also

* [Percentile Timer Pattern](../../spectator/patterns/percentile-timer.md) - Instrumentation for timing with histograms
* [Percentile Distribution Summary Pattern](../../spectator/patterns/percentile-dist-summary.md) - Distribution measurement patterns
