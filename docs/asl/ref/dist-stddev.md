@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

Compute the standard deviation for [timers] and [distribution summaries].

[timers]: http://netflix.github.io/spectator/en/latest/intro/timer/
[distribution summaries]: http://netflix.github.io/spectator/en/latest/intro/dist-summary/

@@@ atlas-example { hilite=:dist-stddev }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-stddev
@@@