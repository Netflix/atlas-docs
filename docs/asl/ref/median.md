@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

Shorthand equivalent to writing: `(,50,),:percentiles`

@@@ atlas-example { hilite=:median }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq,:median
@@@