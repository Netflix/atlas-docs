@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 - ts2): TimeSeriesExpr
@@@

Floating point subtraction operator that follows strict IEEE 754 floating point arithmetic.
Compute a new time series where each interval has the value `(ts1 - ts2)` where values
are the corresponding intervals in the input time series.

## Parameters

* **ts1**: First time series expression (left operand, minuend)
* **ts2**: Second time series expression (right operand, subtrahend)

## NaN Handling

Unlike [:sub](sub.md), this operator follows standard floating point rules where any
operation involving NaN produces NaN as the result:

| :fsub   | 1.0 | 0.0 | 1.0 | NaN | NaN |
|---------|-----|-----|-----|-----|-----|
| Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
| Input 2 | 1.0 | 0.0 | 0.0 | NaN | NaN |

!!! warning
    This can lead to confusing behavior when combining time series with missing data.
    If a time series has NaN values (e.g., from a node that started reporting mid-window),
    the result will be NaN. Use [:sub](sub.md) instead to treat NaN values as zero.

## Examples

Subtracting a constant value:

@@@ atlas-example { hilite=:fsub }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30000,:fsub
@@@

Subtracting two time series:

@@@ atlas-example { hilite=:fsub }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:fsub
@@@

## Related Operations

* [:sub](sub.md) - Subtraction with NaN treated as 0 (often preferred for time series)
* [:fadd](fadd.md) - Floating point addition
* [:fmul](fmul.md) - Floating point multiplication
* [:fdiv](fdiv.md) - Floating point division