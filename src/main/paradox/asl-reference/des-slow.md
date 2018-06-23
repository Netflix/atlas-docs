
# des-slow

## Signature

```
TimeSeriesExpr -- TimeSeriesExpr
```
     
## Summary

Helper for computing DES using settings to quickly adjust to the input line. See
@ref:[recommended values](../asl/des.md#recommended-values) for more information.
For most use-cases the sliding DES variant @ref[:sdes-slow](sdes-slow.md) should be used
instead.

## Example

@@@ atlas-example
Before: /api/v1/graph?q=name,requestsPerSecond,:eq,:sum
 After: /api/v1/graph?q=name,requestsPerSecond,:eq,:sum,:des-slow
@@@
