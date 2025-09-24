@@@ atlas-signature
n: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Find the maximum value within a rolling window of datapoints. This operation is useful for
tracking peak values, establishing upper bounds for noisy data, and creating envelope
functions that follow the highest points in fluctuating signals.

## Parameters

* **expr**: The time series expression to find rolling maximum for
* **n**: Window size (number of datapoints including current value)

## Behavior

* **Maximum selection**: Returns the highest value in the current window
* **Missing data**: NaN values are ignored in the calculation
* **All NaN window**: If all values in window are NaN, emits NaN
* **Window-based**: Uses fixed number of datapoints, not time duration

## Alerting Example

Using rolling max to establish recent peak baseline:

```
name,sps,:eq,:sum,
:dup,
5,:rolling-max
```

This creates both the current value and its recent maximum for comparison.

## Data Processing Example

| Input | 3,:rolling-max |
|-------|----------------|
| 0     | 0              |
| 1     | 1              |
| -1    | 1              |
| NaN   | 1              |
| 0     | 0              |
| 1     | 1              |
| 1     | 1              |
| 1     | 1              |
| 1     | 1              |
| 0     | 1              |

## Examples

5-point rolling maximum:

@@@ atlas-example { hilite=:rolling-max }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,0.4,:gt
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,0.4,:gt,5,:rolling-max
@@@

## Related Operations

* [:rolling-min](rolling-min.md) - Rolling minimum values
* [:rolling-mean](rolling-mean.md) - Rolling average values
* [:rolling-count](rolling-count.md) - Count non-zero values in window
* [:max](max.md) - Global maximum across all values

Since: 1.6