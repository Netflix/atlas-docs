@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Shorthand equivalent to writing: `:dup,10,0.1,0.5,:sdes,sdes-simple,:named-rewrite`

@@@ atlas-example { hilite=:sdes-simple }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:sdes-simple
@@@