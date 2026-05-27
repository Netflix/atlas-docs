# Monotonic Counter

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept.

Java does not expose a dedicated monotonic counter meter; the equivalent is the
[Polled Meter](../patterns/polled-meter.md) helper's `monitorMonotonicCounter`, which
periodically samples a function returning the current absolute value and reports the
per-second rate of the delta. A minimum of two polls is required before the first metric
is reported.

Two common forms:

```java
// Lambda over a source that exposes a long-valued cumulative count.
PolledMeter.using(registry)
    .withName("pool.completedTasks")
    .monitorMonotonicCounter(executor, ThreadPoolExecutor::getCompletedTaskCount);

// A Number instance that the caller updates directly.
LongAdder tasks = new LongAdder();
PolledMeter.using(registry)
    .withName("pool.completedTasks")
    .monitorMonotonicCounter(tasks);
```

For double-valued sources, use `monitorMonotonicCounterDouble`.

If the polled value decreases between samples (counter reset, source restart, or numeric
wraparound), that interval's delta is dropped and the new value becomes the baseline for
the next delta. See [Counter resets and wraparounds](../../../patterns/monotonic-counter.md#counter-resets-and-wraparounds).

Java is long-based, so there is no separate uint64 variant — `monitorMonotonicCounter` covers
both signed and OS-counter use cases.
