# Java Gauges

## Polled Gauges

The most common use of Gauges is by registering a hook with Spectator, so that it will poll the
values in the background. This is done by using the [PolledMeter] helper class.

[PolledMeter]: https://static.javadoc.io/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/com/netflix/spectator/api/patterns/PolledMeter.html 

A Polled Gauge is registered by passing in an id, a reference to the object, and a function to get
or compute a numeric value based on the object. Note that a Gauge should only be registered once,
not on each update. Consider this example of a web server tracking the number of connections:

```java
class HttpServer {
  // Tracks the number of current connections to the server
  private AtomicInteger numConnections;

  public HttpServer(Registry registry) {
    numConnections = PolledMeter.using(registry)
      .withName("server.numConnections")
      .monitorValue(new AtomicInteger(0));
  }

  public void onConnectionCreated() {
    numConnections.incrementAndGet();
    ...
  }

  public void onConnectionClosed() {
    numConnections.decrementAndGet();
    ...
  }

  ...
}
```

The Spectator [Registry](../registry/overview.md) will keep a weak reference to the object. If
the object is garbage collected, then it will automatically drop the registration. In the example
above, the Registry will have a weak reference to `numConnections` and the server instance will
have a strong reference to `numConnections`. If the server instance goes away, then the Gauge
will as well. 

When multiple Gauges are registered with the same id, the reported value will be the sum of the
matches. For example, if multiple instances of the `HttpServer` class were created on different
ports, then the value `server.numConnections` would be the total number of connections across
all server instances. If a different behavior is desired, then ensure your usage does not perform
multiple registrations.

There are several different ways to register a Gauge:

### Using Number

A Gauge can also be created based on an implementation of Number. Note the Number implementation
should be thread-safe. For example:

```java
AtomicInteger size = new AtomicInteger();
PolledMeter.using(registry)
  .withName("queue.size")
  .monitorValue(size);
```

The call will return the Number so the registration can be inline on the assignment:

```java
AtomicInteger size = PolledMeter.using(registry)
  .withName("queue.size")
  .monitorValue(new AtomicInteger());
```

Updates to the value are performed by updating the Number instance directly.

### Using Lambda

Specify a lambda that takes the object as parameter.

```java
public class Queue {

  @Inject
  public Queue(Registry registry) {
    PolledMeter.using(registry)
      .withName("queue.size")
      .monitorValue(this, Queue::size);
  }

  ...
}
```

!!! warning
    Be careful to avoid creating a reference to the object in the lambda. It will prevent garbage
    collection and can lead to a memory leak in the application. For example, by calling size
    without using the passed in object there will be a reference to `this`:

    ```
    PolledMeter.using(registry)
      .withName("queue.size")
      .monitorValue(this, obj -> size());
    ```

### Collection Sizes

For classes that implement `Collection` or `Map`, there are helpers:

```java
Queue queue = new LinkedBlockingQueue();
PolledMeter.using(registry)
  .withName("queue.size")
  .monitorSize(queue);

Map<String, String> cache = new ConcurrentMap<>();
PolledMeter.using(registry)
  .withName("cache.size")
  .monitorSize(cache);
```

### Monotonic Counters

A common technique used by some libraries is to expose a monotonically increasing counter that
represents the number of events since the system was initialized. An example of that in the JDK
is [ThreadPoolExecutor.getCompletedTaskCount], which returns the number of completed tasks on
the thread pool.

[ThreadPoolExecutor.getCompletedTaskCount]: https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadPoolExecutor.html#getCompletedTaskCount--

For sources like this, the `monitorMonotonicCounter` method can be used:

```java
// For an implementation of Number
LongAdder tasks = new LongAdder();
PolledMeter.using(registry)
  .withName("pool.completedTasks")
  .monitorMonotonicCounter(tasks);

// Or using a lambda
ThreadPoolExecutor executor = ...
PolledMeter.using(registry)
  .withName("pool.completedTasks")
  .monitorMonotonicCounter(executor, ThreadPoolExecutor::getCompletedTaskCount);
```

For thread pools specifically, there are better options for getting standard metrics. See the docs
for the [Thread Pools extension](../ext/thread-pools.md) for more information.

## Active Gauges

Gauges can also be set directly by the user. In this mode, the user is responsible for regularly
updating the value of the Gauge by calling `set`. Looking at the HttpServer example, with an active
gauge, it would look like:

```java
class HttpServer {
  // Tracks the number of current connections to the server
  private AtomicInteger numConnections;
  private Gauge gauge;

  public HttpServer(Registry registry) {
    numConnections = new AtomicInteger();
    gauge = registry.gauge("server.numConnections");
    gauge.set(numConnections.get());
  }

  public void onConnectionCreated() {
    numConnections.incrementAndGet();
    gauge.set(numConnections.get());
    ...
  }

  public void onConnectionClosed() {
    numConnections.decrementAndGet();
    gauge.set(numConnections.get());
    ...
  }

  ...
}
```
