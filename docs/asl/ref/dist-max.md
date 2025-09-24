@@@ atlas-signature
query: Query
-->
TimeSeriesExpr
@@@

Compute the maximum recorded value for timer and distribution summary metrics by aggregating
the `max` statistic. This finds the highest individual measurement value recorded within
the distributions, useful for identifying peak values and worst-case scenarios.

## Parameters

* **query**: Query for timer or distribution summary metrics

## How It Works

This operator automatically selects and aggregates the `max` statistic from timer and
distribution summary metrics:

**For Timers:**
- Aggregates the `max` statistic showing the longest recorded duration
- Useful for identifying slowest requests or operations

**For Distribution Summaries:**
- Aggregates the `max` statistic showing the largest recorded value
- Useful for identifying peak sizes or amounts

## Metric Requirements

The metrics must be instrumented using [Timer][timers] or [Distribution Summary][distribution summaries]
classes.

## Examples

Finding the maximum request latency:

@@@ atlas-example { hilite=:dist-max }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-max
@@@

Simple usage pattern:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-max
@@@

## Manual Equivalent

The `:dist-max` operator simplifies this manual query:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,statistic,max,:eq,:and,:max
@@@

## Comparison with Other Distribution Operators

| Operator | Statistic | Use Case |
|----------|-----------|----------|
| `:dist-avg` | Mean of measurements | Average performance |
| `:dist-max` | **Maximum measurement** | **Worst-case scenarios** |
| `:dist-stddev` | Standard deviation | Measurement variability |

## Related Operations

* [:dist-avg](dist-avg.md) - Average for timer/distribution metrics
* [:dist-stddev](dist-stddev.md) - Standard deviation for timer/distribution metrics
* [:max](max.md) - Maximum aggregation across time series (different scope)

## See Also

* [Timer Metrics][timers] - Instrumentation for timing measurements
* [Distribution Summary Metrics][distribution summaries] - Instrumentation for value distributions

[timers]: ../../spectator/core/meters/timer.md
[distribution summaries]: ../../spectator/core/meters/dist-summary.md