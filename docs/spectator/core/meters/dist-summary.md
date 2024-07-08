# Distribution Summary

A Distribution Summary is used to track the distribution of events. It is similar to a [Timer], but
more general, in that the size does not have to be a period of time. For example, a distribution
summary could be used to measure the payload sizes of requests hitting a server or the number of
records returned from a query.

It is recommended to always use base units when recording the data. So, if measuring the payload
size use bytes, not kilobytes or some other unit. This allows the presentation layer for graphing
to use either SI or IEC prefixes in a natural manner, and you do not need to consider the meaning
of something like "milli-milliseconds".

## Querying

!!! Note
    Distribution summaries report summarized statistics about the measurements for a time window
    including the `totalAmount`, `count`, `max` and `totalOfSquares`. If you were to simply query for
    the name of your timer via

    @@@ atlas-stacklang
    /api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.payload.size,:eq,:and
    @@@

    you would get a nonsense value that is the sum of the reported statistics.

When querying the results of a distribution summary, either select *one* of the statistics above
via a filter, or use one of the operators below to generate a useful response.

### Average Measurement (:dist-avg)

To compute the average latency across an arbitrary group, use the [:dist-avg] function:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.payload.size,:eq,:and,:dist-avg,(,nf.asg,),:by
@@@

[:dist-avg]: ../../../asl/ref/dist-avg.md

### Maximum Measurement (:dist-max)

To compute the maximum latency across a group, use [:dist-max]:

@@@ atlas-stacklang
/api/v1/graph?q=nf.cluster,foo,:eq,name,http.req.payload.size,:eq,:and,:dist-max,(,nf.asg,),:by
@@@

[:dist-max]: ../../../asl/ref/dist-max.md

### Standard Deviation of Measurement (:dist-stddev)

To compute the standard deviation of measurements across all instances for a time interval:

@@@ atlas-stacklang
/api/v1/graph?q=nnf.cluster,foo,:eq,name,http.req.payload.size,:eq,:and,:dist-stddev
@@@

[:dist-stddev]: ../../../asl/ref/dist-stddev.md

### Raw Statistics

Note that it is possible to plot the individual statics by filtering on the `statistic` tag.
If you choose to do so, note that the `count`, `totalAmount` and `totalOfSquares` are counters
thus reported as rates per second, while the `max` is reported as a gauge.

## Languages

### First-Class Support

* [C++](../../lang/cpp/usage.md)
* [Go](../../lang/go/meters/dist-summary.md)
* [Java](../../lang/java/meters/dist-summary.md)
* [Node.js](../../lang/nodejs/meters/dist-summary.md)
* [Python](../../lang/py/meters/dist-summary.md)

### Best-Effort Support

* Rust (internal library)
