@@@ atlas-signature
expr: TimeSeriesExpr
-->
TimeSeriesExpr
@@@

Estimate the number of distinct values seen from the start of the graph window up to each point
in time. Where [:approx-distinct](approx-distinct.md) estimates each interval on its own, this
gives a running total of everything seen so far, so the line never decreases.

For a live event, `:approx-distinct` answers "how many people are watching right now" and
`:approx-distinct-cumulative` answers "how many people have watched at all". The two differ by
however much the audience turns over: if viewers join and leave, more people watch over the
event than are ever watching at once.

## Parameters

* **expr**: A query for a metric published as a distinct count sketch. See
  [:approx-distinct](approx-distinct.md) for how to publish it

## Behavior

* **Non-decreasing**: Each value covers everything from the start of the window, so the line
  only rises or stays flat
* **Depends on the time range**: The count starts over at the start of the graph window.
  Widening the range raises the values, because more history is included, so the number is
  only meaningful alongside the window it was taken over
* **The count is approximate**: The same accuracy applies as for
  [:approx-distinct](approx-distinct.md), a relative standard error of roughly 13%. The running
  total is smoother than the per interval estimate but no more accurate
* **Grouping**: Add `(,key,),:by` before the operation to get a running count per group. As
  with [:approx-distinct](approx-distinct.md), the groups only add up when a distinct value can
  appear in just one group

## How It Works

The operation is a rewrite of:

```
:dup,:cumulative-max,:approx-distinct
```

Sketches merge by taking the max of each register, so applying
[:cumulative-max](cumulative-max.md) to the registers unions the sketches across time before
the estimate is computed. The running max has to be applied to the registers, not to the
estimates, which is why this is a distinct operation rather than something to assemble by hand.

## Examples

The total audience next to the audience at any one time, for the live event in the sample data.
The gap between the lines is the turnover: 2.18M viewers over the event against a peak of 1.90M
watching at once:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,:dup,:approx-distinct,active+now,:legend,:swap,:approx-distinct-cumulative,seen+so+far,:legend
@@@

Running count broken out by device:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,(,device,),:by,:approx-distinct-cumulative
@@@

## Order Matters

Applying [:cumulative-max](cumulative-max.md) to the output of
[:approx-distinct](approx-distinct.md) looks similar but answers a different question. It gives
the highest number ever seen at one time, which is smaller than the total seen over the window:

@@@ atlas-graph { show-expr=true }
/api/v1/graph?w=750&h=200&l=0&s=e-6h&e=2012-01-01T00:00&tz=UTC&q=name,viewers.concurrent,:eq,:sum,:dup,:approx-distinct-cumulative,total+seen,:legend,:swap,:approx-distinct,:cumulative-max,peak+at+one+time,:legend
@@@

Use `:approx-distinct-cumulative` for the running total. To track the peak, applying
`:cumulative-max` after `:approx-distinct` is the correct form and is worth plotting alongside
the total.

## Related Operations

* [:approx-distinct](approx-distinct.md) - Distinct values per interval
* [:cumulative-max](cumulative-max.md) - Running maximum of a line
* [:integral](integral.md) - Running sum, the equivalent for values that add up
* [:by](by.md) - Break the running count out by a key

Since: 1.9
