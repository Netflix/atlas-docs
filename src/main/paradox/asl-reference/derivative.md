
# derivative

## Signature

```
TimeSeriesExpr -- TimeSeriesExpr
```
     
## Summary

Computes the amount of change per step of the input time series. The most common use-case is
to convert a monotonically increasing input time series into a time series showing the rate
of change over time.

See also @ref:[:integral](integral.md).

## Example

@@@ atlas-example
Before: /api/v1/graph?q=minuteOfHour,:time
 After: /api/v1/graph?q=minuteOfHour,:time,:derivative
@@@

