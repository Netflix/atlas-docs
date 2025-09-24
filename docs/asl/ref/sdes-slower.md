@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply sliding double exponential smoothing using parameters optimized for very slow adaptation
to changes in the input data. This provides the most stable smoothing with minimal sensitivity to noise.

## Parameters

* **expr**: The time series expression to apply very slow sliding DES to

## Examples

@@@ atlas-example { hilite=:sdes-slower }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:sdes-slower
@@@

## Related Operations

* [:sdes](sdes.md) - Full sliding DES with custom parameters
* [:sdes-slow](sdes-slow.md) - Slow adaptation variant
* [:des-slower](des-slower.md) - Standard DES equivalent (less stable)