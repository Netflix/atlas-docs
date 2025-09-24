@@@ atlas-signature
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Change the line style to be a standard line plot. This is the default visualization
mode for time series data and usually does not need to be set explicitly. It's mainly
useful for converting back from other line styles like area or stack.

## Parameters

* **expr**: A time series expression to render as a line plot

## Examples

Explicitly setting line style (though this is the default):

@@@ atlas-example { hilite=:line }
Default: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:line
@@@

## Related Operations

* [:area](area.md) - Fill area under the line
* [:stack](stack.md) - Stack multiple lines as areas
* [:vspan](vspan.md) - Show vertical spans for events
* [:alpha](alpha.md) - Control line transparency
* [:lw](lw.md) - Control line width/thickness

## See Also

See the [line style examples](../../api/graph/line-styles.md) page for more information
on available line styles and their use cases.
