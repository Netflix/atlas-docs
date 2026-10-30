@@@ atlas-signature
minNumValues: Int
w: Window
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a rolling average over a specified window of datapoints. The mean is only calculated
when there are sufficient non-NaN values in the window, making it robust against missing data.
This is useful for smoothing noisy data while maintaining data quality requirements.

## Parameters

* **expr**: The time series expression to compute the rolling mean for
* **w**: Window size, either a number of datapoints including the current value, such as
  `5`, or a duration, such as `5m`. See [Window Size](#window-size)
* **minNumValues**: Minimum required non-NaN values to compute the mean

## Window Size

The window can be specified as a number of datapoints or as an amount of time. A number of
datapoints, `5`, will consider the last 5 values, including the current value. The amount of
time covered then changes with the step size, for example when zooming out to a time frame that
causes consolidation. A duration, `5m`, will consider the values for the last 5 minutes
independent of the step size. The duration is rounded down to the nearest step boundary, so a
`5m` window with a 2m step will use a 4m window with two datapoints. If the step size is larger
than the window, then the window will be a single datapoint. The window must be positive.

## Window Behavior

* **Quality threshold**: Requires minimum non-NaN values before emitting a result
* **Missing data handling**: NaN values are ignored in calculation but count toward window size
* **Consolidation impact**: With a number of datapoints, each datapoint represents a longer time
  window when the step size increases. Use a duration to keep the time covered fixed
* **Small windows**: If `minNumValues` is larger than the number of datapoints in the window,
  for example a duration window at a large step size, the result is NaN

## Data Processing Example

| Input | 3,2,:rolling-mean |
|-------|-------------------|
| 0     | NaN               |
| 1     | 0.5               |
| -1    | 0.0               |
| NaN   | 0.0               |
| NaN   | NaN               |
| 0     | NaN               |
| 1     | 0.5               |
| 1     | 0.667             |
| 1     | 1                 |
| 0     | 0.667             |

## Examples

5-point rolling mean with minimum 3 values:

@@@ atlas-example { hilite=:rolling-mean }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,5,3,:rolling-mean
@@@

## Related Operations

* [:rolling-max](rolling-max.md) - Rolling maximum values
* [:rolling-min](rolling-min.md) - Rolling minimum values
* [:rolling-count](rolling-count.md) - Count non-zero values in window
* [:trend](trend.md) - Time-based moving average (deprecated)
* [:avg](avg.md) - Global average across all values

Since: 1.6