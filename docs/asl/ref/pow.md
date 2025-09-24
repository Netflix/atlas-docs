@@@ atlas-signature
exponent: TimeSeriesExpr
base: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(base ^ exponent)` where `base`
and `exponent` are the corresponding intervals in the input time series. This performs
mathematical exponentiation using standard floating point arithmetic.

## Parameters

* **base**: The base time series expression (left operand)
* **exponent**: The exponent time series expression (right operand)

## Examples

Raise a time series to a constant power:

@@@ atlas-example { hilite=:pow }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,42,:pow
@@@

Raise one time series to the power of another:

@@@ atlas-example { hilite=:pow }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,name,requestsPerSecond,:eq,:max,(,name,),:by,:pow
@@@

## Related Operations

* [:mul](mul.md) - Multiplication (repeated addition, compared to exponentiation as repeated multiplication)
* [:add](add.md) - Addition operation
* [:sub](sub.md) - Subtraction operation
* [:div](div.md) - Division operation
* [:sqrt](sqrt.md) - Square root (inverse of power of 2)