The following color palettes are supported:

* [armytage](#armytage)
* [epic](#epic)
* [blues](#blues)
* [greens](#greens)
* [oranges](#oranges)
* [purples](#purples)
* [reds](#reds)
* [custom](#custom)

There is also a [hashed selection](#hashed-selection) mode that can be used so that a line
with a given label will always get the same color.

## Armytage

This is the default color palette, it comes from the paper
[A Colour Alphabet and the Limits of Colour Coding](http://www.aic-color.org/journal/previous_archivos/v5/jaic_v5_06.pdf)
by Paul Green-Armytage. Two colors, Xanthin and Yellow, are excluded because users found them hard
to distinguish from a white background when used for a single pixel line. So overall there are
24 distinct colors with this palette.

@@@ atlas-uri { hilite=palette%3Darmytage }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=armytage&stack=1&tz=UTC&q=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=armytage&stack=1&tz=UTC&q=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
@@@

## Epic

This is a legacy palette that alternates between shades of red, green, and blue. It is supported
for backwards compatibility, but not recommended.

@@@ atlas-uri { hilite=palette%3Depic }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=epic&stack=1&tz=UTC&q=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=epic&stack=1&tz=UTC&q=1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
@@@

## Blues

Shades of blue.

@@@ atlas-uri { hilite=palette%3Dblues }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=blues&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=blues&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

## Greens

Shades of green.

@@@ atlas-uri { hilite=palette%3Dgreens }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=greens&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=greens&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

## Oranges

Shades of orange.

@@@ atlas-uri { hilite=palette%3Doranges }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=oranges&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=oranges&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

## Purples

Shades of purple.

@@@ atlas-uri { hilite=palette%3Dpurples }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=purples&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=purples&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

## Reds

Shades of red.

@@@ atlas-uri { hilite=palette%3Dreds }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=reds&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=reds&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

## Custom

A custom color palette can be provided for a graph by using a prefix of `colors:` followed by
a comma separated list of [hex color](../../asl/ref/color.md) values. This is mainly used to customize the
colors for the result of a group by where you cannot set the color for each line using
[:color](../../asl/ref/color.md).

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=colors:1a9850,91cf60,d9ef8b,fee08b,fc8d59,d73027&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=colors:1a9850,91cf60,d9ef8b,fee08b,fc8d59,d73027&stack=1&tz=UTC&q=1,1,1,1,1,1,1
@@@

## Hashed Selection

Any of the palettes above can be prefixed with `hash:` to select the color using a hashing
function on the label rather than picking the next color from the list. The primary advantage
is that the selected color will always be the same for a given label using a particular
palette. However, some nice properties of the default mode are lost:

* Colors can be duplicated even with a small number of lines. Hash collisions will result
  in the same color.
* The palettes are ordered to try and make the stacked appearance and legends easier to
  read. For the [armytage](#armytage) palette it is ordered so adjacent colors are easy
  to distinguish. For the palettes that are shades of a color they are ordered from dark
  to light shades to create a gradient effect. Hashing causes an arbitrary ordering of
  the colors from the palette.

The table below illustrates the difference by adding some additional lines to a chart
for the second row:

<table>
<thead>
  <th width="50%">armytage</th>
  <th width="50%">hash:armytage</th>
</thead>
<tbody>
<tr>
  <td>
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,(,nf.cluster,),:by&stack=1&palette=armytage&layout=iw&w=350&h=150&no_legend_stats=1
@@@</p></td>
  <td>
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,(,nf.cluster,),:by&stack=1&palette=hash:armytage&layout=iw&w=350&h=150&no_legend_stats=1
@@@</p></td>
</tr>
<tr>
  <td>
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=40e3,20e3,name,sps,:eq,(,nf.cluster,),:by&stack=1&palette=armytage&layout=iw&w=350&h=150&no_legend_stats=1
@@@</p></td>
  <td>
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=40e3,20e3,name,sps,:eq,(,nf.cluster,),:by&stack=1&palette=hash:armytage&layout=iw&w=350&h=150&no_legend_stats=1
@@@</p></td>
</tr>
</tbody>
</table>

Example:

@@@ atlas-uri
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=hash:armytage&q=name,sps,:eq,(,nf.cluster,),:by,:stack&tz=UTC
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&no_legend=1&palette=hash:armytage&q=name,sps,:eq,(,nf.cluster,),:by,:stack&tz=UTC
@@@
