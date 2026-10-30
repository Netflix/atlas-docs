@@@ atlas-signature
w: Window
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the cumulative sum of values within a rolling window. This operation
is useful for calculating totals over recent periods, tracking cumulative events, or smoothing
data by summing neighboring values.

## Parameters

* **expr**: The time series expression to apply the rolling sum to
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

Note that the result is still based on datapoints, so the value will change with the step size
even when using a duration to keep the amount of time covered fixed.

## Window Behavior

* **Inclusive**: Includes the current datapoint in the sum calculation
* **NaN handling**: NaN values are treated as 0 for summation but count toward window size

## Examples

Applying a 5-datapoint rolling sum:

@@@ atlas-example { hilite=:rolling-sum }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,5,:rolling-sum
@@@

## Data Processing Example

| Input | 3,:rolling-sum |
|-------|----------------|
| 0     | 0.0            |
| 1     | 1.0            |
| -1    | 0.0            |
| NaN   | 0.0            |
| NaN   | -1.0           |
| NaN   | NaN            |
| 1     | 1.0            |
| 1     | 2.0            |
| 1     | 3.0            |
| 0     | 2.0            |

## Related Operations

* [:rolling-mean](rolling-mean.md) - Rolling average over a window
* [:rolling-max](rolling-max.md) - Rolling maximum over a window
* [:rolling-min](rolling-min.md) - Rolling minimum over a window
* [:rolling-count](rolling-count.md) - Rolling count of non-zero values
* [:integral](integral.md) - Cumulative sum over entire time window (not rolling)
* [:sum](sum.md) - Total aggregation across time series

Since: 1.6