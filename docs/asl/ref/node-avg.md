@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

A helper to compute an average using the `poller.asg.instance` metric as the denominator.
The common infrastructure tags will be used to restrict the scope for the denominator. This
operator should be used instead of [:avg](avg.md) if the goal is to compute an average per
node.

@@@ atlas-stacklang { hilite=:node-avg }
/api/v1/graph?q=name,sps,:eq,nf.app,nccp,:eq,:and,:node-avg
@@@
