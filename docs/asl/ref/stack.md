@@@ atlas-signature
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Change the line style to be a stacked area plot. In this mode, the line will be filled
as an area that stacks on top of the previous stacked line on the same axis. For positive
values, areas stack upward from zero; for negative values, areas stack downward below
zero. This creates a cumulative visualization where each series builds upon the previous
ones, making it easy to see both individual contributions and total values.

## Parameters

* **expr**: A time series expression to render as a stacked area

## Examples

Converting grouped series to stacked areas:

@@@ atlas-example { hilite=:stack }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,:stack
@@@

Stacking with mixed positive and negative values (subtracting 5000 creates negative portions):

@@@ atlas-example { hilite=:stack }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,5e3,:sub
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,5e3,:sub,:stack
@@@

This shows how positive values stack upward from zero while negative values stack
downward below zero, creating separate cumulative areas above and below the zero line.

## Stacking Order

Series are stacked in the order they appear in the result set. Use sorting operations
before applying `:stack` to control the stacking order.

## Related Operations

* [:area](area.md) - Single area plot (not stacked)
* [:line](line.md) - Convert back to line style
* [:by](by.md) - Group data to create multiple series for stacking
* [:sort](sort.md) - Control the order of stacking

## See Also

See the [line style examples](../../api/graph/line-styles.md) page for more information
on available line styles and their use cases.
