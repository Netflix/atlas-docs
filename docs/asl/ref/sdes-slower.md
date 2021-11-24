@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Helper for computing DES using settings to slowly adjust to the input line. See
[recommended values](../des.md#recommended-values) for more information. For most use-cases
the sliding DES variant [:sdes-slower](stateful-sdes‐slower) should be used instead.

@@@ atlas-example { hilite=:des-slower }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:des-slower
@@@