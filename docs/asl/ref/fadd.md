@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 + ts2): TimeSeriesExpr
@@@

Floating point addition operator that follows strict IEEE 754 floating point arithmetic.
Compute a new time series where each interval has the value `(ts1 + ts2)` where values
are the corresponding intervals in the input time series.

## Parameters

* **ts1**: First time series expression (left operand)
* **ts2**: Second time series expression (right operand)

## NaN Handling

Unlike [:add](add.md), this operator follows standard floating point rules where any
operation involving NaN produces NaN as the result:

| :fadd   | 3.0 | 0.0 | 1.0 | NaN | NaN |
|---------|-----|-----|-----|-----|-----|
| Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
| Input 2 | 1.0 | 0.0 | 0.0 | NaN | NaN |

!!! warning
    This can lead to confusing behavior when combining time series with missing data.
    If a time series has NaN values (e.g., from a node that started reporting mid-window),
    the result will be NaN. Use [:add](add.md) instead to treat NaN values as zero.

## Examples

Adding a constant value:

@@@ atlas-example { hilite=:fadd }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3,:fadd
@@@

Adding two time series:

@@@ atlas-example { hilite=:fadd }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:fadd
@@@

## Related Operations

* [:add](add.md) - Addition with NaN treated as 0 (often preferred for time series)
* [:fsub](fsub.md) - Floating point subtraction
* [:fmul](fmul.md) - Floating point multiplication
* [:fdiv](fdiv.md) - Floating point division