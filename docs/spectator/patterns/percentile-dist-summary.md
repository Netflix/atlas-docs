# Percentile Distribution Summary

A Percentile Distribution Summary tracks the distribution of events with percentile
estimates. It is the size-domain analog of a [Percentile Timer](percentile-timer.md):
where Percentile Timer is for durations, Percentile Distribution Summary is for arbitrary
sizes — request payload sizes, records returned from a query, batch sizes, etc.

The summary maintains a set of bucket Counters that the backend uses to estimate percentiles
while still allowing slicing by dimensions.

!!! Warning
    Percentile Distribution Summaries have significantly higher storage cost than a standard
    [Distribution Summary](../core/meters/dist-summary.md) — worst case up to 300x. Use them
    sparingly, and keep tag cardinality tightly bounded. Prefer a standard Distribution
    Summary unless percentile estimates are required.

## Bucket Distribution

Uses the same power-of-4 bucket scheme as [Percentile Timer](percentile-timer.md#bucket-distribution).

## Languages

### First-Class Support

* [C++](../lang/cpp/meters/percentile-dist-summary.md)
* [Go](../lang/go/meters/percentile-dist-summary.md)
* [Java](../lang/java/meters/percentile-dist-summary.md)
* [Node.js](../lang/nodejs/meters/percentile-dist-summary.md)
* [Python](../lang/py/meters/percentile-dist-summary.md)
