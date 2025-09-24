@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a new time series where each interval has the negated value of the input time series.
This applies the unary minus operation, multiplying each value by -1.

## Parameters

* **expr**: The time series expression to negate

## Examples

Demonstrating negation with different constant values:

@@@ atlas-example { hilite=:neg }
0: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=0,:neg
64: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=64,:neg
-64: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=-64,:neg
@@@

This shows that `:neg` converts 0 to 0, positive values to negative, and negative values to positive.

## Related Operations

* [:abs](abs.md) - Absolute value (always positive)
* [:sub](sub.md) - Subtraction (`:neg` is equivalent to `0,:swap,:sub`)
* [:mul](mul.md) - Multiplication (`:neg` is equivalent to `-1,:mul`)
* [:add](add.md) - Addition operation
