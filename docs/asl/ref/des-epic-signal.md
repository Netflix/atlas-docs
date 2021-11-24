@@@ atlas-signature
TimeSeriesExpr
training: Integer
alpha: Double
beta: Double
-->
TimeSeriesExpr
@@@

[Double exponential smoothing](DES). For most use-cases [sliding DES](sdes.md)
should be used instead to ensure a deterministic prediction.

@@@ atlas-example { hilite=:des }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestsPerSecond,:eq,:sum,5,0.1,0.5,:des
@@@