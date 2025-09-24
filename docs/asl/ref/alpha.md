@@@ atlas-signature
alpha: String
TimeSeriesExpr
-->
StyleExpr
@@@

Set the alpha value for the colors on the line. The value should be a two digit hex number
where `00` is transparent and `ff` is opaque.

Since [:color](color.md) includes its own alpha channel, the order of operations matters:
if `:color` is applied after `:alpha`, it will override the alpha setting. However, `:alpha`
applied after `:color` will modify the alpha channel of the previously set color.

## Parameters

* **alpha**: A two-digit hexadecimal value from `00` (transparent) to `ff` (opaque)

## Examples

Basic alpha transparency applied to a stacked area chart:

@@@ atlas-example { hilite=:alpha }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack,40,:alpha
@@@

Applying alpha after color modifies the alpha channel of the color:

@@@ atlas-example { hilite=:alpha }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack,f00,:color
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,:stack,f00,:color,40,:alpha
@@@

## Related Operations

* [:color](color.md) - Set explicit color (interaction depends on order of operations)
* [:palette](palette.md) - Set color palette for multiple lines