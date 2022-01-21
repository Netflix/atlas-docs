@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

Compute the standard deviation for [timers] and [distribution summaries].

[timers]: ../../spectator/core/meters/timer.md
[distribution summaries]: ../../spectator/core/meters/dist-summary.md

@@@ atlas-example { hilite=:dist-stddev }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-stddev
@@@