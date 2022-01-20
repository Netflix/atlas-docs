@@@ atlas-signature
n: Int
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Shorthand equivalent to writing: `:limit`

Example:

@@@ atlas-example { hilite=:head }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,2,:head
@@@
