Examples for using multiple Y-axes:

* [Explicit](#explicit)
* [Explicit Bounds](#explicit-bounds)
* [Axis Per Line](#axis-per-line)
* [Palettes](#palettes)

## Explicit

By default all lines will go on axis `0`, the one on the left side. A different axis can be
specified using the [:axis](../asl/ref/axis.md) operation.

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,42,1,:axis
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,42,1,:axis
@@@

## Explicit Bounds

By default all axes will pick up [axis settings](Graph#y-axis) with no qualifier:

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&l=0&q=name,sps,:eq,42,1,:axis
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&l=0&q=name,sps,:eq,42,1,:axis
@@@

Bounds and other axis settings can be set per axis, e.g., this graph moves the constant line for
`42` to a separate axis and sets the lower bound to `0` via the `&l.1=0` parameter. This would 
work as well for `&u.1=100e3`. Append the index after the `l.` or `u.` :

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&l.1=0&q=name,sps,:eq,42,1,:axis
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&l.1=0&q=name,sps,:eq,42,1,:axis
@@@

## Axis Per Line

There is a convenience operation to plot each line on a separate axis.

@@@ atlas-uri { hilite=axis_per_line%3D1 }
/api/v1/graph?e=2012-01-01T00:00&axis_per_line=1&q=name,sps,:eq,nf.cluster,nccp-p,:re,:and,(,nf.cluster,),:by
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&axis_per_line=1&q=name,sps,:eq,nf.cluster,nccp-p,:re,:and,(,nf.cluster,),:by
@@@

If there are too many lines and it would be over the max Y-axis limit, then a warning will be shown:

@@@ atlas-uri { hilite=axis_per_line%3D1 }
/api/v1/graph?e=2012-01-01T00:00&axis_per_line=1&q=name,sps,:eq,(,nf.cluster,),:by
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&axis_per_line=1&q=name,sps,:eq,(,nf.cluster,),:by
@@@

## Palettes

The color of the first line on an axis will get used as the color of the axis. The intention is
to make it easy to understand which axis a line is associated with and in an image dynamic clues
like hover cannot be used. Generally it is recommended to only have one line per axis when using
multi-Y. Example:

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&l=01&q=name,sps,:eq,(,nf.cluster,),:by,minuteOfHour,:time,1,:axis
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&l=01&q=name,sps,:eq,(,nf.cluster,),:by,minuteOfHour,:time,1,:axis
@@@

Though we recommend not using more than one line per axis with multi-Y, a
[color palette](Color-Palettes) can be specified for a specific axis. This can be used to
select shades of a color for an axis so it is still easy to visually associate which axis a line
belongs to:

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T00:00&l=01&palette.0=reds&palette.1=blues&q=name,sps,:eq,(,nf.cluster,),:by,:stack,minuteOfHour,:time,1,:axis
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&l=01&palette.0=reds&palette.1=blues&q=name,sps,:eq,(,nf.cluster,),:by,:stack,minuteOfHour,:time,1,:axis
@@@
