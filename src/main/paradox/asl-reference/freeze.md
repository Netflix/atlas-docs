
# freeze

## Signature

`* -- <empty>`

## Summary

Freeze removes all data from the stack and pushes it to a separate frozen stack
that cannot be modified other than to push additional items using the freeze operation.
The final stack at the end of the execution will include the frozen contents along with
any thing that is on the normal stack.

This operation is useful for isolating common parts of the stack while still allowing
tooling to manipulate the main stack using concatenative rewrite operations. The most
common example of this is the @ref:[:cq](cq.md) operation used to apply a common query
to graph expressions. For a concrete example, suppose you want to have an overlay
expression showing network errors on a switch that you want to add in to graphs on
a dashboard. The dashboard allows drilling into the graphs by selecting a particular
cluster. To make this work the dashboard appends a query rewrite to the expression
like:

@@@ atlas-expr
,:list,(,nf.cluster,{{selected_cluster}},:eq,:cq,),:each
@@@

This @ref:[:list](list.md) operator will apply to everything on the stack. However, this
is problematic because the cluster restriction will break the overlay query. Using
the freeze operator the overlay expression can be isolated from the main stack. So
the final expression would look something like:

@@@ atlas-expr
-- Query that should be used as is and not modified further,
name,networkErrors,:eq,:sum,50,:gt,:vspan,40,:alpha,
:freeze,

-- Normal contents of the stack,
name,ssCpuUser,:eq,:avg,1,:axis,
name,loadavg1,:eq,:avg,2,:axis,

-- Rewrite appended by tooling only applies to main stack,
:list,(,nf.cluster,{{selected_cluster}},:eq,:cq,),:each
@@@

Since: 1.6
