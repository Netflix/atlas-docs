@@@ atlas-signature
duration: Duration
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Shift the time frame used when fetching the data to look at a previous interval. This is
commonly used for comparative analysis like day-over-day, week-over-week, or year-over-year
comparisons by overlaying current and historical data.

!!! warning
    **Streaming Limitations**: Offset cannot be used with streaming execution of queries.
    For real-time change detection over short intervals, consider using the
    [delay](delay.md) operator instead.

!!! info
    **Deprecated Variant**: There is a deprecated `List[Duration]` variant that only modifies
    the presentation layer. It cannot be used with mathematical operations and should be avoided.

## Parameters

* **expr**: The time series expression to apply the time offset to
* **duration**: The time duration to shift backward (e.g., `1w`, `1d`, `PT1H`)

## Duration Formats

* **Simple format**: `1w` (1 week), `1d` (1 day), `1h` (1 hour)
* **ISO 8601 format**: `PT1H` (1 hour), `P1D` (1 day), `P1W` (1 week)

## Examples

Week-over-week comparison (show current and previous week):

@@@ atlas-example { hilite=:offset }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,1w,:offset
Combined: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,:dup,1w,:offset
@@@

Hour-over-hour comparison using ISO 8601 duration:

@@@ atlas-example { hilite=:offset }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,PT1H,:offset
Combined: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,:dup,PT1H,:offset
@@@

## Common Use Cases

* **Trend analysis**: Compare current metrics with historical baselines
* **Anomaly detection**: Identify deviations from typical patterns
* **Performance regression**: Detect when current performance differs from past
* **Seasonal comparison**: Compare metrics across similar time periods

## Related Operations

* [:delay](delay.md) - Time shifting for streaming execution contexts
* [:dup](dup.md) - Duplicate series for comparison (commonly used with offset)
* [:sub](sub.md) - Calculate differences between current and offset data
* [:div](div.md) - Calculate ratios between current and offset data
* [:time](time.md) - Generate time-based values for reference
