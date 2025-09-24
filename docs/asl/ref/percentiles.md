@@@ atlas-signature
percentiles: List
query: Query
-->
TimeSeriesExpr
@@@

Estimate percentiles for timer or distribution summary metrics. This operator extracts
percentile values from histogram data that has been published with appropriate bucket
information for approximation.

## Parameters

* **query**: A query that selects timer or distribution summary metrics
* **percentiles**: A list of percentile values to compute (e.g., `25`, `50`, `90`, `99`)

## Data Requirements

The metrics must be published with histogram information that supports percentile estimation.
If using [Spectator][spectator], use these helper classes:

* **[PercentileTimer][PercentileTimer]** - For timing measurements
* **[PercentileDistributionSummary][PercentileDistributionSummary]** - For distribution measurements

[spectator]: ../../spectator/index.md
[PercentileTimer]: https://www.javadoc.io/doc/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/histogram/PercentileTimer.html
[PercentileDistributionSummary]: https://www.javadoc.io/doc/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/histogram/PercentileDistributionSummary.html

## Variable Substitution

The percentile values can be displayed in legends using the `$percentile` variable, which
will be substituted with the actual percentile value (e.g., "25", "50", "90").

## Examples

Computing common percentiles for request latency:

@@@ atlas-example { hilite=:percentiles }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq,(,25,50,90,),:percentiles
@@@

This creates three time series showing the 25th, 50th (median), and 90th percentiles of
request latency over time.

*Since: 1.5.0 (first in 1.5.0-rc.4)*

## Related Operations

* [:max](max.md) - Maximum value (equivalent to 100th percentile)
* [:min](min.md) - Minimum value (equivalent to 0th percentile)
* [:avg](avg.md) - Average value (different from median/50th percentile)
* [:legend](legend.md) - Use `$percentile` variable for custom legend text
* [:by](by.md) - Group by dimensions before computing percentiles