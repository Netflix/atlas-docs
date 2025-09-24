@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Calculate the percentage contribution of each time series to the total across all series.
Each individual time series value is divided by the sum of all series at that timestamp,
then multiplied by 100 to get a percentage. This is useful for understanding the relative
contribution of each component to the total.

This operator is equivalent to: `:dup,:dup,:sum,:div,100,:mul`

The operation:
1. Duplicates the input expression twice
2. Sums all series together to get the total
3. Divides each individual series by the total
4. Multiplies by 100 to convert to percentage

## Parameters

* **expr**: The time series expression (typically grouped data) to calculate percentages for

## Examples

Basic percentage calculation:

@@@ atlas-stacklang
/api/v1/graph?q=name,sps,:eq,(,nf.cluster,),:by,:pct
@@@

Comparing before and after percentage conversion:

@@@ atlas-example { hilite=:pct }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:pct
Stack to 100%: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,:pct,:stack
@@@

## Related Operations

* [:div](div.md) - Manual percentage calculation with custom divisors
* [:sum](sum.md) - Get totals used in percentage calculation
* [:stack](stack.md) - Display percentages as cumulative areas
* [:by](by.md) - Group data before calculating percentages