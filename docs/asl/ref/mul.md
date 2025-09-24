@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 * ts2): TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a * b)` where `a`
and `b` are the corresponding intervals in the input time series.

## Parameters

* **ts1**: First time series or numeric value (multiplicand)
* **ts2**: Second time series or numeric value to multiply with the first (multiplier)

## Examples

Multiplying a time series by a constant (e.g., converting to different units):

@@@ atlas-example { hilite=:mul }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,1024,:mul
@@@

Multiplying two time series together:

@@@ atlas-example { hilite=:mul }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,requestLatency,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:mul
@@@

## Related Operations

* [:add](add.md) - Add two time series
* [:sub](sub.md) - Subtract two time series
* [:div](div.md) - Divide two time series
* [:fmul](fmul.md) - Equivalent to :mul (provided for symmetry with other math operations)
* [:pow](pow.md) - Raise to a power