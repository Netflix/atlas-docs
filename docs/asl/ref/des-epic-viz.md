@@@ atlas-signature
TimeSeriesExpr
training: Integer
alpha: Double
beta: Double
maxPercent: Double
minPercent: Double
noise: Double
-->
TimeSeriesExpr
@@@

Helper for configuring [DES](../des.md) in a manner compatible with legacy Epic alerts. For more
information see the [epic macros](../des.md#epic-macros) section of the DES page.

@@@ atlas-example { hilite=:des-epic-viz }
Example: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,10,0.1,0.5,0.2,0.2,4,:des-epic-viz
@@@