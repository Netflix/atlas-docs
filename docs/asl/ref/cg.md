@@@ atlas-signature
keys: List[String]
Expr
-->
Expr
@@@

Recursively add a list of keys to group by expressions. This can be useful for tooling that
needs to adjust existing expressions to include keys in the grouping. 

@@@ atlas-example { hilite=:cg }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.app,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.app,),:by,(,nf.cluster,),:cg
@@@

