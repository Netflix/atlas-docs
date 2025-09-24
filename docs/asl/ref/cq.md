@@@ atlas-signature
commonQuery: Query
expr: Expr
-->
Expr
@@@

Apply a common query filter to all query expressions within a complex expression tree. This operator
traverses the expression and adds the common query as an AND condition to every query it finds.
Non-query expressions (like constants or math operations) are left unchanged.

This is particularly useful for applying global filters (like application or region restrictions)
to complex expressions that contain multiple queries.

## Parameters

* **expr**: The expression tree that may contain multiple queries
* **commonQuery**: The query condition to AND with every query found in the expression

## Examples

Apply a common application filter to an expression with multiple queries:

@@@ atlas-stacklang
/api/v1/graph?q=name,ssCpuUser,:eq,name,DiscoveryStatus_UP,:eq,:mul,nf.app,alerttest,:eq,:cq
@@@

This transforms:
- `name,ssCpuUser,:eq` becomes `name,ssCpuUser,:eq,nf.app,alerttest,:eq,:and`
- `name,DiscoveryStatus_UP,:eq` becomes `name,DiscoveryStatus_UP,:eq,nf.app,alerttest,:eq,:and`

@@@ atlas-example { hilite=:cq }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,name,DiscoveryStatus_UP,:eq,:mul,nf.app,alerttest,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,name,DiscoveryStatus_UP,:eq,:mul,nf.app,alerttest,:eq,:cq
@@@

Non-query expressions are unaffected (42 remains unchanged):

@@@ atlas-example { hilite=:cq }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42,nf.app,alerttest,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42,nf.app,alerttest,:eq,:cq
@@@

## Related Operations

* [:and](and.md) - Manually combine two query conditions
* [:freeze](freeze.md) - Isolate expressions from common query operations