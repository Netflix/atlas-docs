# Monotonic Counter

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept.

Java does not expose a dedicated monotonic counter meter; the equivalent is the
[Polled Meter](../patterns/polled-meter.md) helper's `monitorMonotonicCounter`, which
periodically samples a function returning the current absolute value and reports the
per-second rate of the delta:

```java
public class Worker {

  @Inject
  public Worker(Registry registry, ThreadPoolExecutor executor) {
    PolledMeter.using(registry)
        .withName("threadpool.completedTasks")
        .monitorMonotonicCounter(executor, ThreadPoolExecutor::getCompletedTaskCount);
  }
}
```

For double-valued sources, use `monitorMonotonicCounterDouble`. A minimum of two polls is
required before the first metric is reported.

Java is long-based, so there is no separate uint64 variant — `monitorMonotonicCounter` covers
both signed and OS-counter use cases.
