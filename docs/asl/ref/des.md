@@@ atlas-signature
beta: Double
alpha: Double
training: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply double exponential smoothing to predict future values based on trends in time series data.
This statistical method is useful for anomaly detection and forecasting by establishing a baseline
prediction that accounts for both level and trend components in the data.

!!! warning
    **Deterministic Issues**: For most use cases, [:sdes](sdes.md) (sliding DES) should be used
    instead to ensure deterministic predictions that don't depend on the exact start time of data feeding.

## Parameters

* **expr**: The time series expression to apply smoothing to
* **training**: Number of data points to use for initial training before generating predictions
* **alpha**: Smoothing factor for the level component (0.0 to 1.0, higher = more responsive to recent changes)
* **beta**: Smoothing factor for the trend component (0.0 to 1.0, higher = more responsive to recent trend changes)

## How It Works

Double exponential smoothing maintains two components:
1. **Level**: The current estimated value
2. **Trend**: The current estimated rate of change

The algorithm uses these to predict future values, but the predictions can vary depending on when
data feeding starts, making it problematic for consistent alerting and analysis.

## Examples

Applying DES with 5-point training, alpha=0.1, beta=0.5:

@@@ atlas-example { hilite=:des }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,5,0.1,0.5,:des
@@@

## Parameter Guidelines

* **Training period**: Should be long enough to capture typical behavior (typically 5-20 points)
* **Alpha (level)**: Lower values (0.1-0.3) for stable data, higher (0.5-0.9) for rapidly changing data
* **Beta (trend)**: Lower values (0.1-0.3) for stable trends, higher (0.3-0.7) for changing trends

## Limitations

* **Non-deterministic**: Same time point can have different predictions depending on data start time
* **Training dependency**: Requires sufficient historical data for meaningful predictions
* **Alerting issues**: Inconsistent predictions make threshold-based alerting unreliable

## Related Operations

* [:sdes](sdes.md) - Sliding DES (recommended alternative for most use cases)
* [:rolling-mean](rolling-mean.md) - Simple moving average (simpler alternative)
* [:trend](trend.md) - Deprecated moving average operator

## See Also

* [Double Exponential Smoothing](../des.md) - Detailed mathematical explanation