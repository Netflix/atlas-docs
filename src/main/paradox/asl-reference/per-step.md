
# per-step

## Signature

```
TimeSeriesExpr -- TimeSeriesExpr
```
     
## Summary

Converts a line from a rate per second to a rate based on the step size of the graph. This is
useful for getting an estimate of the raw number of events for a given interval.

See also @ref:[:integral](integral.md).

## Example

@@@ atlas-example
Before: /api/v1/graph?q=64
 After: /api/v1/graph?q=64,:per-step
@@@

