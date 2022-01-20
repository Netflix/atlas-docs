
@@@ atlas-signature
replacement: String
original: String
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Map a tag key name to an alternate name. This can be useful for cases where it is desirable
to perform a binary math operation, but the two sides use different tag keys for the same
concept. The [common IPC](../../spectator/specs/ipc.md) metrics are an example where it might
be desirable to compare RPS for servers and their clients. The server side RPS would group by
`nf.app` while the client side view would group by `ipc.server.app`.

@@@ atlas-example { hilite=:as }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by,nf.cluster,c,:as,$c,:legend
@@@
