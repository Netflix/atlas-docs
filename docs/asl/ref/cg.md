@@@ atlas-signature
keys: List[String]
expr: Expr
-->
Expr
@@@

Recursively add additional grouping keys to all group-by expressions within a complex expression tree.
This operator traverses the expression and enhances existing `:by` operations by adding the specified
keys to their grouping lists, enabling dynamic modification of aggregation granularity.

## Parameters

* **expr**: The expression tree to modify (can contain multiple nested `:by` operations)
* **keys**: List of additional tag keys to add to all group-by operations found in the expression

## How It Works

The `:cg` operator performs a recursive tree walk through the expression:

1. **Finds all `:by` operations**: Locates every group-by operation in the expression tree
2. **Enhances grouping**: Adds the specified keys to each `:by` operation's key list
3. **Preserves structure**: Maintains the original expression structure while enhancing grouping
4. **Avoids duplicates**: Does not add keys that are already present in a `:by` operation

## Common Use Cases

### Dynamic Dashboard Filtering

Enable dashboard controls to add grouping dimensions without rewriting entire expressions:

```
# Base expression:
name,requests,:eq,:sum,(,nf.app,),:by

# Add cluster grouping dynamically:
name,requests,:eq,:sum,(,nf.app,),:by,(,nf.cluster,),:cg
```

### Tooling Integration

Programmatic tools can enhance existing expressions to include additional grouping:

```
# Original multi-part expression:
name,errors,:eq,:sum,(,nf.app,),:by,
name,requests,:eq,:sum,(,nf.app,),:by,
:div

# Add region grouping to both parts:
name,errors,:eq,:sum,(,nf.app,),:by,
name,requests,:eq,:sum,(,nf.app,),:by,
:div,
(,nf.region,),:cg

# The result is equivalent to:
name,errors,:eq,:sum,(,nf.app,nf.region,),:by,
name,requests,:eq,:sum,(,nf.app,nf.region,),:by,
:div,
```

## Examples

Adding cluster grouping to an existing application-grouped expression:

@@@ atlas-example { hilite=:cg }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.app,),:by
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,sps,:eq,(,nf.app,),:by,(,nf.cluster,),:cg
@@@

## Related Operations

* [:by](by.md) - Group time series by specific tag keys (modified by `:cg`)
* [:cq](cq.md) - Apply common query filters to all queries in expression tree
* [:freeze](freeze.md) - Protect parts of expression tree from modification

