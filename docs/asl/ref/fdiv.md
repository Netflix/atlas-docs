@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 / ts2): TimeSeriesExpr
@@@

Floating point division operator that follows strict IEEE 754 floating point arithmetic.
Compute a new time series where each interval has the value `(ts1 / ts2)` where values
are the corresponding intervals in the input time series.

## Parameters

* **ts1**: First time series expression (left operand, numerator)
* **ts2**: Second time series expression (right operand, denominator)

## Floating Point Behavior

This operator follows strict floating point rules, including:

| :fdiv   | 2.0 | NaN | Inf | NaN | NaN |
|---------|-----|-----|-----|-----|-----|
| Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
| Input 2 | 1.0 | 0.0 | 0.0 | NaN | NaN |

Key behaviors:
* **Division by zero**: Results in positive or negative infinity (Inf)
* **Zero divided by zero**: Results in NaN
* **Any operation with NaN**: Results in NaN

!!! warning
    **For time series visualization**: The strict floating point behavior can create confusing
    results when dealing with missing data or inactive periods. Unless you specifically need
    IEEE 754 compliance, use [:div](div.md) instead, which provides behavior more appropriate
    for time series graphs.

## Examples

Dividing by a constant value:

@@@ atlas-example { hilite=:fdiv }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,1024,:fdiv
@@@

Dividing two time series:

@@@ atlas-example { hilite=:fdiv }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:fdiv
@@@

## Related Operations

* [:div](div.md) - Division with special zero handling (often preferred for time series)
* [:fadd](fadd.md) - Floating point addition
* [:fsub](fsub.md) - Floating point subtraction
* [:fmul](fmul.md) - Floating point multiplication