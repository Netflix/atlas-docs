# Timer

A Timer is used to measure how long (in seconds) some event is taking. Timer measurements
are typically short, less than 1 minute. 

A selection of specialized timers include: 

* `LongTaskTimer` - Periodically reports the time taken for a long running task (> 1 minute). See
  the [Long Task Timer] pattern for details.
* `PercentileTimer` - Useful if percentile approximations are needed in addition to basic stats.
  See the [Percentile Timer] pattern for details.

[Long Task Timer]: ../../patterns/long-task-timer.md
[Percentile Timer]: ../../patterns/percentile-timer.md

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

Note that it is possible to plot the individual statics by filtering on the `statistic` tag.
If you choose to do so, note that the `count`, `totalAmount` and `totalOfSquares` are counters
thus reported as rates per second, while the `max` is reported as a gauge.

## Languages

### First-Class Support

* [C++](../../lang/cpp/meters/timer.md)
* [Go](../../lang/go/meters/timer.md)
* [Java](../../lang/java/meters/timer.md)
* [Node.js](../../lang/nodejs/meters/timer.md)
* [Python](../../lang/py/meters/timer.md)

### Best-Effort Support

* Rust (internal library)
