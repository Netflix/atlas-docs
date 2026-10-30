@@@ atlas-signature
w: Window
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Find the minimum value within a rolling window of datapoints. This operation is useful for
tracking low-water marks, establishing lower bounds for noisy data, and creating envelope
functions that follow the lowest points in fluctuating signals.

## Parameters

* **expr**: The time series expression to find rolling minimum for
* **w**: Window size, either a number of datapoints including the current value, such as
  `5`, or a duration, such as `5m`. See [Window Size](#window-size)

## Window Size

The window can be specified as a number of datapoints or as an amount of time. A number of
datapoints, `5`, will consider the last 5 values, including the current value. The amount of
time covered then changes with the step size, for example when zooming out to a time frame that
causes consolidation. A duration, `5m`, will consider the values for the last 5 minutes
independent of the step size. The duration is rounded down to the nearest step boundary, so a
`5m` window with a 2m step will use a 4m window with two datapoints. If the step size is larger
than the window, then the window will be a single datapoint and the input is passed through
unchanged. The window must be positive.

## Behavior

* **Minimum selection**: Returns the lowest value in the current window
* **Missing data**: NaN values are ignored in the calculation
* **All NaN window**: If all values in window are NaN, emits NaN

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