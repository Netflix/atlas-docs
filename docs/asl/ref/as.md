
@@@ atlas-signature
replacement: String
original: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Rename a tag key to use an alternative name. This operator creates a mapping from one tag key
to another, which is essential for performing mathematical operations between time series that
use different tag keys to represent the same conceptual dimension.

## Parameters

* **expr**: The time series expression to apply tag key renaming to
* **original**: The existing tag key name to be renamed
* **replacement**: The new tag key name to use

## Common Use Cases

### Binary Math Operations
When performing operations like addition, subtraction, or division between time series from
different sources, tag keys must match for proper alignment. In most cases, the data should
be cleaned up so renaming is not necessary. If that is not possible, then the `:as` operator
can rename one side to align the keys.

### IPC Metrics Comparison
A common scenario involves comparing server and client perspectives of the same interactions.
The [common IPC](../../spectator/specs/ipc.md) metrics illustrate this pattern:

* **Server side**: Groups by `nf.app` (the server application)
* **Client side**: Groups by `ipc.server.app` (the server being called)

Both represent the same application, but use different tag keys.

## Examples

Basic tag key renaming for legend display:

@@@ atlas-example { hilite=:as }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.cluster,),:by,nf.cluster,c,:as,$c,:legend
@@@

## Mathematical Operation Alignment

```
# Server-side requests per second (grouped by nf.app):
name,server.requests,:eq,(,nf.app,),:by

# Client-side requests per second (grouped by ipc.server.app):
name,client.requests,:eq,(,ipc.server.app,),:by,ipc.server.app,nf.app,:as

# Now both can be combined since they share the same tag key:
name,server.requests,:eq,(,nf.app,),:by,
name,client.requests,:eq,(,ipc.server.app,),:by,ipc.server.app,nf.app,:as,
:sub
```

## Related Operations

* [:legend](legend.md) - Custom legend text with variable substitution
* [:s](s.md) - Search and replace on legend strings
* [:by](by.md) - Group time series by tag keys
* [:add](add.md) / [:sub](sub.md) / [:mul](mul.md) / [:div](div.md) - Mathematical operations requiring aligned tag keys

## See Also

* [Common IPC Specifications](../../spectator/specs/ipc.md) - Examples of server/client tag key differences
