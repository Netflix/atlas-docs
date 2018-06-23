
# sdes-slower

## Signature

```
TimeSeriesExpr -- TimeSeriesExpr
```
     
## Summary

Helper for computing sliding DES using settings to quickly adjust to the input line. See
@ref:[recommended values](../asl/des.md#recommended-values) for more information.

## Example

@@@ atlas-example
Before: /api/v1/graph?q=name,requestsPerSecond,:eq,:sum
 After: /api/v1/graph?q=name,requestsPerSecond,:eq,:sum,:sdes-slower
@@@
