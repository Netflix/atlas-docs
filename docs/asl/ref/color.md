
@@@ atlas-signature
color: String
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Set the color for rendering the time series line. This allows you to specify exact colors for
individual series, overriding the default color palette. Colors can be specified using hex
codes, named colors, or ARGB values that include transparency.

## Parameters

* **expr**: The time series expression to apply color styling to
* **color**: Color specification (see supported formats below)

## Supported Color Formats

* **3-digit hex triplet**: e.g. `f00` is red
* **6-digit hex RGB**: e.g. `ff0000` is red
* **8-digit hex ARGB**: e.g. `ffff0000` is red with full opacity (first byte is alpha)
* **Named colors**: Theme-aware color names that adapt to light/dark themes:
    * `blue1`, `blue2`, `blue3`
    * `gray1`, `gray2`, `gray3`
    * `green1`, `green2`, `green3`
    * `orange1`, `orange2`, `orange3`
    * `purple1`, `purple2`, `purple3`
    * `red1`, `red2`, `red3`

## Examples

Setting a specific red color:

@@@ atlas-example { hilite=:color }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,ff0000,:color
@@@

## Alpha Channel Behavior

When using 8-digit ARGB format, the color includes its own alpha channel. If [:alpha](alpha.md)
is applied after `:color`, it will modify the alpha channel of the previously set color.
However, if `:color` is applied after `:alpha`, it will override the alpha setting.

## Related Operations

* [:alpha](alpha.md) - Set transparency (interacts with ARGB colors)
* [:palette](palette.md) - Use color palettes for multiple series
* [:lw](lw.md) - Set line width
* [:line](line.md) - Set line style

## See Also

* [Color Palettes](../../api/graph/color-palettes.md) - For automatic color assignment
* [Themes](../../api/graph/theme.md) - How named colors adapt to themes