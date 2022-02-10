@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

Compute the maximum recorded value for [timers] and [distribution summaries]. This
is a helper for aggregating by the max of the max statistic for the meter.

A manual query would look
like:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,statistic,max,:eq,:and,:max
@@@

Using `:dist-max` the query is reduced to:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-max
@@@

[timers]: ../../spectator/core/meters/timer.md
[distribution summaries]: ../../spectator/core/meters/dist-summary.md

@@@ atlas-example { hilite=:dist-max }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-max
@@@