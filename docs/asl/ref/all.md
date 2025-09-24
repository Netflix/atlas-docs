!!! warning
    **Deprecated:** use [:by](by.md) instead. This operation is primarily intended for
    debugging and results can be confusing unless you have detailed understanding of Atlas
    internals.

@@@ atlas-signature
query: Query
-->
DataExpr
@@@

Avoid aggregation and output all time series that match the query. This bypasses the normal
aggregation behavior and returns every individual time series, which can result in extremely
large result sets.

## Parameters

* **query**: The query to execute without aggregation

## Related Operations

* [:by](by.md) - Recommended replacement for proper grouping