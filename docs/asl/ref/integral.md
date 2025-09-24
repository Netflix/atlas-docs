@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the running cumulative sum (integral) of a time series across the evaluation time window.
Each output datapoint represents the total accumulated value from the start of the time range
to that point. This is useful for calculating totals from rate data or estimating the area
under a curve.

## Parameters

* **expr**: The time series expression to compute the integral of

## Behavior

- Each output value is the cumulative sum: `integral[i] = sum(input[0] to input[i])`
- Missing values (NaN) are treated as zeros
- Negative values will decrease the cumulative total
- The result represents the area under the input curve

## Data Processing

| Input | :integral |
|-------|-----------|
| 0     | 0         |
| 1     | 1         |
| -1    | 0         |
| NaN   | 0         |
| 0     | 0         |
| 1     | 1         |
| 2     | 3         |
| 1     | 4         |
| 1     | 5         |
| 0     | 5         |

## Examples

Basic integral of a constant:

@@@ atlas-example { hilite=:integral }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=1,:integral
@@@

Integrating rate data to get total counts:

@@@ atlas-example { hilite=:integral }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,:per-step
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,:per-step,:integral
@@@

## Counter Metrics

For [counter metrics](../../spectator/core/meters/counter.md), datapoints represent average
rates per second. To get meaningful totals, first convert to per-step values using
[:per-step](per-step.md), then apply `:integral` to get the cumulative count.

## Related Operations

* [:derivative](derivative.md) - Rate of change (inverse operation)
* [:per-step](per-step.md) - Convert rates for use with integral
* [:add](add.md) - Single-step addition vs. cumulative sum
* [:rolling-sum](rolling-sum.md) - Rolling accumulation (related to cumulative operations)