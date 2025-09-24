@@@ atlas-signature
minNumValues: Int
n: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a rolling average over a specified window of datapoints. The mean is only calculated
when there are sufficient non-NaN values in the window, making it robust against missing data.
This is useful for smoothing noisy data while maintaining data quality requirements.

## Parameters

* **expr**: The time series expression to compute the rolling mean for
* **n**: Window size (number of datapoints including current value)
* **minNumValues**: Minimum required non-NaN values to compute the mean

## Window Behavior

* **Window-based**: Uses a fixed number of datapoints, not time duration
* **Quality threshold**: Requires minimum non-NaN values before emitting a result
* **Missing data handling**: NaN values are ignored in calculation but count toward window size
* **Consolidation impact**: Each datapoint represents a longer time window when step size increases

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