@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply sliding double exponential smoothing using parameters optimized for quick adaptation
to changes in the input data. This provides deterministic smoothing with rapid response characteristics.

## Parameters

* **expr**: The time series expression to apply fast sliding DES to

## Examples

@@@ atlas-example { hilite=:sdes-fast }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:sdes-fast
@@@

## Related Operations

* [:sdes](sdes.md) - Full sliding DES with custom parameters
* [:des-fast](des-fast.md) - Standard DES equivalent (less stable)
* [:sdes-simple](sdes-simple.md) - Basic sliding DES with simple defaults