@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Shorthand equivalent to writing: `:dup,:dup,:sum,:div,100,:mul,pct,:named-rewrite`
The percent contribution of an individual time series to a group.

Example:

@@@ atlas-stacklang
/api/v1/graph?q=name,sps,:eq,(,nf.cluster,),:by,:pct
@@@

@@@ atlas-example { hilite=:pct }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:pct
Stack to 100%: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:pct,:stack
@@@