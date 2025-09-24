@@@ atlas-signature
window: Duration
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

!!! warning
    **Deprecated**: Use [:rolling-mean](rolling-mean.md) instead. This operator exists for
    backwards compatibility but new expressions should use the more flexible rolling operators.

Compute a moving average over a time-based window. This operator smooths time series data by
averaging values within a sliding time window, which can help reduce noise and identify trends.

## Parameters

* **expr**: The time series expression to apply the moving average to
* **window**: Time duration for the averaging window (e.g., `5m`, `PT20M`)

## Behavior

* **Window requirement**: Emits `NaN` until the full window duration has data
* **NaN handling**: Input `NaN` values are treated as zeros in the calculation
* **Window sizing**: Window duration is rounded down to fit evenly within step size boundaries
* **Edge cases**: If step size > window duration, the operation becomes a no-op

## Window Sizing Rules

The effective window size depends on the relationship to step size:

| Window | Step Size | Effective Window | Datapoints |
|--------|-----------|------------------|------------|
| 5m     | 1m        | 5m               | 5          |
| 5m     | 2m        | 4m               | 2          |
| 2m     | 5m        | No-op            | 1          |

## Examples

5-minute moving average:

@@@ atlas-example { hilite=:trend }
5 Minutes: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,PT5M,:trend
@@@

20-minute moving average:

@@@ atlas-example { hilite=:trend }
20 Minutes: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,20m,:trend
@@@

## Sample Calculation

Example showing how `:trend` processes data:

| Input | 2m,:trend | 5m,:trend |
|-------|-----------|-----------|
| 0     | NaN       | NaN       |
| 1     | 0.5       | NaN       |
| -1    | 0.0       | NaN       |
| NaN   | -0.5      | NaN       |
| 0     | 0.0       | 0.0       |
| 1     | 0.5       | 0.2       |
| 2     | 1.5       | 0.4       |
| 1     | 1.5       | 0.8       |
| 1     | 1.0       | 1.0       |
| 0     | 0.5       | 1.0       |

## Migration Guide

Replace `:trend` with `:rolling-mean` for similar functionality:

```
# Old (deprecated):
name,cpu,:eq,:sum,5m,:trend

# New (recommended):
name,cpu,:eq,:sum,5,:rolling-mean
```

## Related Operations

* [:rolling-mean](rolling-mean.md) - Recommended replacement (uses datapoint count instead of time)
* [:rolling-max](rolling-max.md) - Rolling maximum over datapoint windows
* [:rolling-min](rolling-min.md) - Rolling minimum over datapoint windows
* [:sdes](sdes.md) - More sophisticated smoothing with trend detection

## See Also

* [Step Size](../../concepts/time-series.md#step-size) - Understanding time series intervals