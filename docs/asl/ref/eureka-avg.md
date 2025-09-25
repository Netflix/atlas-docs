@@@ atlas-signature
query: Query
-->
TimeSeriesExpr
@@@

Compute an average based on the number of instances in the `UP` state according to Eureka service
discovery. This operator uses the `discovery.status` metric to determine the active instance count
as the denominator, making it ideal for metrics related to incoming traffic that is load-balanced
through Eureka.

## Parameters

* **query**: Query for metrics to average, typically traffic-related metrics routed via Eureka

## How It Works

1. **Numerator**: Uses the total from the provided query (typically aggregated metrics)
2. **Denominator**: Counts instances with `state=UP` for the same service
3. **Scoping**: Common infrastructure tags automatically restrict the denominator scope
4. **Result**: Average per active (traffic-receiving) instance

## When to Use

This operator is specifically designed for scenarios where:

- Metrics represent incoming traffic routed through Eureka service discovery
- You want average per active instance, not per total deployed instance
- The goal is to measure per-node load for traffic-bearing services

## Examples

Computing average requests per second per active instance:

@@@ atlas-stacklang { hilite=:eureka-avg }
/api/v1/graph?q=name,sps,:eq,nf.app,nccp,:eq,:and,:eureka-avg
@@@

## Comparison with Other Averages

| Operator | Denominator | Use Case |
|----------|-------------|----------|
| `:avg` | Number of reporting time series | General averaging |
| `:node-avg` | Number of unique instances | Per-instance average (all instances) |
| `:eureka-avg` | Number of UP instances in Eureka | Per-active-instance average (Eureka-routed traffic) |
| `:dist-avg` | Recorded sample count | Per-measurement average |

## Infrastructure Tag Scoping

The operator automatically uses common tags to ensure the denominator matches the numerator scope:

- `nf.app` - Application name
- `nf.cluster` - Cluster identifier
- `nf.region` - AWS region
- Other standard Netflix infrastructure tags

## Related Operations

* [:avg](avg.md) - Standard average across time series
* [:node-avg](node-avg.md) - Average using total instance count (includes non-traffic instances)
* [:dist-avg](dist-avg.md) - Average using measurement sample counts
* [:sum](sum.md) - Total aggregation (numerator for manual average calculation)
