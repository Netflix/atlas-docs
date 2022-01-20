@@@ atlas-signature
noise: Double
minPercent: Double
maxPercent: Double
beta: Double
alpha: Double
training: Int
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Helper for configuring [DES](../des.md) in a manner compatible with legacy epic alerts. For more
information see the [epic macros](../des.md#epic-macros) section of the DES page.

@@@ atlas-example { hilite=:des-epic-signal }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum,10,0.1,0.5,0.2,0.2,4,:des-epic-signal
@@@