@@@ atlas-signature
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Change the line style to be an area plot. In this mode, the line will be filled from
the data points to zero on the Y-axis, creating a solid area. For positive values,
the area fills down to zero; for negative values, the area fills up to zero. This
visualization is useful for showing volume, cumulative values, or when you want
to emphasize the magnitude of the data.

!!! note
    **Multiple Series Behavior**: When multiple time series are rendered as areas, their
    filled regions will overlap each other. To see cumulative contributions where each
    series builds on top of the previous ones, use [:stack](stack.md) instead.

## Parameters

* **expr**: A time series expression to render as an area plot

## Examples

Converting a line plot to an area plot:

@@@ atlas-example { hilite=:area }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,:area
@@@

## Related Operations

* [:line](line.md) - Default line style (converts area back to line)
* [:stack](stack.md) - Stack multiple areas on top of each other
* [:vspan](vspan.md) - Show vertical spans for events or conditions
* [:alpha](alpha.md) - Control transparency of area fills

## See Also

See the [line style examples](../../api/graph/line-styles.md) page for more information
on available line styles and their use cases.
