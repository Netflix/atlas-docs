Browse the sidebar to get a good overview of graph options. It is recommended to at least go
through the [basics](basics.md) section. There is also a quick visual index below:

<table>
<tr>
<td>Line</td>
<td>Area</td>
<td>Stack</td>
<td>Stacked Percent</td>
</tr>
<tr>
<td><a href="https://github.com/Netflix/atlas/wiki/Line-Styles#line">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Line-Styles#area">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,:area&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Line-Styles#stack">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,(,nf.cluster,),:by,:stack&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Line-Styles#stacked-percentage">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,(,nf.cluster,),:by,:pct,:stack&layout=image&zoom=0.20
@@@</p></a></td>
</tr>
<tr>
<td>VSpan</td>
<td>Transparency</td>
<td>Line Width</td>
<td>Palettes</td>
</tr>
<tr>
<td><a href="https://github.com/Netflix/atlas/wiki/Line-Styles#vertical-span">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,:dup,500e3,:gt,:vspan,40,:alpha,500e3&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Line-Attributes#transparency">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,:dup,12h,:offset,40,:alpha,:area,:swap,:area,:swap&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Line-Attributes#line-width">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,:dup,12h,:offset,8,:lw&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Color-Palettes">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=1,1,1,1,1,1,1,1,1&stack=1&layout=image&zoom=0.20
@@@</p></a></td>
</tr>
<tr>
<td>Bounds</td>
<td>Scales</td>
<td>Multi Y</td>
<td>Time Zones</td>
</tr>
<tr>
<td><a href="https://github.com/Netflix/atlas/wiki/Axis-Bounds#line">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,:stack&u=500e3&l=350e3&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Axis-Scale#area">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq&o=1&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Multi-Y">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq,nf.cluster,nccp-(p|s),:re,:and,(,nf.cluster,),:by,:stack&axis_per_line=1&layout=image&zoom=0.20
@@@</p></a></td>
<td><a href="https://github.com/Netflix/atlas/wiki/Time-Zone">
<p>@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&s=e-2d&q=name,sps,:eq&tz=UTC&tz=US/Pacific&layout=image&zoom=0.20
@@@</p></a></td>
</tr>
</table>