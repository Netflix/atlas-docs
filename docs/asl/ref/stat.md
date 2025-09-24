@@@ atlas-signature
statistic: String
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute a summary statistic for each time series, producing a constant horizontal line showing
the statistical value calculated across all datapoints in the time window. This reduces each
time series to a single representative value based on the specified statistic.

## Parameters

* **expr**: The time series expression to compute statistics for
* **statistic**: The type of statistic to compute (see supported values below)

## Supported Statistics

* **`avg`**: Average (mean) of all non-NaN values
* **`max`**: Maximum value across all datapoints
* **`min`**: Minimum value across all datapoints
* **`count`**: Number of non-NaN datapoints
* **`total`**: Sum of all non-NaN values
* **`last`**: Most recent non-NaN value in the time window

## Visual Example

The graph below shows `avg`, `max`, `min`, and `last` statistics for a sample time series:

@@@ atlas-graph { show-expr=false }
/api/v1/graph?h=125&no_legend_stats=1&s=e-6m&e=2012-01-01T00:06&tz=UTC&l=1.5&u=4.5&q=minuteOfDay,:time,e-2m,ge-6m,:time-span,2,:mul,:add,e-2m,ge,:time-span,1.5,:mul,:sub,1,e-1m,ge,:time-span,1,:sub,:div,1,:fadd,:fadd,m,:sset,m,:get,input,:legend,m,:get,avg,:stat,avg,:legend,3,:lw,60,:alpha,m,:get,max,:stat,max,:legend,3,:lw,60,:alpha,m,:get,min,:stat,min,:legend,3,:lw,60,:alpha,m,:get,last,:stat,last,:legend,3,:lw,60,:alpha
@@@

## Examples

Computing average statistic for grouped data:

@@@ atlas-example { hilite=:stat }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&palette=hash:armytage&tz=UTC&l=0&q=name,sps,:eq,(,nf.cluster,),:by,avg,:stat
@@@

## Filter Helpers

The most common usage is with [:filter](filter.md) to restrict results based on statistical
criteria. Helper operators `:stat-$(name)` provide a convenient shorthand:

* **[:stat-avg](stat-avg.md)** - Filter by average values
* **[:stat-max](stat-max.md)** - Filter by maximum values
* **[:stat-min](stat-min.md)** - Filter by minimum values
* **[:stat-count](stat-count.md)** - Filter by datapoint count
* **[:stat-total](stat-total.md)** - Filter by sum of values
* **[:stat-last](stat-last.md)** - Filter by most recent values

These helpers automatically substitute the input expression when used with `:filter`, eliminating
the need to repeat complex queries.

## Related Operations

* [:filter](filter.md) - Use stat results for filtering time series
* [:by](by.md) - Group data before computing statistics
