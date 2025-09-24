@@@ atlas-signature
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Create a heatmap visualization from percentile distribution data by grouping on the `percentile` tag.
This provides an intuitive way to visualize the distribution of values over time, with color intensity
representing the magnitude of values at different percentile levels.

## Parameters

* **expr**: Time series expression for percentile metrics (must contain `percentile` tag)

## Data Requirements

The metrics must be recorded as percentile timers or distribution summaries with the `percentile` tag.
If using [Spectator][spectator], use these helper classes:

* **[PercentileTimer][PercentileTimer]** - For timing measurements with percentile tracking
* **[PercentileDistributionSummary][PercentileDistributionSummary]** - For distribution measurements

## How It Works

This operator is syntactic sugar that combines grouping and heatmap visualization:

```
# These expressions are equivalent:
name,requestLatency,:eq,:percentiles-heatmap
name,requestLatency,:eq,(,percentile,),:by,:heatmap
```

The resulting heatmap shows:
- **X-axis**: Time progression
- **Y-axis**: Percentile levels (P50, P90, P95, P99, etc.)
- **Color intensity**: Magnitude of values at each percentile/time combination

## Examples

Creating a latency distribution heatmap:

@@@ atlas-example { hilite=:percentiles-heatmap }
Default: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,requestLatency,:eq,:percentiles-heatmap
@@@

## Related Operations

* [:heatmap](heatmap.md) - General heatmap visualization for any grouped data
* [:percentiles](percentiles.md) - Extract specific percentile values
* [:by](by.md) - Group data by tag keys (used internally)

## See Also

* [Heatmap API Documentation](../../api/graph/heatmap.md#percentiles) - Additional configuration options
* [Percentile Timer Pattern][PercentileTimer] - How to instrument code for percentile tracking
* [Percentile Distribution Summary Pattern][PercentileDistributionSummary] - Distribution measurement patterns

[spectator]: ../../spectator/index.md
[PercentileTimer]: ../../spectator/patterns/percentile-timer.md
[PercentileDistributionSummary]: ../../spectator/core/meters/dist-summary.md

Since: 1.8
