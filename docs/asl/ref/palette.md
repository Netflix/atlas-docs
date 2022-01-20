@@@ atlas-signature
String
TimeSeriesExpr
-->
StyleExpr
@@@

Set the [palette](../../api/graph/color-palettes.md) to use for the results of an expression. This
operator is allows for scoping a palette to a particular group by instead of to
all lines that share the same axis. A common use-case is to have multiple stacked
group by expressions using different palettes. For example, suppose I want to create
a graph showing overall request per second hitting my services with successful requests
shown in shades of [green](../../api/graph/color-palettes.md#greens) and errors in shades of
[red](../../api/graph/color-palettes.md#reds). This can make it easy to visually see if a change is
due to an increase in errors:

![Spike in Errors](../../images/palette-errors.png)

Or a spike in successful requests:

![Spike in Success](../../images/palette-success.png)

Examples:

@@@ atlas-example { hilite=:palette }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,reds,:palette
@@@

@@@ atlas-example { hilite=:palette }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,reds,:palette
@@@