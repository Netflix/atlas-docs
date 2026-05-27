# Max Gauge

See [Max Gauge](../../../core/meters/max-gauge.md) for the concept.

Create one via the [Registry](../registry/overview.md):

```java
public class Queue {

  private final Gauge queueSize;

  @Inject
  public Queue(Registry registry) {
    queueSize = registry.maxGauge("server.queueSize");
  }

  public void enqueue(Object obj) {
    impl.enqueue(obj);
    queueSize.set(impl.size());
  }
}
```

`Registry.maxGauge(...)` returns a [`Gauge`](https://static.javadoc.io/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/Gauge.html)
that retains the maximum value seen during a reporting interval and resets at the end of the
interval.
