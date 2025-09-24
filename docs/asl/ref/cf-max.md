@@@ atlas-signature
aggr: AggregationFunction
-->
AggregationFunction
@@@

Force the consolidation function to be maximum when aggregating data points within time intervals.
This operator overrides the default consolidation behavior to ensure that when multiple data points
fall within a single time step, the maximum value is selected rather than using other methods
like averaging or summing.

!!! warning
    **Performance Impact**: This operator can make queries significantly more expensive by preventing
    consolidation pushdown and is rarely needed or desirable.

## Parameters

* **aggr**: The aggregation function to apply maximum consolidation to

## How Consolidation Works

When the step size for a graph is larger than the reporting interval of the data, multiple
data points may fall within a single graph interval. The consolidation function determines
how these points are combined:

* **Default behavior**: Most aggregation functions use their natural consolidation (e.g., `:sum` uses avg consolidation)
* **Override behavior**: `:cf-max` forces maximum consolidation regardless of the aggregation function

## Examples

Force maximum consolidation for a sum aggregation:

```asl
name,requests,:eq,:sum,:cf-max
```

This ensures that when multiple sum values exist within a time interval, the maximum of those
sums is displayed rather than averaging them.

## Related Operations

* [:cf-min](cf-min.md) - Force minimum consolidation
* [:cf-avg](cf-avg.md) - Force average consolidation
* [:cf-sum](cf-sum.md) - Force sum consolidation

## See Also

* [Consolidation](../../concepts/consolidation.md) - Detailed explanation of consolidation concepts
