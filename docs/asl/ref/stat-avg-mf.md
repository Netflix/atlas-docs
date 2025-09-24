!!! warning
    **Deprecated:** use [:stat](stat.md) instead.

@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the average value statistic for a time series. This is a deprecated convenience
operator that is equivalent to `avg,:stat`.

## Parameters

* **expr**: The time series expression to compute the average statistic for

## Examples

@@@ atlas-example { hilite=:stat-avg-mf }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-12h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-12h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,:sum,:stat-avg-mf
@@@

## Equivalent Expression

```
# These expressions are equivalent:
name,cpu,:eq,:sum,:stat-avg-mf
name,cpu,:eq,:sum,avg,:stat
```

## Related Operations

* [:stat](stat.md) - Recommended replacement
