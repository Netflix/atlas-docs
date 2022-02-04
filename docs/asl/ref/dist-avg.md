@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

Compute the average recorded value for [timers] and [distribution summaries]. This
is calculated by dividing the total amount recorded by the number of recorded values.

For [Timer] and Distribution Summary metrics, the `totalTime` (timers) /`totalAmount` (distributions)
and `count` are collected each time a measurement is taken. If this technique was applied to a
request latency metric, then you would have the average latency per request for an arbitrary
grouping. These types of metrics have an explicit count based on activity. To get an average
per measurement manually:

@@@ atlas-stacklang
/api/v1/graph?q=statistic,totalTime,:eq,:sum,statistic,count,:eq,:sum,:div
@@@

This expression can be bound to a query using the [:cq] (common query) operator:

@@@ atlas-stacklang
/api/v1/graph?q=statistic,totalTime,:eq,:sum,statistic,count,:eq,:sum,:div,nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:cq
@@@

Using the `:dist-avg` function reduces the query to:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-avg
@@@

To compute the average by group, apply the group after the `:dist-avg` function:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-avg,(,nf.asg,),:by
@@@

[:cq]: cq.md
[timers]: ../../spectator/core/meters/timer.md
[distribution summaries]: ../../spectator/core/meters/dist-summary.md

@@@ atlas-example { hilite=:dist-avg }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,playback.startLatency,:eq,:dist-avg
@@@