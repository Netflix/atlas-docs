@@@ atlas-signature
value: Double
-->
TimeSeriesExpr
@@@

Generates a time series where each datapoint has the same constant value. Since any numeric value
left on the stack is automatically converted to a constant line, this operator is rarely used
explicitly. It's mainly useful for clarity or when you need to be explicit about the conversion.

## Parameters

* **value**: The constant numeric value for all datapoints in the time series

## Examples

Creating an explicit constant line (though `42` alone would produce the same result):

@@@ atlas-example { hilite=:const }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42,:const
@@@

## Related Operations

* [:time](time.md) - Generate time-based values instead of constants
* [:random](random.md) - Generate random values instead of constants
* Mathematical operators like [:add](add.md), [:sub](sub.md) for combining with constants
