@@@ atlas-signature
n: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Count the number of non-zero occurrences within a rolling window of datapoints. This operation
is particularly valuable for alerting to reduce noise and ensure conditions persist over
multiple datapoints before triggering alerts.

## Parameters

* **expr**: The time series expression to count occurrences for
* **n**: Window size (number of datapoints including current value)

## Counting Rules

* **Non-zero values**: Only values != 0 are counted as occurrences
* **Missing data**: NaN values are treated as zero (not counted)
* **Negative values**: Negative non-zero values are counted as occurrences
* **Window-based**: Uses fixed number of datapoints, not time duration

## Alerting Pattern

A common alerting pattern using rolling count:

```
# Check if average CPU usage > 80%
name,cpuUser,:eq,:avg,80,:gt,

# Only alert if condition is true for 3+ of the last 5 datapoints
5,:rolling-count,3,:gt
```

## Data Processing Example

| Input | 3,:rolling-count |
|-------|------------------|
| 0     | 0                |
| 1     | 1                |
| -1    | 2                |
| NaN   | 2                |
| 0     | 1                |
| 1     | 1                |
| 1     | 2                |
| 1     | 3                |
| 1     | 3                |
| 0     | 2                |

## Examples

Counting positive occurrences in a 5-point window:

@@@ atlas-example { hilite=:rolling-count }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,0.4,:gt
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=:random,0.4,:gt,5,:rolling-count
@@@

## Related Operations

* [:rolling-mean](rolling-mean.md) - Rolling average of values
* [:rolling-max](rolling-max.md) - Rolling maximum values
* [:rolling-min](rolling-min.md) - Rolling minimum values
* [:gt](gt.md) - Generate boolean conditions for counting

## See Also

* [Alerting Expressions](../alerting-expressions.md) - Patterns for using rolling operations in alerts