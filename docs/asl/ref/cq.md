@@@ atlas-signature
Expression
Query
-->
Expression
@@@

Recursively AND a common query to all queries in an expression. If the first parameter
is not an expression, then it will be not be modified.

Example:

@@@ atlas-stacklang
/api/v1/graph?q=name,ssCpuUser,:eq,name,DiscoveryStatus_UP,:eq,:mul,nf.app,alerttest,:eq,:cq
@@@

@@@ atlas-example { hilite=:cq }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,name,DiscoveryStatus_UP,:eq,:mul,nf.app,alerttest,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,ssCpuUser,:eq,name,DiscoveryStatus_UP,:eq,:mul,nf.app,alerttest,:eq,:cq
@@@

@@@ atlas-example { hilite=:cq }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42,nf.app,alerttest,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=42,nf.app,alerttest,:eq,:cq
@@@
