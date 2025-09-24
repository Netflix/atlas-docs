@@@ atlas-signature
aggr: AggregationFunction
-->
AggregationFunction
@@@

Force the consolidation function to be average when aggregating data points within time intervals.
This operator overrides the default consolidation behavior to ensure that when multiple data points
fall within a single time step, the average value is used rather than other methods like summing
or taking the maximum.

!!! warning
    **Performance Impact**: This operator can make queries significantly more expensive by preventing
    consolidation pushdown and is rarely needed or desirable.

## Parameters

* **aggr**: The aggregation function to apply average consolidation to

## How Consolidation Works

When the step size for a graph is larger than the reporting interval of the data, multiple
data points may fall within a single graph interval. The consolidation function determines
how these points are combined:

* **Default behavior**: Most aggregation functions use their natural consolidation (e.g., `:sum` uses avg consolidation)
* **Override behavior**: `:cf-avg` forces average consolidation regardless of the aggregation function

## Examples

Force average consolidation for a sum aggregation:

```asl
name,requests,:eq,:max,:cf-avg
```

This ensures that when multiple sum values exist within a time interval, the average of those
sums is displayed rather than summing them up.

## Related Operations

* [:cf-min](cf-min.md) - Force minimum consolidation
* [:cf-max](cf-max.md) - Force maximum consolidation
* [:cf-sum](cf-sum.md) - Force sum consolidation

## See Also

* [Consolidation](../../concepts/consolidation.md) - Detailed explanation of consolidation concepts
