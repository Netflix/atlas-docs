
@@@ atlas-signature
TimeSeriesExpr
String
-->
StyleExpr
@@@

Since: 1.7

Set the color for the line. The value should be one of:

* [Hex triplet](http://en.wikipedia.org/wiki/Web_colors#Hex_triplet), e.g. f00 is red.
* 6 digit hex RBG, e.g. ff0000 is red.
* 8 digit hex ARGB, e.g. ffff0000 is red. The first byte is the [alpha](style-alpha)
  setting to use with the color.

@@@ atlas-example { hilite=:color }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,ff0000,:color
@@@
