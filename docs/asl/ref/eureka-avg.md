@@@ atlas-signature
Query
-->
TimeSeriesExpr
@@@

A helper to compute an average using the number of instances in the `UP` state based on the
`discovery.status` metric as the denominator. The common infrastructure tags will be used to
restrict the scope for the denominator. This operator should be used if the numerator is based
on incoming traffic that is routed via the Eureka service and goal is to compute an average
per node receiving traffic.

@@@ atlas-stacklang { hilite=:eureka-avg }
/api/v1/graph?q=name,sps,:eq,nf.app,nccp,:eq,:and,:eureka-avg
@@@
