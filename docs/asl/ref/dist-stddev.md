@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

Compute the standard deviation for [timers] and [distribution summaries].

A manual query would look like:

@@@ atlas-stacklang
/api/v1/graph?q=statistic,count,:eq,:sum,statistic,totalOfSquares,:eq,:sum,:mul,statistic,totalTime,:eq,:sum,:dup,:mul,:sub,statistic,count,:eq,:sum,:dup,:mul,:div,:sqrt,nf.cluster,foo,:eq, name,http.req.latency,:eq,:and,:cq
@@@

This is much simpler using the `:dist-stddev` function:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-stddev
@@@

[timers]: ../../spectator/core/meters/timer.md
[distribution summaries]: ../../spectator/core/meters/dist-summary.md

@@@ atlas-example { hilite=:dist-stddev }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-stddev
@@@