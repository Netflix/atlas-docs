@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 / ts2): TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a / b)` where `a`
and `b` are the corresponding intervals in the input time series.

Special handling for division by zero:
- If both `a` and `b` are 0, the result is 0 (instead of NaN)
- If only `b` (divisor) is 0, the result is NaN

:div    | 0.5 | 0.0 | NaN | NaN | NaN |
---------|-----|-----|-----|-----|-----|
Input 1 | 1.0 | 0.0 | 1.0 | 1.0 | NaN |
Input 2 | 2.0 | 0.0 | 0.0 | NaN | NaN |

## Parameters

* **ts1**: First time series or numeric value (dividend/numerator)
* **ts2**: Second time series or numeric value to divide the first by (divisor/denominator)

## Examples

Dividing a time series by a constant:

@@@ atlas-example { hilite=:div }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,42
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,42,:div
@@@

Dividing two time series (e.g., calculating error rate):

@@@ atlas-example { hilite=:div }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:div
@@@

## Related Operations

* [:add](add.md) - Add two time series
* [:sub](sub.md) - Subtract two time series
* [:mul](mul.md) - Multiply two time series
* [:fdiv](fdiv.md) - Strict floating point division (NaN / anything = NaN)
* [:avg](avg.md) - Calculate average (uses division internally)