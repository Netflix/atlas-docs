# Monotonic Counter

A Monotonic Counter is a use of a [Counter](../core/meters/counter.md) where the source
data is a **cumulative** value that only increases (e.g. bytes-sent on a network interface,
total tasks completed by a thread pool). The library samples successive absolute values and
computes the delta itself, reporting the per-second rate to the backend.

Use this when the underlying source is naturally monotonic and you don't have a hook to
increment a regular counter on each event. Common sources: OS counters, JMX counters, thread
pool stats, network interface counters.

A minimum of **two samples** is required before the first metric is reported, so there is a
slower time-to-first-data point than a standard counter.

## Numeric variants

* **Signed / double** — the default. Suitable when the source fits in a signed 64-bit
  integer or double and is not expected to overflow.
* **uint64** — required when reading from a source that uses unsigned 64-bit semantics
  (most OS-level interface counters) so that a wrap-around past `2^63` is not interpreted
  as a backward jump.

The spectatord-backed clients (C++, Go, Node.js, Python) expose both variants. In Java,
use [Polled Meter](polled-meter.md)'s `monitorMonotonicCounter` — Java is long-based and
does not need a separate uint variant.

## Implementations

For the spectatord-backed clients, Monotonic Counter is a first-class meter type — call
`set(absoluteValue)` on each sample.

For Java, the equivalent is exposed via the [Polled Meter](polled-meter.md) helper, which
periodically samples a function returning the current absolute value and reports the delta:

```java
PolledMeter.using(registry)
    .withName("threadpool.completedTasks")
    .monitorMonotonicCounter(executor, ThreadPoolExecutor::getCompletedTaskCount);
```

## Languages

* C++: [signed](../lang/cpp/meters/monotonic-counter.md), [uint64](../lang/cpp/meters/monotonic-counter-uint.md)
* Go: [signed](../lang/go/meters/monotonic-counter.md), [uint64](../lang/go/meters/monotonic-counter-uint.md)
* [Java](../lang/java/meters/monotonic-counter.md) (no dedicated meter; uses [Polled Meter](polled-meter.md))
* Node.js: [signed](../lang/nodejs/meters/monotonic-counter.md), [uint64](../lang/nodejs/meters/monotonic-counter-uint.md)
* Python: [signed](../lang/py/meters/monotonic-counter.md), [uint64](../lang/py/meters/monotonic-counter-uint.md)
