!!! warning
    **Deprecated:** use [:stat](stat.md) instead.

@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the minimum value statistic for a time series. This is a deprecated convenience
operator that is equivalent to `min,:stat`.

## Parameters

* **expr**: The time series expression to compute the minimum statistic for

## Examples

@@@ atlas-example { hilite=:stat-min-mf }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-12h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-12h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,:stat-min-mf
@@@

## Equivalent Expression

```
# These expressions are equivalent:
name,cpu,:eq,:sum,:stat-min-mf
name,cpu,:eq,:sum,min,:stat
```

## Related Operations

* [:stat](stat.md) - Recommended replacement
