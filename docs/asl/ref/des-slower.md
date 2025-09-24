@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply double exponential smoothing using parameters optimized for very slow adaptation
to changes in the input data. This provides stable smoothing with minimal sensitivity to noise.

## Parameters

* **expr**: The time series expression to apply very slow DES smoothing to

## Examples

@@@ atlas-example { hilite=:des-slower }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:des-slower
@@@

## Related Operations

* [:des](des.md) - Full DES with custom parameters
* [:sdes-slower](sdes-slower.md) - Sliding DES equivalent (recommended alternative)
* [:des-simple](des-simple.md) - Basic DES with simple defaults