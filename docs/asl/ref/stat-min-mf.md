!!! warning
    **Deprecated:** use [:stat](stat.md) instead.

@@@ atlas-signature
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Equivalent to `min,:stat`. Example of usage:

@@@ atlas-example { hilite=:stat-min-mf }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-12h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-12h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,:stat-min-mf
@@@
