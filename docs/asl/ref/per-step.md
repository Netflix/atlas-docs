@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Converts a line from a rate per second to a rate based on the step size of the graph.
This is useful for getting an estimate of the raw number of events for a given
interval.

@@@ atlas-example { hilite=:per-step }
0: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=0,:per-step
64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=64,:per-step
-64: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=-64,:per-step
@@@