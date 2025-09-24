@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply sliding double exponential smoothing using parameters optimized for slow adaptation
to changes in the input data. This provides stable smoothing that is less sensitive to noise.

## Parameters

* **expr**: The time series expression to apply slow sliding DES to

## Examples

@@@ atlas-example { hilite=:sdes-slow }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:sdes-slow
@@@

## Related Operations

* [:sdes](sdes.md) - Full sliding DES with custom parameters
* [:sdes-fast](sdes-fast.md) - Fast adaptation variant
* [:sdes-slower](sdes-slower.md) - Even slower adaptation variant