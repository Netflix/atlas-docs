@@@ atlas-signature
TimeSeriesExpr
stat: String
-->
TimeSeriesExpr
@@@

Create a summary time series showing the value of the specified summary statistic for the
data points of the input time series. Valid statistic values are `avg`, `count`, `max`, `min`,
`last`, and `total`. The graph below shows `avg`, `max`, `min`, and `last` for a simple input
time series:

@@@ atlas-graph { show-expr=false }
/api/v1/graph?h=125&no_legend_stats=1&s=e-6m&e=2012-01-01T00:06&tz=UTC&l=1.5&u=4.5&q=minuteOfDay,:time,e-2m,ge-6m,:time-span,2,:mul,:add,e-2m,ge,:time-span,1.5,:mul,:sub,1,e-1m,ge,:time-span,1,:sub,:div,1,:fadd,:fadd,m,:sset,m,:get,input,:legend,m,:get,avg,:stat,avg,:legend,3,:lw,60,:alpha,m,:get,max,:stat,max,:legend,3,:lw,60,:alpha,m,:get,min,:stat,min,:legend,3,:lw,60,:alpha,m,:get,last,:stat,last,:legend,3,:lw,60,:alpha
@@@

The `count` is the number of data points for the time series. In the example above, that is five
since the last value is `NaN`. The `total` is the sum of the data points for the time series.

The most common usage of stats is in conjunction with [:filter](filter.md) to restrict the set
of results for grouped expression. When filtering, helper macros, `:stat-$(name)`, can be used
to represent applying the statistic to the input time series being filtered without explicitly
repeating the input expression.

Example of usage:

@@@ atlas-example { hilite=:stat }
Input: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
Output: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,avg,:stat
@@@

