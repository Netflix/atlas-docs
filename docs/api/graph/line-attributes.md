In addition to the [line style](line-styles.md) and [legend](legends.md) the following attributes
can be adjusted:

* [Color](#color)
* [Transparency](#transparency)
* [Line Width](#line-width)

## Color

By default the color will come from the [palette](color-palettes.md) that is in use. However the
color for a line can also be set explicitly using the [:color](../../asl/ref/color.md) operator:

@@@ atlas-uri { hilite=color }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,f00,:color&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,f00,:color&s=e-1w
@@@

Note, that for a group by all results will get the same attributes, so in this case all would
end up being the same color:

@@@ atlas-uri { hilite=color }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,f00,:color&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,(,nf.cluster,),:by,f00,:color&s=e-1w
@@@

## Transparency

The transparency of a line can be set using the [:alpha](../../asl/ref/alpha.md) operator or by explicitly
setting the alpha channel as part of the [color](../../asl/ref/color.md).

@@@ atlas-uri { hilite=alpha }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,6h,:offset,:area,40,:alpha&s=e-2d
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,6h,:offset,:area,40,:alpha&s=e-2d
@@@

Setting the alpha explicitly as part of the color:

@@@ atlas-uri { hilite=color }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,6h,:offset,:area,40ff0000,:color&s=e-2d
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,6h,:offset,:area,40ff0000,:color&s=e-2d
@@@

## Line Width

Adjust the stroke width used for a line:

@@@ atlas-uri { hilite=lw }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,6h,:offset,3,:lw&s=e-1w
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&no_legend=1&q=name,sps,:eq,:dup,6h,:offset,3,:lw&s=e-1w
@@@
