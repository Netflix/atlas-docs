@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Convert a rate per second to a rate per step interval. This multiplies each value by the step
size (in seconds) to estimate the total count of events that occurred during each step interval.

Metrics like counters are reported as rates (events per second), but in some case you need
to know the actual count of events that occurred in each time interval. For example, if you
have a rate of 64 requests/second and your step size is 60 seconds, this operation converts
that to 3,840 total requests for that step.

## Parameters

* **expr**: The time series expression representing a rate per second

## Examples

Converting various rates to per-step counts:

@@@ atlas-example { hilite=:per-step }
0: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=0,:per-step
64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=64,:per-step
-64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=-64,:per-step
@@@

## Related Operations

* [:integral](integral.md) - Sum values across time (often used with :per-step)
* [:derivative](derivative.md) - Opposite operation (rate of change)
* [:mul](mul.md) - Manual scaling by constant factors

## See Also

* [Time Series Concepts](../../concepts/time-series.md#step-size) - Understanding step size