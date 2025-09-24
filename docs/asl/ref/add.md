@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 + ts2): TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a addNaN b)` where `a`
and `b` are the corresponding intervals in the input time series.

NaN values are handled specially: if either input is NaN, it is treated as 0 for the operation.
If both inputs are NaN, the result is NaN. This differs from strict floating point addition
where any NaN input produces NaN output.

:add    | 3.0 | 0.0 | 1.0 | 1.0 | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 1.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 2.0 | 0.0 | 0.0 | NaN | NaN |

## Parameters

* **ts1**: First time series or numeric value
* **ts2**: Second time series or numeric value to add to the first

## Examples

Adding a constant value to a time series:

@@@ atlas-example { hilite=:add }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3,:add
@@@

Adding two time series together:

@@@ atlas-example { hilite=:add }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:add
@@@

## Related Operations

* [:fadd](fadd.md) - Strict floating point addition (NaN + anything = NaN)
* [:sub](sub.md) - Subtract two time series
* [:mul](mul.md) - Multiply two time series
* [:div](div.md) - Divide two time series
