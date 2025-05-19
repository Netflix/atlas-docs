
@@@ atlas-signature
String
TimeSeriesExpr
-->
StyleExpr
@@@

Set the color for the line. The value should be one of:

* [Hex triplet](http://en.wikipedia.org/wiki/Web_colors#Hex_triplet), e.g. f00 is red.
* 6 digit hex RBG, e.g. ff0000 is red.
* 8 digit hex ARGB, e.g. ffff0000 is red. The first byte is the [alpha](alpha.md)
  setting to use with the color.
* Named colors. These are useful when working with [themes](../../api/graph/theme.md), they provide
  a few shades for some common colors. The specific colors will vary based on the theme to ensure
  they have good contrast with the background color. Available options:
    * `blue1`, `blue2`, `blue3`
    * `gray1`, `gray2`, `gray3`
    * `green1`, `green2`, `green3`
    * `orange1`, `orange2`, `orange3`
    * `purple1`, `purple2`, `purple3`
    * `red1`, `red2`, `red3`

For queries with multiple time series, color palettes are available to automatically assign
different colors to the various series. See [Color Palettes](../../api/graph/color-palettes.md).

@@@ atlas-example { hilite=:color }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,ff0000,:color
@@@