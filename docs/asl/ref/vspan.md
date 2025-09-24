@@@ atlas-signature
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Change the line style to be a vertical span. In this mode, any non-zero datapoints on the
line will be shown as a vertical band covering the full height of the graph. This is
frequently used to visualize when conditions are met, such as when an alert would have fired
or during maintenance windows.

## Parameters

* **expr**: A time series expression, typically a signal line with 0/1 values

## Examples

Visualizing when a threshold condition is exceeded:

@@@ atlas-example { hilite=:vspan }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:dup,20e3,:gt
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:dup,20e3,:gt,:vspan
@@@

## Related Operations

* [:line](line.md) - Default line style for time series
* [:area](area.md) - Fill area under the line
* [:stack](stack.md) - Stack multiple series as areas
* [:alpha](alpha.md) - Control transparency of the span

## See Also

See the [line style examples](../../api/graph/line-styles.md) page for more information on
available line styles and their use cases.
