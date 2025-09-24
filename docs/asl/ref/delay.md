@@@ atlas-signature
n: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Delays the values in a time series by shifting them forward by N time steps. This creates
a lag effect where each value appears N intervals later than it originally occurred.
Unlike [:offset](offset.md), this operates on the computed time series data rather than
changing the time window used for data fetching.

## Parameters

* **expr**: The time series expression to delay
* **n**: The number of time steps to delay the values (integer)

## Examples

Delaying a time series by 5 time steps:

@@@ atlas-example { hilite=:delay }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,5,:delay
Combined: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,:dup,5,:delay
@@@

The "Combined" example shows both the original and delayed series overlaid, demonstrating
how the delayed series follows the same pattern but shifted later in time.

## Key Differences from :offset

* **:delay**: Operates on computed time series values, shifting them within the same time window
* **:offset**: Changes the time window used for data fetching, looking at historical data
* **Streaming compatibility**: `:delay` works with streaming queries, `:offset` does not

## Use Cases

* **Change detection**: Compare current values with slightly delayed versions to detect trends
* **Alerting**: Detect when current metrics deviate from recent patterns
* **Trend analysis**: Identify lead/lag relationships between different metrics
* **Smoothing effects**: Create visual comparisons between immediate and delayed signals

*Since: 1.6*

## Related Operations

* [:offset](offset.md) - Shift the time window for data fetching (complementary approach)
* [:dup](dup.md) - Duplicate series for comparison (commonly used with delay)
* [:sub](sub.md) - Calculate differences between original and delayed series
* [:time](time.md) - Generate time-based values for reference