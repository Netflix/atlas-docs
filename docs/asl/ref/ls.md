@@@ atlas-signature
style: String
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Set the line style for visualizing time series data. This operator allows you to choose between
different visualization styles that control how the data is rendered on the graph. It provides
a single interface for setting any of the four main line styles.

## Parameters

* **expr**: The time series expression to apply the line style to
* **style**: The line style to use (one of: `line`, `area`, `stack`, `vspan`)

## Supported Styles

### `line` (Default)
* **Behavior**: Draws a normal line connecting data points
* **Use case**: Standard time series visualization
* **Equivalent**: Using [:line](line.md) operator

### `area`
* **Behavior**: Fills the space between the line and zero on the Y-axis
* **Use case**: Emphasizing magnitude and volume
* **Equivalent**: Using [:area](area.md) operator

### `stack`
* **Behavior**: Stacks filled areas on top of previous stacked lines on the same axis
* **Use case**: Showing cumulative contributions
* **Equivalent**: Using [:stack](stack.md) operator

### `vspan`
* **Behavior**: Non-zero datapoints are drawn as vertical spans covering the full graph height
* **Use case**: Event visualization and condition marking
* **Equivalent**: Using [:vspan](vspan.md) operator

## Examples

Basic line style (default):

@@@ atlas-example { hilite=:ls }
Line: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,line,:ls
@@@

Area fill visualization:

@@@ atlas-example { hilite=:ls }
Area: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,area,:ls
@@@

Stacked area visualization:

@@@ atlas-example { hilite=:ls }
Stack: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,stack,:ls
@@@

Vertical span for events:

@@@ atlas-example { hilite=:ls }
VSpan: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,name,),:by,200e3,:gt,vspan,:ls
@@@

## Alternative Approach

While `:ls` provides a unified interface, you can also use the specific style operators directly:

```
# These pairs are equivalent:
name,cpu,:eq,:sum,area,:ls
name,cpu,:eq,:sum,:area

name,cpu,:eq,:sum,stack,:ls
name,cpu,:eq,:sum,:stack
```

## Related Operations

* [:line](line.md) - Standard line style (default)
* [:area](area.md) - Area fill style
* [:stack](stack.md) - Stacked area style
* [:vspan](vspan.md) - Vertical span style
* [:alpha](alpha.md) - Control line transparency
* [:lw](lw.md) - Control line width

## See Also

* [Line Style Examples](../../api/graph/line-styles.md) - Visual examples of all line styles