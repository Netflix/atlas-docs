# Counter

See [Counter](../../../core/meters/counter.md) for the concept.

Counters are created using the [Registry](../registry/overview.md), which will be set up as part of
application initialization. For example:

```java
public class Queue {

  private final Counter insertCounter;
  private final Counter removeCounter;
  private final QueueImpl impl;

  @Inject
  public Queue(Registry registry) {
    insertCounter = registry.counter("queue.insert");
    removeCounter = registry.counter("queue.remove");
    impl = new QueueImpl();
  }
```

Then call increment when an event occurs:

```java
  public void insert(Object obj) {
    insertCounter.increment();
    impl.insert(obj);
  }

  public Object remove() {
    if (impl.nonEmpty()) {
      removeCounter.increment();
      return impl.remove();
    } else {
      return null;
    }
  }
```

Optionally, an amount can be passed in when calling increment. This is useful when a collection of
events happen together.

```java
  public void insertAll(Collection<Object> objs) {
    insertCounter.increment(objs.size());
    impl.insertAll(objs);
  }
}
```

## Batch Updates

For very high-volume updates within a single thread, `Counter` exposes a `batchUpdater` that
buffers updates and flushes them as a single operation. The trade-off is that updates are
delayed by up to `batchSize` events before they appear on the underlying counter.

```java
try (Counter.BatchUpdater updater = insertCounter.batchUpdater(1000)) {
  for (Object obj : objs) {
    impl.insert(obj);
    updater.increment();
  }
}
```

The updater is `AutoCloseable`; the try-with-resources block guarantees a final flush. See
[Performance Tips](../../../core/performance.md) for the cross-cutting guidance.
