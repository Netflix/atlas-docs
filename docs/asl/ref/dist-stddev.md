@@@ atlas-signature
query: Query
-->
TimeSeriesExpr
@@@

Compute the standard deviation for timer and distribution summary metrics based on the
recorded samples. This calculates the standard deviation of the individual measurements
that were recorded, showing the variability of the actual sample values.

## Parameters

* **query**: Query for timer or distribution summary metrics

## How It Works

This operator automatically combines the appropriate distribution statistics to calculate
per-measurement standard deviation using the mathematical formula:

```
σ = √((totalOfSquares × count - totalTime²) / count²)
```

**For Timers:**
- Uses `totalTime`, `totalOfSquares`, and `count` statistics
- Calculates standard deviation of individual request durations

**For Distribution Summaries:**
- Uses `totalAmount`, `totalOfSquares`, and `count` statistics
- Calculates standard deviation of individual measurement values

## Metric Requirements

The metrics must be instrumented using [Timer][timers] or [Distribution Summary][distribution summaries]
classes.

## Examples

Computing standard deviation of request latency measurements:

@@@ atlas-example { hilite=:dist-stddev }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-stddev
@@@

Simple usage pattern:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-stddev
@@@

## Manual Equivalent

The `:dist-stddev` operator simplifies this complex manual calculation:

@@@ atlas-stacklang
/api/v1/graph?q=statistic,count,:eq,:sum,statistic,totalOfSquares,:eq,:sum,:mul,statistic,totalTime,:eq,:sum,:dup,:mul,:sub,statistic,count,:eq,:sum,:dup,:mul,:div,:sqrt,nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:cq
@@@

## Comparison with Other Standard Deviations

| Operator | Measures | Use Case |
|----------|----------|----------|
| `:stddev` | Variation across time series | Group consistency analysis |
| `:dist-stddev` | **Variation within measurements** | **Distribution spread analysis** |

## Related Operations

* [:stddev](stddev.md) - Standard deviation across time series (different calculation)
* [:dist-avg](dist-avg.md) - Average for timer/distribution metrics
* [:dist-max](dist-max.md) - Maximum for timer/distribution metrics
* [:sum](sum.md) - Total values across time series
* [:by](by.md) - Group results by dimensions

## See Also

* [Timer Metrics][timers] - Instrumentation for timing measurements with distribution statistics
* [Distribution Summary Metrics][distribution summaries] - Instrumentation for value distributions

[timers]: ../../spectator/core/meters/timer.md
[distribution summaries]: ../../spectator/core/meters/dist-summary.md