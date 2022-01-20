@@@ atlas-signature
name: String
rewritten: TimeSeriesExpr
original: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Internal operation used by some macros to provide a more user friendly display
expression. The expanded version will get used for evaluation, but if a new expression
is generated from the parsed expression tree it will use the original version
along with the named of the macro.

@@@ atlas-example { hilite=:named-rewrite }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,:dup,:dup,:sum,:swap,:count,:div
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,:dup,:dup,:sum,:swap,:count,:div,avg,:named-rewrite
@@@