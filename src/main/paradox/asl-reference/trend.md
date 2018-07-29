
# trend

## Signature

```
TimeSeriesExpr window:Duration -- TimeSeriesExpr
```
     
## Summary

Computes a moving average over the input window. Until there is at least one sample
for the whole window it will emit `NaN`. If the input line has `NaN` values, then they
will be treated as zeros. Example:

 Input | 2m,:trend | 5m,:trend |
-------|-----------|-----------|
   0   |  NaN      | NaN       |
   1   |  0.5      | NaN       |
  -1   |  0.0      | NaN       |
 NaN   | -0.5      | NaN       |
   0   |  0.0      | 0.0       |
   1   |  0.5      | 0.2       |
   2   |  1.5      | 0.4       |
   1   |  1.5      | 0.8       |
   1   |  1.0      | 1.0       |
   0   |  0.5      | 1.0       |

The window size is specified as a range of time. If the window size is not evenly
divisible by the @ref:[step size](../concepts.md#step-size), then the window size will be
rounded down. So a 5m window with a 2m step would result in a 4m window with two datapoints
per average. A step size larger than the window will result in the trend being a no-op.

## Example

@@@ atlas-example
Before: /api/v1/graph?q=:random
 After: /api/v1/graph?q=:random,5m,:trend
@@@

