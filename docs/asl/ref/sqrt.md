@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the square root of the value from the
input time series. For negative values, the result is NaN following standard mathematical conventions.

## Parameters

* **expr**: The time series expression to take the square root of

## Examples

Demonstrating square root with different constant values:

@@@ atlas-example { hilite=:sqrt }
0: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=0,:sqrt
64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=64,:sqrt
-64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=-64,:sqrt
@@@

The examples show that √0 = 0, √64 = 8, and √(-64) = NaN.

## Related Operations

* [:pow](pow.md) - Exponentiation (square root is equivalent to `0.5,:pow`)
* [:abs](abs.md) - Absolute value (often used with sqrt to handle negative values)
* [:mul](mul.md) - Multiplication operation
* [:add](add.md) - Addition operation