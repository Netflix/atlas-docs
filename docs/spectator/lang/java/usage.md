## Project

* [Source](https://github.com/Netflix/spectator)
* [Javadoc](https://www.javadoc.io/doc/com.netflix.spectator/spectator-api/) 
* **Product Lifecycle:** GA
* **Requirements:** Java >= 8

## Install Library

1. Depend on the API library, which is available in [Maven Central]. The only transitive dependency
is `slf4j`. For Gradle, the dependency is specified as follows:

    ```groovy
    dependencies {
        compile "com.netflix.spectator:spectator-api:{{ spectator_api.java_latest }}"
    }
    ```

1. Pick a [Registry] to bind, when initializing the application.

1. If running at Netflix, see the [Netflix Integration] section.

[Registry]: registry/overview.md
[Netflix Integration]: #netflix-integration
[Maven Central]: https://search.maven.org/artifact/com.netflix.spectator/spectator-api/{{ spectator_api.java_latest }}/jar

## Instrumenting Code

Suppose we have a server and we want to keep track of:

* Number of requests received with dimensions for breaking down by status code, country, and
  the exception type if the request fails in an unexpected way.
* Latency for handling requests.
* Summary of the response sizes.
* Current number of active connections on the server.

Here is some sample code that does that:

```java
// In the application initialization setup a registry
Registry registry = new DefaultRegistry();
Server s = new Server(registry);

public class Server {
  private final Registry registry;
  private final Id requestCountId;
  private final Timer requestLatency;
  private final DistributionSummary responseSizes;

  @Inject
  public Server(Registry registry) {
    this.registry = registry;

    // Create a base id for the request count. The id will get refined with
    // additional dimensions when we receive a request.
    requestCountId = registry.createId("server.requestCount");

    // Create a timer for tracking the latency. The reference can be held onto
    // to avoid additional lookup cost in critical paths.
    requestLatency = registry.timer("server.requestLatency");

    // Create a distribution summary meter for tracking the response sizes.
    responseSizes = registry.distributionSummary("server.responseSizes");

    // Gauge type that can be sampled. In this case it will invoke the
    // specified method via reflection to get the value. The registry will
    // keep a weak reference to the object passed in so that registration will
    // not prevent garbage collection of the server object.
    registry.methodValue("server.numConnections", this, "getNumConnections");
  }

  public Response handle(Request req) {
    final long s = System.nanoTime();
    requestLatency.record(() -> {
      try {
        Response res = doSomething(req);

        // Update the counter id with dimensions based on the request. The
        // counter will then be looked up in the registry which should be
        // fairly cheap, such as lookup of id object in a ConcurrentHashMap.
        // However, it is more expensive than having a local variable seti
        // to the counter.
        final Id cntId = requestCountId
          .withTag("country", req.country())
          .withTag("status", res.status());
        registry.counter(cntId).increment();

        responseSizes.record(res.body().size());

        return res;
      } catch (Exception e) {
        final Id cntId = requestCountId
          .withTag("country", req.country())
          .withTag("status", "exception")
          .withTag("error", e.getClass().getSimpleName());
        registry.counter(cntId).increment();
        throw e;
      }
    });
  }

  public int getNumConnections() {
    // however we determine the current number of connections on the server
  }
}
```

## Netflix Integration

When running at Netflix, use the `atlas-client` library to enable transferring the
instrumented data to [Atlas](../../../index.md). See the appropriate
section for the type of project you are working on:

* [Libraries](#libraries)
* [SBN Applications](#sbn-applications), specifically standalone apps using SBN.

### Libraries

For libraries, the only dependency that should be needed is:

```
com.netflix.spectator:spectator-api:{{ spectator_api.java_latest }}
```

The bindings to integrate internally should be included with the application. In your code,
just inject a [Registry], e.g.:

```java
public class Foo {
  @Inject
  public Foo(Registry registry) {
    ...
  }
  ...
}
```

See the [testing docs](testing.md) for more information about creating a binding to use with tests.
Libraries should not install a particular registry. The bindings to use for the [Registry] should be
determined by the [application](#sbn-applications) that is using the library. Think of it as being like
slf4j where [logging configuration] is up to the end-user, not the library owner.

[logging configuration]: https://www.slf4j.org/faq.html#configure_logging

You may want to avoid binding errors if the end-user has not provided a binding for the Spectator
registry. For Spring, this can be done by using optional injections, for example:

```java
// Sample library class
public class MyLib {
  Registry registry;

  @Inject
  public MyLib(Optional<Registry> registryOpt) {
    this.registry = registryOpt.orElseGet(NoopRegistry::new);
  }
}
```

### SBN Applications

Applications should include `spring-boot-netflix-starter-metrics` which will configure the
registry bindings for internal use.

