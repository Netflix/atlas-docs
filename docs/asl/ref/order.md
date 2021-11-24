@@@ atlas-signature
TimeSeriesExpr
String
-->
StyleExpr
@@@

Order to use for [sorting](sort.md) results. Supported values are `asc` and `desc`
for ascending and descending order respectively. Default is `asc`.

Since: 1.5

Examples:

@@@ atlas-example { hilite=:order }
Sorted: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,max,:sort,asc,:order
Default: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,desc,:order
@@@
