
# rolling-count

## Signature

```
TimeSeriesExpr n:Int -- TimeSeriesExpr
```
     
## Summary

Number of occurrences within a specified window. This operation is frequently used in
alerting expressions to reduce noise. For example:

@@@ atlas-expr
-- Check to see if average cpu usage is > 80%
name,cpuUser,:eq,:avg,80,:gt,

-- Only alert if that is true for more than 3 of the last 5
-- datapoints
5,:rolling-count,3,:gt
@@@

A value is counted if it is non-zero. Missing values, `NaN`, will be treated as zeroes.
For example:

 Input | 3,:rolling-count |
-------|------------------|
 0     | 0                |
 1     | 1                |
 -1    | 2                |
 NaN   | 2                |
 0     | 1                |
 1     | 1                |
 1     | 2                |
 1     | 3                |
 1     | 3                |
 0     | 2                |

The window size, `n`, is the number of datapoints to consider including the current
value. Note that it is based on datapoints not a specific amount of time. As a result the
number of occurrences will be reduced when transitioning to a larger time frame that
causes consolidation.

For more information see the @ref:[Alerting Expressions](../asl/alerting.md) page.

## Example

@@@ atlas-example
Before: /api/v1/graph?q=:random,0.4,:gt
 After: /api/v1/graph?q=:random,0.4,:gt,5,:rolling-count
@@@

