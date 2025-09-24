@@@ atlas-signature
text: String
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Set custom legend text for time series. Legends support variable substitution using tag
values from the query and grouping operations, allowing for dynamic legend generation based
on the actual data being displayed.

## Parameters

* **expr**: The time series expression to apply the legend to
* **text**: The legend text template with optional variable substitutions

## Variable Substitution

Variables are referenced using the `$` prefix and can optionally be enclosed in parentheses:

* **Basic syntax**: `$tagname` - substitutes the value of the specified tag
* **Parentheses syntax**: `$(tagname)` - required when the variable name might be ambiguous
* **Undefined variables**: If a variable doesn't exist, the variable name itself is displayed

### Available Variables

* **Query tag keys**: Any tag key used in `:eq` clauses (e.g., `$name`, `$nf.app`)
* **Group by keys**: Any tag key used in [`:by`](by.md) grouping operations
* **System variables**: `$atlas.offset` for time shift information

## Examples

Using a tag value directly in the legend:

@@@ atlas-example { hilite=:legend }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,$name,:legend
@@@

Combining static text with variable substitution:

@@@ atlas-example { hilite=:legend }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,cluster+$nf.cluster,:legend
@@@

## Related Operations

* [:eq](eq.md) - Create exact tag matches that provide variables for legend substitution
* [:by](by.md) - Group data to create variables for legend substitution

## See Also

* [Legend API Documentation](../../api/graph/legends.md) - Complete guide to legend formatting and configuration