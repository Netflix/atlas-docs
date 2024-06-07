# Java Percentile Timers

**Note**: Percentile timers generate a metric per bucket in the histogram. Create instances
once per ID and reuse them as needed. Avoid adding tags with high cardinality as that increases
the cardinality of the metric. If at all possible, use a [Timer](timer.md) instead.

To get started, create an instance using the [Registry](../registry/overview.md):

```java
public class Server {

  private final Registry registry;
  private final PercentileTimer requestLatency;

  @Inject
  public Server(Registry registry) {
    this.registry = registry;
    requestLatency = PercentileTimer.builder(registry)
        .withId(registry.createId("server.request.latency", "status", "200"))
        .build();
```

Then wrap the call you need to measure, preferably using a lambda:

```java
  public Response handle(Request request) {
    return requestLatency.recordRunnable(() -> handleImpl(request));
  }
```

The lambda variants will handle exceptions for you and ensure the record happens as part of a
finally block using the monotonic time. It could also have been done more explicitly like:

```java
  public Response handle(Request request) {
    final long start = registry.clock().monotonicTime();
    try {
      return handleImpl(request);
    } finally {
      final long end = registry.clock().monotonicTime();
      requestLatency.record(end - start, TimeUnit.NANOSECONDS);
    }
  }
```

This example uses the Clock from the Registry, which can be useful for testing, if you need
to control the timing. In actual usage, it will typically get mapped to the system clock. It
is recommended to use a monotonically increasing source for measuring the times, to avoid
occasionally having bogus measurements due to time adjustments. For more information, see the
[Clock documentation](../../../core/clock.md).

