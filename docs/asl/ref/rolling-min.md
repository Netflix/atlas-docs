@@@ atlas-signature
n: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Find the minimum value within a rolling window of datapoints. This operation is useful for
tracking low-water marks, establishing lower bounds for noisy data, and creating envelope
functions that follow the lowest points in fluctuating signals.

## Parameters

* **expr**: The time series expression to find rolling minimum for
* **n**: Window size (number of datapoints including current value)

## Behavior

* **Minimum selection**: Returns the lowest value in the current window
* **Missing data**: NaN values are ignored in the calculation
* **All NaN window**: If all values in window are NaN, emits NaN
* **Window-based**: Uses fixed number of datapoints, not time duration

## Alerting Example

Using rolling min to establish recent low baseline:

```
name,sps,:eq,:sum,
:dup,
5,:rolling-min
```

This creates both the current value and its recent minimum for comparison.

## Data Processing Example

| Input | 3,:rolling-min |
|-------|----------------|
| 0     | 0              |
| 1     | 0              |
| -1    | -1             |
| NaN   | -1             |
| 0     | -1             |
| 1     | 0              |
| 1     | 0              |
| 1     | 1              |
| 1     | 1              |
| 0     | 0              |

## Examples

5-point rolling minimum:

@@@ atlas-example { hilite=:rolling-min }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,5,:rolling-min
@@@

## Related Operations

* [:rolling-max](rolling-max.md) - Rolling maximum values
* [:rolling-mean](rolling-mean.md) - Rolling average values
* [:rolling-count](rolling-count.md) - Count non-zero values in window
* [:min](min.md) - Global minimum across all values

Since: 1.6