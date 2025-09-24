@@@ atlas-signature
name: String
rewritten: TimeSeriesExpr
original: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Create a macro-like operation that shows a simplified name in expression displays while executing
the full expanded implementation. This allows complex operations to be represented with user-friendly
names while maintaining the full implementation for execution.

When expressions are displayed or serialized, the simplified name will be shown instead of the
complex expanded form. However, the actual evaluation uses the full rewritten expression to
ensure correct behavior.

## Parameters

* **original**: The complex expression that performs the actual computation
* **rewritten**: An equivalent but possibly optimized version of the expression
* **name**: The simplified name to display instead of the complex expression

## Examples

Create an `avg` macro that displays simply but executes the full sum/count/divide logic:

@@@ atlas-example { hilite=:named-rewrite }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,:dup,:dup,:sum,:swap,:count,:div
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,:dup,:dup,:sum,:swap,:count,:div,avg,:named-rewrite
@@@

In this example, the complex expression `:dup,:dup,:sum,:swap,:count,:div` will execute to calculate
the average, but when the expression is displayed, it will simply show `avg`.

## Related Operations

* [:avg](avg.md) - A built-in macro that uses named-rewrite internally
* Commonly used by macro implementations to provide clean user interfaces