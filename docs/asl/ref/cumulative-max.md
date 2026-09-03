@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Compute the running maximum of a time series across the evaluation time window. Each output
datapoint is the largest value seen on the input line from the start of the graph up to the
time for that datapoint, so the result never decreases.

This is the max analogue of [:integral](integral.md): a running value from the start of the
window, rather than a sliding window like [:rolling-max](rolling-max.md).

## Parameters

* **expr**: The time series expression to compute the running maximum of

## Behavior

* **Non-decreasing**: Each value is the maximum of the input up to that point, so the output
  only ever rises or stays flat
* **Missing data**: NaN values are ignored and leave the running maximum unchanged
* **Window relative**: The running maximum starts over at the beginning of the graph window,
  so changing the time range changes the result
* **No leading NaN**: Unlike the rolling operations, there is no window to fill, so the first
  datapoint is already the maximum of the input up to that point

## Data Processing

| Input | :cumulative-max |
|-------|-----------------|
| 1     | 1               |
| 2     | 2               |
| 0     | 2               |
| NaN   | 2               |
| 5     | 5               |
| 3     | 5               |

## Peak So Far

The common use is showing the worst value seen so far next to the current value. The two lines
meet whenever the input is setting a new peak, and the running maximum holds flat afterwards:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-18h&e=2012-01-01T12:00&tz=UTC&q=name,sps,:eq,:sum,:dup,:cumulative-max,peak+so+far,:legend,:swap,sps,:legend
@@@

The same shape applied to the number of viewers of a live event, where the peak reached during
the event is held after the audience leaves:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,:approx-distinct,:dup,:cumulative-max,peak+so+far,:legend,:swap,active+viewers,:legend
@@@

## Distinct Counts

To get a running count of distinct values, use
[:approx-distinct-cumulative](approx-distinct-cumulative.md) rather than applying
`:cumulative-max` to a distinct count. As shown above, applying it to the output of
[:approx-distinct](approx-distinct.md) gives the highest count seen at any one time, which is
not the same as the total number seen over the window.

## Related Operations

* [:rolling-max](rolling-max.md) - Maximum over a sliding window of datapoints
* [:max](max.md) - Maximum across lines at each interval, not across time
* [:integral](integral.md) - Running sum across the window
* [:approx-distinct-cumulative](approx-distinct-cumulative.md) - Running count of distinct
  values

Since: 1.9
