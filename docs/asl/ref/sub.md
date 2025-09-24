@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 - ts2): TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a subtractNaN b)` where `a`
and `b` are the corresponding intervals in the input time series.

NaN values are handled specially: if either input is NaN, it is treated as 0 for the operation.
If both inputs are NaN, the result is NaN. This differs from strict floating point subtraction
where any NaN input produces NaN output.

:sub    | 1.0 | 0.0 | 1.0 | 1.0 | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 2.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 1.0 | 0.0 | 0.0 | NaN | NaN |

## Parameters

* **ts1**: First time series or numeric value (minuend)
* **ts2**: Second time series or numeric value to subtract from the first (subtrahend)

## Examples

Subtracting a constant value from a time series:

@@@ atlas-example { hilite=:sub }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,30e3,:sub
@@@

Subtracting two time series:

@@@ atlas-example { hilite=:sub }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:sub
@@@

## Related Operations

* [:add](add.md) - Add two time series
* [:fsub](fsub.md) - Strict floating point subtraction (NaN - anything = NaN)
* [:mul](mul.md) - Multiply two time series
* [:div](div.md) - Divide two time series
* [:neg](neg.md) - Negate a single time series