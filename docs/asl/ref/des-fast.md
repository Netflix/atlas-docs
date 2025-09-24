@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Apply double exponential smoothing using parameters optimized for quick adaptation to changes
in the input data. This is a convenience operator with pre-configured settings for rapid response.

## Parameters

* **expr**: The time series expression to apply fast DES smoothing to

## Examples

@@@ atlas-example { hilite=:des-fast }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:des-fast
@@@

## Related Operations

* [:des](des.md) - Full DES with custom parameters
* [:sdes-fast](sdes-fast.md) - Sliding DES equivalent (recommended alternative)
* [:des-simple](des-simple.md) - Basic DES with simple defaults

## See Also

* [DES Recommended Values](../des.md#recommended-values) - Parameter guidance