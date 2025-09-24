There are four [line styles](../../asl/ref/ls.md) available:

* [Line](#line)
* [Area](#area)
* [Stack](#stack)
* [Vertical Span](#vertical-span)
* [Heatmap](#heatmap)

Multiple styles can be used in the same chart or combined with other operations.

* [Stacked Percentage](#stacked-percentage)
* [Combinations](#combinations)
* [Layering](#layering)


## Line

The default style is line.

@@@ atlas-uri { hilite=:line }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:line&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:line&s=e-1w
@@@


## Area

Area will fill the space between the line and 0 on the Y-axis. The [alpha](../../asl/ref/alpha.md)
setting is just used to help visualize the overlap.

@@@ atlas-uri { hilite=:area }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:area,40,:alpha&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:area,40,:alpha&s=e-1w
@@@

Similarly for negative values:

@@@ atlas-uri { hilite=:area }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:neg,:area,40,:alpha&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:neg,:area,40,:alpha&s=e-1w
@@@


## Stack

Stack is similar to [area](#area), but will stack the filled areas on top of each other.

@@@ atlas-uri { hilite=:stack }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:stack&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:stack&s=e-1w
@@@

Similarly for negative values:

@@@ atlas-uri { hilite=:stack }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:neg,:stack&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:neg,:stack&s=e-1w
@@@


## Stacked Percentage

The [stack](#stack) style can be combined with the [:pct](../../asl/ref/pct.md) operator to get a stacked
percentage chart for a group by:

@@@ atlas-uri { hilite=:pct }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:pct,:stack&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,:pct,:stack&s=e-1w
@@@


## Heatmap

Since 1.8.

Plotting many time series with a heat map can be useful for identifying concentrations of
measurements where individual lines may produce too much noise.

See [Heatmap](heatmap.md) for more details.

@@@ atlas-uri { hilite=:heatmap }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,:heatmap
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,:heatmap
@@@


## Vertical Span

The vertical span style converts non-zero to spans. This is often used to highlight some portion of
another line.

@@@ atlas-uri { hilite=:vspan }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,50e3,:gt,:vspan&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,50e3,:gt,:vspan&s=e-1w
@@@


## Combinations

Line styles can be combined, e.g., to highlight the portion of a line that is above a
threshold:

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,5003,:gt,:vspan,40,:alpha,50e3&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,50e3,:gt,:vspan,40,:alpha,50e3&s=e-1w
@@@


## Layering

The z-order is based on the order of the expression on the stack.

@@@ atlas-uri
/api/v1/graph?e=2015-03-10T13:13&no_legend=1&q=t,name,sps,:eq,:sum,:set,t,:get,:stack,t,:get,1.1,:mul,6h,:offset,t,:get,4,:div,:stack&s=e-2d
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2015-03-10T13:13&no_legend=1&q=t,name,sps,:eq,:sum,:set,t,:get,:stack,t,:get,1.1,:mul,6h,:offset,t,:get,4,:div,:stack&s=e-2d
@@@
