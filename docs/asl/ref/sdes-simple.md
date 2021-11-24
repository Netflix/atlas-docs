@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Helper for computing DES using default values.

!!! Warning 
    The values used by this operation are prone to wild oscillations. See
    [recommended values](../des.md#recommended-values) for better options.

@@@ atlas-example { hilite=:des-simple }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,:des-simple
@@@