@@@ atlas-signature
-->
Query
@@@

Universal query that matches no time series unconditionally. This operator returns a query
expression that evaluates to false for any input, effectively excluding all time series data.
It's useful for creating empty result sets or as a component in logical expressions.

## Parameters

* None - this operator takes no parameters

## Examples

Create an empty query (matches nothing):

```
:false
```

Use in logical operations:

```
:false,name,cpu,:eq,:or    # Equivalent to just name,cpu,:eq
name,cpu,:eq,:false,:and   # Always produces empty results
```

## Related Operations

* [:true](true.md) - Universal query that matches all time series
* [:and](and.md) - Logical AND (`:false` with any query returns `:false`)
* [:or](or.md) - Logical OR (`:false` with any query returns that query)
* [:not](not.md) - Logical NOT (`:false,:not` is equivalent to `:true`)