Options for adjusting legend:

* [Automatic](#automatic)
* [Explicit](#explicit)
* [Variables](#variables)
* [Disable](#disable)
* [Disable Stats](#disable-stats)
* [Sorting](#sorting)

## Automatic

If no [explicit](#explicit) legend is specified, then the system will generate an automatic
legend that summarizes the expression. There is no particular guarantee about what it will contain
and in some cases it is difficult to generate a usable legend automatically. Example:

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&q=hourOfDay,:time,100,:mul,minuteOfHour,:time,:add&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=hourOfDay,:time,100,:mul,minuteOfHour,:time,:add&s=e-1w
@@@

## Explicit

The legend for a line can be explicitly set using the [:legend](../../asl/ref/legend.md) operator.

@@@ atlas-uri { hilite=:legend }
/api/v1/graph?e=2012-01-01T00:00&q=hourOfDay,:time,100,:mul,minuteOfHour,:time,:add,time+value,:legend&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=hourOfDay,:time,100,:mul,minuteOfHour,:time,:add,time+value,:legend&s=e-1w
@@@

## Variables

Tag keys can be used as variables to plug values into the legend. This is useful when working
with group by operations to customize the legend for each output. The variable can be expressed
as a `$` followed by the tag key if it is the only part of the legend:

@@@ atlas-uri { hilite=:legend }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend&s=e-1w
@@@

Or as `$(` the tag key and a closing `)` if combined with other text:

@@@ atlas-uri { hilite=:legend }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,cluster+$(nf.cluster)+sps,:legend&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,cluster+$(nf.cluster)+sps,:legend&s=e-1w
@@@

## Disable

Legends can be disabled using the `no_legend` graph parameter.

@@@ atlas-uri { hilite=legend }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w
@@@

## Disable Stats

You can also save vertical space and keep the legend by disabling the summary stats shown in the
legend using the `no_legend_stats` graph parameter.

@@@ atlas-uri { hilite=no_legend_stats }
/api/v1/graph?e=2012-01-01T00:00&no_legend_stats=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend_stats=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w
@@@

## Sorting

By default the legend for an [axis](multi-y.md) will be ordered based on the order of the
expressions on the stack. If an expression results in multiple lines, i.e. a
[group by](basics.md#group-by), then they will be sorted by the label.

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by&s=e-12h
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by&s=e-12h
@@@

### Overall

To sort all lines on a given axis using a different [mode](#sorting-modes) use the `sort` URL
parameter.

@@@ atlas-uri { hilite=sort }
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by&s=e-12h&sort=max
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by&s=e-12h&sort=max
@@@

To change it to descending order use the `order` parameter, e.g.:

@@@ atlas-uri { hilite=order }
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by&s=e-12h&sort=max&order=desc
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by&s=e-12h&sort=max&order=desc
@@@

### Group By Expression

If more control is needed, then sorting can be applied to a particular group by expression. This
can be useful for things like alerting visualizations where some common lines like the threshold
and trigger indicator should be pinned to the top, but it is desirable to sort other results
based on a stat like `max`. For example:

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by,:dup,:max,120e3,:gt,30,:alpha,:vspan,trigger,:legend,:swap,max,:sort,desc,:order,$nf.cluster,:legend&s=e-12h
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=120e3,threshold,:legend,name,sps,:eq,(,nf.cluster,),:by,:dup,:max,120e3,:gt,30,:alpha,:vspan,trigger,:legend,:swap,max,:sort,desc,:order,$nf.cluster,:legend&s=e-12h
@@@

### Sorting Modes

* `legend`: alphabetically based on the label used in the legend. This is the default.
* `min`: using the minimum value shown the legend stats.
* `max`: using the maximum value shown the legend stats.
* `avg`: using the average value shown the legend stats.
* `count`: using the count value shown the legend stats.
* `total`: using the total value shown the legend stats.
* `last`: using the last value shown the legend stats.

### Sorting Order

* `asc`: use ascending order. This is the default.
* `desc`: used descending order.