@@@ atlas-signature
TimeSeriesExpr
Double
-->
TimeSeriesExpr
@@@

Restricts the minimum value of the output time series to the specified value. Values
from the input time series that are greater than or equal to the minimum will not be
changed. A common use-case is to allow for auto-scaled axis up to a specified bound.
For more details see [:clamp-max](clamp-max.md).

@@@ atlas-example { hilite=:clamp-min }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,200e3,:clamp-min
@@@