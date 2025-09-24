@@@ atlas-signature
item: Any
-->
item: Any
item: Any
@@@

Duplicates the item on the top of the stack, pushing a copy of it onto the stack. This is commonly
used when you need to apply multiple operations to the same value or expression.

## Parameters

* **item**: Any value or expression that will be duplicated

## Examples

Basic duplication of a time expression:

@@@ atlas-example { hilite=:dup }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfDay,:time
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfDay,:time,:dup
@@@

Common pattern for applying multiple aggregations to the same query:

@@@ atlas-example { hilite=:dup }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:sum
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,:dup,:sum,:swap,:count,:div
@@@

## Related Operations

* [:over](over.md) - Copy the second item to the top
* [:swap](swap.md) - Exchange the top two stack items
* [:tuck](tuck.md) - Copy the top item to the third position
