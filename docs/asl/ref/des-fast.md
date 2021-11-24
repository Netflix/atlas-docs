@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Helper for computing DES using settings to quickly adjust to the input line. See
[recommended values](../des.md#recommended-values) for more information. For most use-cases
the sliding DES variant [:sdes-fast](sdes-fast.md) should be used instead.

@@@ atlas-example { hilite=:des-fast }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:des-fast
@@@