@@@ atlas-signature
query: Query
-->
TimeSeriesExpr
@@@

Compute the average recorded value for timer and distribution summary metrics by dividing
the total recorded amount by the count of recorded measurements. This provides the true
average per individual measurement, not per time series or instance.

## Parameters

* **query**: Query for timer or distribution summary metrics

## How It Works

This operator automatically combines the appropriate statistics to calculate per-measurement averages:

**For Timers:**
```
# Manual calculation:
name,http.req.latency,:eq,statistic,totalTime,:eq,:and,:sum,
name,http.req.latency,:eq,statistic,count,:eq,:and,:sum,
:div

# Equivalent using :dist-avg:
name,http.req.latency,:eq,:dist-avg
```

**For Distribution Summaries:**
```
# Manual calculation:
name,request.size,:eq,statistic,totalAmount,:eq,:and,:sum,
name,request.size,:eq,statistic,count,:eq,:and,:sum,
:div

# Equivalent using :dist-avg:
name,request.size,:eq,:dist-avg
```

## Metric Requirements

The metrics must be instrumented using [Timer][timers] or [Distribution Summary][distribution summaries]
classes that collect both total and count statistics. These classes automatically record:

- **totalTime/totalAmount**: Cumulative sum of all measurements
- **count**: Number of individual measurements recorded

## Examples

Computing average request latency per request:

@@@ atlas-example { hilite=:dist-avg }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-avg
@@@

Simple usage pattern:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-avg
@@@

Computing average by auto-scaling group:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-avg,(,nf.asg,),:by
@@@

## Comparison with Other Averages

| Operator | Denominator | Use Case |
|----------|-------------|----------|
| `:avg` | Number of reporting time series | General time series averaging |
| `:node-avg` | Number of unique instances | Per-instance average |
| `:eureka-avg` | Number of UP instances in Eureka | Per-active-instance average |
| `:dist-avg` | Number of recorded measurements | **Per-measurement average** |

## Related Operations

* [:avg](avg.md) - Standard average across time series
* [:node-avg](node-avg.md) - Average using total instance count
* [:eureka-avg](eureka-avg.md) - Average using UP instances in Eureka service discovery

## See Also

* [Timer Metrics][timers] - Instrumentation for timing measurements
* [Distribution Summary Metrics][distribution summaries] - Instrumentation for size/amount measurements

[timers]: ../../spectator/core/meters/timer.md
[distribution summaries]: ../../spectator/core/meters/dist-summary.md