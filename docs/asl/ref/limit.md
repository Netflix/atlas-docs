@@@ atlas-signature
TimeSeriesExpr
n: Integer
-->
StyleExpr
@@@

Restrict the output to the first `N` lines from the input expression. The lines will be
chosen in order based on the [sort](sort.md) and [order](order.md) used.


Example:

@@@ atlas-example { hilite=:limit }
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,3,:limit
@@@
