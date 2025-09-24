@@@ atlas-signature
noise: Double
minPercent: Double
maxPercent: Double
beta: Double
alpha: Double
training: Int
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Configure double exponential smoothing for signal generation in a manner compatible with legacy
Epic alert systems. This operator generates alert signals using Epic-compatible thresholds and
parameters for seamless migration from Epic-based monitoring.

## Parameters

* **expr**: The time series expression to apply Epic-compatible DES signal generation to
* **training**: Number of data points to use for initial training
* **alpha**: Smoothing factor for the level component (0.0 to 1.0)
* **beta**: Smoothing factor for the trend component (0.0 to 1.0)
* **maxPercent**: Maximum percentage threshold for Epic compatibility
* **minPercent**: Minimum percentage threshold for Epic compatibility
* **noise**: Noise tolerance parameter for Epic compatibility

## Examples

@@@ atlas-example { hilite=:des-epic-signal }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,10,0.1,0.5,0.2,0.2,4,:des-epic-signal
@@@

## Related Operations

* [:des-epic-viz](des-epic-viz.md) - Epic-compatible visualization
* [:des](des.md) - Standard DES with custom parameters

## See Also

* [Epic Macros](../des.md#epic-macros) - Detailed Epic compatibility documentation