# Distribution Summary

A Distribution Summary is used to track the distribution of events. It is similar to a [Timer], but
more general, in that the size does not have to be a period of time. For example, a distribution
summary could be used to measure the payload sizes of requests hitting a server.

It is recommended to always use base units when recording the data. So, if measuring the payload
size use bytes, not kilobytes or some other unit. This allows the presentation layer for graphing
to use either SI or IEC prefixes in a natural manner, and you do not need to consider the meaning
of something like "milli-milliseconds".

[Timer]: timer.md

## Average Measurement (:dist-avg)

For [Timer] and Distribution Summary metrics, the `totalTime`/`totalAmount` and `count` are
collected each time a measurement is taken. If this technique was applied to a request latency
metric, then you would have the average latency per request for an arbitrary grouping. These
types of metrics have an explicit count based on activity. To get an average per measurement 
manually:

```
statistic,totalTime,:eq,:sum,
statistic,count,:eq,:sum,
:div
```

This expression can be bound to a query using the [:cq] (common query) operator:

```
statistic,totalTime,:eq,:sum,
statistic,count,:eq,:sum,
:div
nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:cq
```

To make this process easier, Atlas provides a [:dist-avg] function that is used in the same
manner as a built-in aggregate function:

```
nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-avg

nf.cluster,foo,:eq,name,http.req.latency,:eq,:and,:dist-avg,(,nf.asg,),:by
```

[:cq]: ../../../asl/ref/cq.md
[:dist-avg]: ../../../asl/ref/dist-avg.md

## Maximum Measurement (:dist-max)

TBD

## Standard Deviation of Measurement (:dist-stddev)

TBD

## Languages

### First-Class Support

* [Java](../../lang/java/meters/dist-summary.md)
* [Node.js](../../lang/nodejs/meters/dist-summary.md)

### Experimental Support

* [C++](../../lang/cpp/meters/dist-summary.md)
* [Go](../../lang/go/meters/dist-summary.md)
* [Python](../../lang/py/meters/dist-summary.md)
* [Ruby](../../lang/rb/meters/dist-summary.md)
