# Registry

The [Registry] is the main class for managing a set of meters. A [Meter] is a class for collecting
a set of measurements about your application.

[Registry]: https://static.javadoc.io/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/com/netflix/spectator/api/Registry.html
[Meter]: https://static.javadoc.io/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/com/netflix/spectator/api/Meter.html

## Choose Implementation

The core Spectator library, `spectator-api`, comes with the following [Registry] implementations:

<table>
    <tr>
        <th>Class
        <th>Dependency
        <th>Description
    <tr>
        <td><a href="https://static.javadoc.io/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/com/netflix/spectator/api/DefaultRegistry.html">DefaultRegistry</a>
        <td>spectator-api
        <td>
        Updates local counters, frequently used with <a href="../../testing">unit tests</a>.
    <tr>
        <td><a href="https://static.javadoc.io/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/com/netflix/spectator/api/NoopRegistry.html">NoopRegistry</a>
        <td>spectator-api
        <td>
        Does nothing, tries to make operations as cheap as possible.
        <br><br>
        This implementation is typically used to help understand the overhead being created
        due to instrumentation. It can also be useful in testing to help ensure that no side
        effects were introduced where the instrumentation is now needed in order for the
        application for function properly.
    <tr>
        <td><a href="https://static.javadoc.io/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/com/netflix/spectator/metrics3/MetricsRegistry.html">MetricsRegistry</a>
        <td><a href="../metrics3">spectator-reg-metrics3</a>
        <td>
        Map to <a href="http://metrics.dropwizard.io/3.1.0/">metrics3 library</a>.
        <br><br>
        This implementation is typically used for reporting to local files, JMX, or other
        backends like Graphite. Note that it uses a hierarchical naming scheme rather
        than the dimensional naming used by Spectator, so the names will get flattened
        when mapped to this Registry.
</table>

It is recommended for libraries to write code against the [Registry] interface and allow the
implementation to get injected by the user of the library. The simplest way is to accept the
Registry via the constructor, for example:

```java
public class HttpServer {
  public HttpServer(Registry registry) {
    // use registry to collect measurements
  }
}
```

The user of the class can then provide the implementation:

```java
Registry registry = new DefaultRegistry();
HttpServer server = new HttpServer(registry);
```

More complete examples can be found on the [testing page](../testing.md) or in the
[spectator-examples repo](https://github.com/brharrington/spectator-examples).

## Working with Ids

Spectator is primarily intended for collecting data for dimensional time series backends like
[Atlas](https://github.com/Netflix/atlas). The ids used for looking up a [Meter] in the [Registry]
consist of a name and set of tags. Ids will be consumed many times by users after the data has
been reported, so they should be chosen with some care and thought about how they will get used.
See the [conventions page](../../../../concepts/naming.md) for some general guidelines.

Ids are created via the Registry, for example:

```java
Id id = registry.createId("server.requestCount");
```

The ids are immutable, so they can be freely passed around and used in a concurrent context.
Tags can be added when an id is created:

```java
Id id = registry.createId(
    "server.requestCount",
    "status", "2xx",
    "method", "GET"
);
```

Or by using `withTag` and `withTags` on an existing id:

```java
public class HttpServer {
  private final Id baseId;

  public HttpServer(Registry registry) {
    baseId = registry.createId("server.requestCount");
  }

  private void handleRequestComplete(HttpRequest req, HttpResponse res) {
    // Remember Id is immutable, withTags will return a copy with the
    // the additional metadata
    Id reqId = baseId.withTags(
      "status", res.getStatus(),
      "method", req.getMethod().name());
    registry.counter(reqId).increment();
  }

  private void handleRequestError(HttpRequest req, Throwable t) {
    // Can also be added individually using `withTag`. However, it is better
    // for performance to batch modifications using `withTags`.
    Id reqId = baseId
      .withTag("error",  t.getClass().getSimpleName())
      .withTag("method", req.getMethod().name());
    registry.counter(reqId).increment();
  }
}
```

## Collecting Measurements

Once you have an id, the [Registry] can be used to get an instance of a [Meter] to record a
measurement. Meters can roughly be categorized in two groups:

### Active

Active Meters are ones that are called directly when some event occurs. There are three basic
types supported:

* **[Counters](../../../core/meters/counter.md)** measure how often something is occurring. This
will be reported to backend systems as a rate-per-second. For example, the number of requests
processed by a web server.
* **[Timers](../../../core/meters/timer.md)** measure how long something took. For example,
the latency of requests processed by a web server.
* **[Distribution Summaries](../../../core/meters/dist-summary.md)** measure the size of
something. For example, the entity sizes for requests processed by a web server.

### Passive

Passive Meters are ones where the Registry has a reference to get the value when needed. For
example, the number of current connections on a web server or the number threads that are
currently in use. These will be [Gauges](../../../core/meters/gauge.md).

## Global Registry

There are some use-cases where injecting the [Registry] is not possible or is too cumbersome. The
main example from the core Spectator libraries is the [log4j appender](../ext/log4j2.md). The
[Global Registry] is useful there because logging is often initialized before any other systems
and Spectator itself uses logging via the slf4j api which is quite likely being bound to log4j
when that the appender is being used. By using the Global Registry, the logging initialization
can proceed before the Spectator initialization in the application. Though any measurements
taken before a Registry instance has been added will be lost.

The Global Registry is accessed using:

```java
Registry registry = Spectator.globalRegistry();
```

By default, it will not record anything. For a specific registry instance you can choose to
configure it to work with the Global Registry by calling `add`:

```java
public void init() {
  Registry registry = // Choose an appropriate implementation
  
  // Add it to the global registry so it will receive
  // any activity on the global registry
  Spectator.globalRegistry().add(registry);
}
```

Any measurements taken while no Registries are added to the global instance will be lost. If
multiple Registries are added, all will receive updates made to the Global Registry.

[Global Registry]: https://static.javadoc.io/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/com/netflix/spectator/api/Spectator.html#globalRegistry--
