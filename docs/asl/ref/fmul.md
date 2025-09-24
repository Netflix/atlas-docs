@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 * ts2): TimeSeriesExpr
@@@

Floating point multiplication operator that follows strict IEEE 754 floating point arithmetic.
Compute a new time series where each interval has the value `(ts1 * ts2)` where values
are the corresponding intervals in the input time series.

!!! info
    **Note**: `:fmul` is functionally equivalent to [:mul](mul.md) as both handle NaN values
    using standard floating point rules. This variant exists for consistency with other
    floating point operators like `:fadd` and `:fsub`.

## Parameters

* **ts1**: First time series expression (left operand)
* **ts2**: Second time series expression (right operand)

## Examples

Multiplying by a constant value:

@@@ atlas-example { hilite=:fmul }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,1024,:fmul
@@@

Multiplying two time series:

@@@ atlas-example { hilite=:fmul }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:fmul
@@@

## Related Operations

* [:mul](mul.md) - Equivalent multiplication operation (same behavior as `:fmul`)
* [:fadd](fadd.md) - Floating point addition
* [:fsub](fsub.md) - Floating point subtraction
* [:fdiv](fdiv.md) - Floating point division