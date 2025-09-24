@@@ atlas-signature
query: Query
-->
TimeSeriesExpr
@@@

Compute an average per node by using the `poller.asg.instance` metric as the denominator.
This specialized aggregation function accounts for the actual number of active instances
rather than just averaging using the number of time series. It automatically restricts the
scope using common infrastructure tags to ensure proper normalization.

## Parameters

* **query**: The query to compute the per-node average for

## Purpose

This operator should be used instead of [:avg](avg.md) when you need a true per-node average
that accounts for the actual instance count. Regular `:avg` computes the mean across all
matching time series, but `:node-avg` divides by the actual number of reporting instances.

The key difference: if you have 3 instances but each reports metrics with multiple dimensions
(creating more time series), `:avg` would divide by the total number of time series while
`:node-avg` divides by 3 (the actual instance count).

## How It Works

1. Executes the provided query to get the numerator values
2. Finds the corresponding `poller.asg.instance` metrics using infrastructure tags
3. Divides the query results by the instance count to get per-node averages
4. Uses common tags (like `nf.app`, `nf.cluster`) to properly scope the calculation

## Examples

Computing average requests per second per node:

@@@ atlas-stacklang { hilite=:node-avg }
/api/v1/graph?q=name,sps,:eq,nf.app,nccp,:eq,:and,:node-avg
@@@

## Related Operations

* [:avg](avg.md) - Standard average aggregation (doesn't normalize by node count)
* [:eureka-avg](eureka-avg.md) - Average using nodes UP in Eureka for the denominator
* [:dist-avg](dist-avg.md) - Average over the number of recorded samples
