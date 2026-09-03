@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Estimate the number of distinct values seen in each interval, for example the number of
distinct users active on a service. Counting distinct values exactly means remembering every
value seen, which does not fit in a time series, so the count is approximate.

Each output datapoint is the estimate for that interval on its own. For a running count of the
distinct values seen so far, use
[:approx-distinct-cumulative](approx-distinct-cumulative.md).

## Parameters

* **expr**: A query for a metric published as a distinct count sketch

## Publishing the Data

This operation only works on data published for it, with a
[Distinct Count Sketch](../../spectator/lang/java/patterns/distinct-count-sketch.md). Query the
metric by name as usual. Applying `:approx-distinct` to an ordinary metric matches nothing.

## Behavior

* **The count is approximate**: The relative standard error is roughly 13%, so expect the value
  to move around a little from one interval to the next even when the true count is steady. Use
  it to see the magnitude and the shape of a trend, not to read off an exact number
* **Merges across sources**: A single estimate is computed over everything the query matches. A
  user active on several instances counts once, so the result is not the sum of the per instance
  counts
* **Per interval**: Each interval is estimated on its own, so the line goes down as well as up
* **Aggregation is optional**: `:sum` is not required, it makes no difference to the estimate.
  `:avg`, `:count`, and `:all` are rejected
* **Grouping**: Add `(,key,),:by` before the operation to estimate separately for each value of
  a key

## Examples

The sample data has a metric for a live event that runs once a day, with the audience joining
over the first half hour, turning over while the event runs, and leaving at the end:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,:approx-distinct,active+viewers,:legend
@@@

Break the estimate out by device:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,(,device,),:by,:approx-distinct
@@@

## Groups May Not Add Up

The grouped estimates only total the ungrouped estimate when each distinct value can appear in
just one group. In the example above a viewer watches on one device, so the devices roughly add
up to the overall count. Group by something a viewer can be in more than once, such as the
titles watched, and the groups will total more than the ungrouped estimate: the viewer counts
once overall but once in each group they appear in.

This is a property of counting distinct things, not of the approximation. Summing the groups
answers a different question from estimating over everything at once, so aggregating the result
of `:approx-distinct` with `:sum` is nearly always a mistake. Put the grouping before the
operation and let it do the merging.

## Related Operations

* [:approx-distinct-cumulative](approx-distinct-cumulative.md) - Distinct values seen so far,
  rather than per interval
* [:by](by.md) - Break the estimate out by a key
* [:count](count.md) - Number of lines matched, which is not the number of distinct values

Since: 1.9
