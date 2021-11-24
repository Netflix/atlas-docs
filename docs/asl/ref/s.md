@@@ atlas-signature
TimeSeriesExpr
s: String
r: String
-->
StyleExpr
@@@

Perform a search and replace on the legend strings. This command is similar
to the global search and replace (`s/regexp/replace/g`) operation from tools
like [vim][vim] or [sed][sed].

[vim]: http://vim.wikia.com/wiki/Search_and_replace
[sed]: https://linux.die.net/man/1/sed

The replacement string can use variables to refer to the capture groups of the
input expression. The syntax is that same as for [legends](legend.md).

Since: 1.6

Examples:

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,^nccp-(.*)$,$1,:s
@@@

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,^nccp-(?<stack>.*)$,$stack,:s
@@@

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,nccp-,_,:s
@@@

@@@ atlas-example { hilite=:s }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,(,nf.cluster,),:by,$nf.cluster,:legend,([a-z]),_$1,:s
@@@