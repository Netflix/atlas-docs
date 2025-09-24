@@@ atlas-signature
minValue: Double
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Limit the minimum value of a time series by clamping values below a specified threshold.
Any values less than the minimum will be set to the minimum value, while values at or
above the minimum remain unchanged. This is the counterpart to [:clamp-max](clamp-max.md)
for setting floor values.

## Parameters

* **expr**: The time series expression to apply the minimum limit to
* **minValue**: The minimum allowed value (values below this will be clamped)

## Behavior

* **Values ≥ minValue**: Remain unchanged
* **Values < minValue**: Are set to exactly minValue
* **Missing data**: NaN values are preserved as NaN

## Examples

Setting a minimum threshold to prevent negative spikes:

@@@ atlas-example { hilite=:clamp-min }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,200e3,:clamp-min
@@@

## Related Operations

* [:clamp-max](clamp-max.md) - Limit maximum values (ceiling operation)

## See Also

* [Axis Bounds](../../api/graph/axis-bounds.md) - Global axis scaling options
* [Axis Scale](../../api/graph/axis-scale.md) - Alternative approaches for handling extreme values