
# des-slower

## Signature

```
TimeSeriesExpr -- TimeSeriesExpr
```
     
## Summary

Helper for computing DES using settings to quickly adjust to the input line. See
@ref:[recommended values](../asl/des.md#recommended-values) for more information.
For most use-cases the sliding DES variant @ref[:sdes-slower](sdes-slower.md) should be used
instead.

## Example

@@@ atlas-graph { show-expr=true }
/api/v1/graph?q=name,requestsPerSecond,:eq,:sum,:des-slower
@@@
