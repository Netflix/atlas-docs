@@@ atlas-signature
String
TimeSeriesExpr
-->
StyleExpr
@@@

Sort the results of an expression in the legend by one of the
[summary statistics](stat.md) or by the legend text. The default
behavior is to sort by the legend text. This will sort in ascending
order by default, for descending order use [order](order.md).

Since: 1.5

Example:

@@@ atlas-example { hilite=:sort }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,max,:sort
@@@