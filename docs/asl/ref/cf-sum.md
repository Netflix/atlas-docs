@@@ atlas-signature
aggr: AggregationFunction
-->
AggregationFunction
@@@

Force the consolidation function to be sum when aggregating data points within time intervals.
This operator overrides the default consolidation behavior to ensure that when multiple data points
fall within a single time step, the values are summed together rather than using other methods
like averaging or taking the maximum.

!!! warning
    **Performance Impact**: This operator can make queries significantly more expensive by preventing
    consolidation pushdown and is rarely needed or desirable.

## Parameters

* **aggr**: The aggregation function to apply sum consolidation to

## How Consolidation Works

When the step size for a graph is larger than the reporting interval of the data, multiple
data points may fall within a single graph interval. The consolidation function determines
how these points are combined:

* **Default behavior**: Most aggregation functions use their natural consolidation (e.g., `:sum` already uses avg consolidation)
* **Override behavior**: `:cf-sum` forces sum consolidation even for functions that normally use other methods

## Examples

Force sum consolidation for an average aggregation:

```
name,requests,:eq,:sum,:cf-sum
```

This ensures that when multiple average values exist within a time interval, they are summed
together rather than averaged again.

## Related Operations

* [:cf-min](cf-min.md) - Force minimum consolidation
* [:cf-max](cf-max.md) - Force maximum consolidation
* [:cf-avg](cf-avg.md) - Force average consolidation

## See Also

* [Consolidation](../../concepts/consolidation.md) - Detailed explanation of consolidation concepts
