@@@ atlas-signature
Int
TimeSeriesExpr
-->
StyleExpr
@@@

Specify which Y-axis to use for the line. The value specified is the axis number and should be
an integer in the range 0 to 4 inclusive.

Example:

@@@ atlas-example { hilite=:axis }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,42
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,42,1,:axis
@@@