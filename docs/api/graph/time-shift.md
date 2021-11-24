A common use-case is to compare a given line with a shifted line to compare week-over-week or day-over-day.

@@@ atlas-uri { hilite=:offset }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,nf.cluster,nccp-silverlight,:eq,:and,:sum,:dup,1w,:offset
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,nf.cluster,nccp-silverlight,:eq,:and,:sum,:dup,1w,:offset
@@@

The `$(atlas.offset)` variable can be used to show the offset in a custom legend:

@@@ atlas-uri { hilite=:offset }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,nf.cluster,nccp-silverlight,:eq,:and,:sum,:dup,1w,:offset,:list,(,$nf.cluster+(offset=$atlas.offset),:legend,),:each
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,nf.cluster,nccp-silverlight,:eq,:and,:sum,:dup,1w,:offset,:list,(,$nf.cluster+(offset=$atlas.offset),:legend,),:each
@@@
