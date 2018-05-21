
# des

## Signature

`TimeSeriesExpr training:Int alpha:Double beta:Double -- TimeSeriesExpr`

## Summary

@ref:[Double exponential smoothing](../asl/des.md). For most use-cases
@ref:[sliding DES](sdes.md) should be used instead to ensure a deterministic prediction.

## Example

@@@ atlas-graph { show-expr=true }
/api/v1/graph?q=name,requestsPerSecond,:eq,:sum,:dup,input,:legend,:swap,5,0.1,0.5,:des,des,:legend
@@@