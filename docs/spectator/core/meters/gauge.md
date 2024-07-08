# Gauge

A Gauge is a value that is sampled at some point in time. Typical examples for Gauges would be the
size of a queue, or the number of threads in a running state. Since Gauges are not updated inline
when a state change occurs, there is no information about what might have occurred between samples.

Consider monitoring the behavior of a queue of tasks. If the data is being collected once a minute,
then a Gauge for the size will show the size when it was sampled (a.k.a. last-write-wins). The size
may have been much higher or lower at some point during interval, but that is not known.

## Languages

### First-Class Support

* [C++](../../lang/cpp/usage.md)
* [Go](../../lang/go/usage.md)
* [Java](../../lang/java/meters/gauge.md)
* [Node.js](../../lang/nodejs/meters/gauge.md)
* [Python](../../lang/py/meters/gauge.md)

### Best-Effort Support

* Rust (internal library)
