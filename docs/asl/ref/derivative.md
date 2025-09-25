@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the rate of change (derivative) of a time series, showing how much the value changes
per step interval. This is the inverse operation of [:integral](integral.md) and is useful for
converting cumulative values back to rates or identifying trends in the data.

## Parameters

* **expr**: The time series expression to compute the derivative of

## Behavior

Each output value represents the difference between consecutive datapoints:

- `derivative[i] = input[i] - input[i-1]`
- The first datapoint will typically be NaN since there's no previous value
- Missing values (NaN) are handled as 0 for the calculation

## Examples

Comparing integral and derivative operations:

@@@ atlas-example { hilite=:derivative }
Derivative: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:derivative
Integral: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:integral
Integral Then Derivative: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:integral,:derivative
@@@

## Relationship with Integral

`:derivative` and `:integral` have an asymmetric relationship:

- Applying `:integral` then `:derivative` approximates the original signal
- Applying `:derivative` then `:integral` does NOT restore the original signal

The derivative operation loses information that cannot be recovered with integral. For example,
with a constant input like `1`:

- `1,:derivative` produces `0` (derivative of constant is zero)
- `0,:integral` produces `0` (integral of zero stays zero)
- The original constant value `1` is permanently lost

## Related Operations

* [:integral](integral.md) - Cumulative sum (inverse operation)
* [:per-step](per-step.md) - Convert rates to step-based counts
* [:sub](sub.md) - Manual difference calculation between time series
* [:rolling-sum](rolling-sum.md) - Rolling accumulation (related to cumulative operations)