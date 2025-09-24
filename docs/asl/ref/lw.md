@@@ atlas-signature
width: Int
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Set the line width (thickness) for drawing the time series. The width is specified in pixels
and affects how prominently the line appears on the graph. This is useful for emphasizing
important time series or creating visual hierarchy between different data.

## Parameters

* **expr**: The time series expression to apply line width styling to
* **width**: Line width in pixels (positive integer)

## Examples

Setting line width to make series more prominent:

@@@ atlas-example { hilite=:lw }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,2,:lw
@@@

## Related Operations

* [:line](line.md) - Set line style (works with line width)
* [:color](color.md) - Set line color
* [:alpha](alpha.md) - Set line transparency
* [:area](area.md) - Fill area under the line
* [:stack](stack.md) - Stack multiple lines as areas

## See Also

* [Line Style Examples](../../api/graph/line-styles.md)