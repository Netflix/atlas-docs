@@@ atlas-signature
Double
-->
TimeSeriesExpr
@@@

Generates a line where each datapoint is a constant value. Any double value that is left on
the stack will get implicitly converted to a constant line, so this operator is typically not
used explicitly.

@@@ atlas-example { hilite=:const }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42,:const
@@@
