@@@ atlas-signature
-->
Query
@@@

Universal query that matches all time series unconditionally. This operator returns a query
expression that evaluates to true for any input, effectively selecting all available time series
data. It's useful as a starting point for complex filtering or when you need to include all data.

## Parameters

* None - this operator takes no parameters

## Examples

Select all time series (typically used as a base for further filtering):

```
:true
```

Combine with logical operations to create complex queries:

```
:true,name,cpu,:eq,:and    # Equivalent to just name,cpu,:eq
```

## Related Operations

* [:false](false.md) - Universal query that matches no time series
* [:and](and.md) - Logical AND (`:true` with any query returns that query)
* [:or](or.md) - Logical OR (`:true` with any query returns `:true`)
* [:not](not.md) - Logical NOT (`:true,:not` is equivalent to `:false`)