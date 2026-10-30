@@@ atlas-signature
w: Window
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Estimate the number of distinct values seen within a trailing window, for example the number of
distinct users active over the last hour. Where [:approx-distinct](approx-distinct.md) estimates
each interval on its own, this counts a value once if it was seen anywhere in the window.

For a live event, `:approx-distinct` answers "how many people are watching right now",
`:approx-distinct-rolling` answers "how many people have watched in the last 30 minutes", and
[:approx-distinct-cumulative](approx-distinct-cumulative.md) answers "how many people have
watched at all".

## Parameters

* **expr**: A query for a metric published as a distinct count sketch. See
  [:approx-distinct](approx-distinct.md) for how to publish it
* **w**: Window size, either a duration, such as `30m`, or a number of datapoints including the
  current value, such as `5`. See [Window Size](#window-size)

## Window Size

Use a duration, `30m`, to cover a fixed amount of time independent of the step size. The
duration is rounded down to the nearest step boundary. A number of datapoints can also be used,
but then the amount of time covered by the estimate will change when zooming out to a time
frame that causes consolidation.

If the step size is at least as large as the window, then a single interval already covers the
window and the result is the same as [:approx-distinct](approx-distinct.md).

## Behavior

* **At least the per interval count**: A value seen in any interval of the window is counted, so
  the result is at least `:approx-distinct` for the same interval, and is larger when the
  values turn over within the window. For small counts, a few hundred or fewer, the estimator
  can occasionally put the window slightly below the interval
* **Not a rolling max of the estimate**: Applying [:rolling-max](rolling-max.md) to the output
  of `:approx-distinct` gives the highest number seen at one time in the window, which is
  smaller. Use `:approx-distinct-rolling` for the number seen across the window
* **The count is approximate**: The same accuracy applies as for
  [:approx-distinct](approx-distinct.md), a relative standard error of roughly 13%
* **Grouping**: Add `(,key,),:by` before the operation to get a count per group. As with
  [:approx-distinct](approx-distinct.md), the groups only add up when a distinct value can
  appear in just one group

## Examples

The audience over the last 30 minutes next to the audience at any one time, for the live event
in the sample data. The gap between the lines is the turnover within the window:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,:dup,:approx-distinct,active+now,:legend,:swap,30m,:approx-distinct-rolling,last+30m,:legend
@@@

Rolling count broken out by device:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,(,device,),:by,30m,:approx-distinct-rolling
@@@

## Related Operations

* [:approx-distinct](approx-distinct.md) - Distinct values per interval
* [:approx-distinct-cumulative](approx-distinct-cumulative.md) - Distinct values seen so far
* [:rolling-max](rolling-max.md) - Rolling maximum of a line
* [:by](by.md) - Break the rolling count out by a key

Since: 1.9
