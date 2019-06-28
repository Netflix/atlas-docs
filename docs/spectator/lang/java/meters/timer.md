# Java Timers

## Timer

To get started, create an instance using the [Registry](../registry/overview.md):

```java
public class Server {

  private final Registry registry;
  private final Timer requestLatency;

  @Inject
  public Server(Registry registry) {
    this.registry = registry;
    requestLatency = registry.timer("server.requestLatency");
  }
```

Then wrap the call you need to measure, preferably using a lambda:

```java
  public Response handle(Request request) {
    return requestLatency.record(() -> handleImpl(request));
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

## LongTaskTimer

To get started, create an instance using the [Registry](../registry/overview.md):

```java
import com.netflix.spectator.api.patterns.LongTaskTimer;

public class MetadataService {

  private final LongTaskTimer metadataRefresh;

  @Inject
  public MetadataService(Registry registry) {
    metadataRefresh = LongTaskTimer.get(
        registry, registry.createId("metadata.refreshDuration"));
    // setup background thread to call refresh()
  }

  private void refresh() {
    final int id = metadataRefresh.start();
    try {
      refreshImpl();
    } finally {
      metadataRefresh.stop(id);
    }
  }
```

The id value returned by the `start` method is used to keep track of a particular task being
measured by the Timer. It must be stopped using the provided id. Note that unlike a regular Timer
that does not do anything until the final duration is recorded, a long duration Timer will report
as two Gauges:

* `duration`: total duration spent within all currently running tasks.
* `activeTasks`: number of currently running tasks.

This means that you can see what is happening while the task is running, but you need to keep in
mind:

* The meter id is fixed before the task begins. There is no way to change tags based on the run,
e.g., update a different Timer, if an exception is thrown.
* Being a Gauge, it is inappropriate for short tasks. In particular, Gauges are sampled and if it
is not sampled during the execution, or the sampling period is a significant subset of the expected
duration, then the duration value will not be meaningful.

Like a regular Timer, the duration Timer also supports using a lambda to simplify the common case:

```java
  private void refresh() {
    metadataRefresh.record(this::refreshImpl);
  }
```
