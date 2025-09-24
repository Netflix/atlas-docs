@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply double exponential smoothing using parameters optimized for slow adaptation
to changes in the input data. This provides stable smoothing that responds gradually to changes.

## Parameters

* **expr**: The time series expression to apply slow DES smoothing to

## Examples

@@@ atlas-example { hilite=:des-slow }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:des-slow
@@@

## Related Operations

* [:des](des.md) - Full DES with custom parameters
* [:sdes-slow](sdes-slow.md) - Sliding DES equivalent (recommended alternative)
* [:des-simple](des-simple.md) - Basic DES with simple defaults