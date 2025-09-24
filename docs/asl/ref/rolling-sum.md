@@@ atlas-signature
n: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the cumulative sum of values within a rolling window of N datapoints. This operation
is useful for calculating totals over recent periods, tracking cumulative events, or smoothing
data by summing neighboring values.

## Parameters

* **expr**: The time series expression to apply the rolling sum to
* **n**: Window size in number of datapoints (positive integer, includes current value)

## Window Behavior

* **Datapoint-based**: Uses a fixed number of datapoints, not time duration
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

## Consolidation Impact

Since the window is based on datapoints rather than time, the effective time coverage changes
when step size increases due to consolidation. Each datapoint represents a longer time window
when the step size is larger.

## Related Operations

* [:rolling-mean](rolling-mean.md) - Rolling average over datapoint windows
* [:rolling-max](rolling-max.md) - Rolling maximum over datapoint windows
* [:rolling-min](rolling-min.md) - Rolling minimum over datapoint windows
* [:rolling-count](rolling-count.md) - Rolling count of non-NaN values
* [:integral](integral.md) - Cumulative sum over entire time window (not rolling)
* [:sum](sum.md) - Total aggregation across time series

Since: 1.6