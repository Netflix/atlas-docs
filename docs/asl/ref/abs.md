
@@@ atlas-signature
Query
-->
Query
@@@

Computes a new time series where each interval has the negated value of the input series.

Examples:

@@@ atlas-example { hilite=:neg }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:neg
@@@
