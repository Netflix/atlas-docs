@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the absolute value of the input time series.
This ensures all values are non-negative by converting negative values to positive while
leaving positive values unchanged.

## Parameters

* **expr**: The time series expression to take the absolute value of

## Examples

Demonstrating absolute value with different constant values:

@@@ atlas-example { hilite=:abs }
0: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=0,:abs
64: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=64,:abs
-64: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=-64,:abs
@@@

This shows that `:abs` converts 0 to 0, leaves positive values unchanged, and converts
negative values to positive.

## Related Operations

* [:neg](neg.md) - Negation (changes sign, compared to abs which removes sign)
* [:sub](sub.md) - Subtraction (often used with abs for absolute differences)
* [:add](add.md) - Addition operation
* [:mul](mul.md) - Multiplication operation
