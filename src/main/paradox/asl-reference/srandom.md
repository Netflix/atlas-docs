
# srandom

## Signature

```
seed:Int -- TimeSeriesExpr
```
     
## Summary

Generate a time series that appears to be random noise for the purposes of
creating sample data to experiment with expressions. To ensure that the line is deterministic
and reproducible it actually is based on a hash of the timestamp. Different seed values can
be used to generate distinct noise lines. Each datapoint is a value between 0.0 and 1.0.

See also @ref:[:random](random.md).

Since 1.6.0

## Example

@@@ atlas-graph { show-expr=true }
/api/v1/graph?q=1,:srandom,2,:srandom
@@@
