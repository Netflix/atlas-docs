# Timer

A Timer is used to measure how long (in seconds) some event is taking. Timer measurements
are typically short, less than 1 minute.

Two specialized variants exist:

* [Percentile Timer](#percentile-timer) — adds bucket counters so the backend can estimate
  percentiles.
* [Long Task Timer](../../lang/java/patterns/long-task-timer.md) (Java only) — periodically
  reports time spent in long-running tasks (> 1 minute) as a gauge while they're still
  running.

## Querying

!!! Note
    Timers report summarized statistics about the measurements for a time window
    including the `totalTime`, `count`, `max` and `totalOfSquares`. If you were to simply query for
    the name of your timer via

    @@@ atlas-stacklang
    /api/v1/graph?q=nnf.cluster,foo,:eq,name,http.req.latency,:eq,:and
    @@@

    you would get a nonsense value that is the sum of the reported statistics.

When querying the results of a timer, use one of the operators below to generate a useful
response.

### Average Measurement (:dist-avg)

To compute the average latency across an arbitrary group, use the [:dist-avg] function:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-avg,(,nf.asg,),:by
@@@

[:dist-avg]: ../../../asl/ref/dist-avg.md

### Maximum Measurement (:dist-max)

To compute the maximum latency across a group, use [:dist-max]:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-max,(,nf.asg,),:by
@@@

[:dist-max]: ../../../asl/ref/dist-max.md

### Standard Deviation of Measurement (:dist-stddev)

To compute the standard deviation of measurements across all instances for a time interval:

@@@ atlas-stacklang
/api/v1/graph?q=nnf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-stddev
@@@

[:dist-stddev]: ../../../asl/ref/dist-stddev.md

### Raw Statistics

Note that it is possible to plot the individual statistics by filtering on the `statistic` tag.
If you choose to do so, note that the `count`, `totalAmount` and `totalOfSquares` are counters
thus reported as rates per second, while the `max` is reported as a gauge.

## Percentile Timer

A Percentile Timer is a [Timer](#timer) that also buckets each measurement so the backend can
estimate percentiles. The bucket counters are reported alongside the standard timer stats,
and queries can select either the basic stats or a percentile approximation.

!!! Warning
    Percentile Timers have significant overhead on both the client and storage side. Use
    them sparingly — usually one or two key performance indicators per application — and
    keep tag cardinality tightly bounded. Prefer a basic Timer whenever possible.

In order to maintain the data distribution, Percentile Timers have a higher storage cost,
worst case up to 300x that of a standard Timer. It is highly recommended to set a range to
restrict the worst case overhead. When using the builder, the range defaults to 10 ms to
1 minute, which reduces the worst case multiple from 276x to 58x.

### Range Recommendations

The range should be the SLA boundary or failure point for the activity. Explicitly setting
the range allows the implementation to optimize for the important range of values and reduce
the overhead associated with tracking the data distribution.

For example, suppose you are making a client call and timeout after 10 seconds. Setting the
range to 10 seconds will restrict the possible set of buckets used to those approaching the
boundary. So we can still detect if it is nearing failure, but percentiles that are further
away from the range may be inflated compared to the actual value.

## Languages

### First-Class Support

* [C++](../../lang/cpp/meters/timer.md)
* [Go](../../lang/go/meters/timer.md)
* [Java](../../lang/java/meters/timer.md)
* [Node.js](../../lang/nodejs/meters/timer.md)
* [Python](../../lang/py/meters/timer.md)

### Best-Effort Support

* Rust (internal library)
