@@@ atlas-signature
axisNumber: Int
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Assign a time series to a specific Y-axis for display. This allows multiple time series with
different scales or units to be displayed on the same graph while maintaining separate axis
scaling. Axis 0 (left side) is the default, and axes 1-4 provide additional right-side axes
for data with different ranges or units.

## Parameters

* **expr**: The time series expression to assign to the specified axis
* **axisNumber**: Y-axis number (integer from 0 to 4 inclusive)
  - **0**: Left Y-axis (default)
  - **1-4**: Right Y-axes (numbered from innermost to outermost)

## Examples

Assigning a time series to axis 1 (first right axis):

@@@ atlas-example { hilite=:axis }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,42
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,42,1,:axis
@@@

## Related Operations

* [:legend](legend.md) - Customize axis labels and legends
* [:by](by.md) - Group data that might need separate axes
* [:offset](offset.md) - Compare data from different time periods

## See Also

* [Multi-Y Axis](../../api/graph/multi-y.md) - API documentation for multi-axis graphs