Occasionally it is useful to show a graph, but the exact values need to be suppressed. This can
be useful for communicating with external support or including in a presentation. To avoid showing
the actual values disable tick labels using `tick_labels=off` and either
[disable the legend](legends.md#disable) or [disable the legend stats](legends.md#disable-stats).

@@@ atlas-uri { hilite=tick_labels%3Doff }
/api/v1/graph?e=2012-01-01T00:00&no_legend_stats=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=off
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend_stats=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=off
@@@

If you also want to suppress the time axis, then use the `only_graph` option:

@@@ atlas-uri { hilite=only_graph%3D1 }
/api/v1/graph?e=2012-01-01T00:00&only_graph=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&only_graph=1&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w
@@@
