## Project

[![Build Status](https://travis-ci.org/Netflix/spectator.svg?branch=master)](https://travis-ci.org/Netflix/spectator)

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
instrumented data to [Atlas](http://github.com/Netflix/atlas/wiki/). See the appropriate
section for the type of project you are working on:

* [Libraries](#libraries)
* [Applications](#applications), specifically standalone apps using Guice or Governator directly.
* [Base Server](#base-server)

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

Libraries should not install `SpectatorModule`. The bindings to use for the [Registry] should be
determined by the [application](#application) that is using the library. Think of it as being like
slf4j where [logging configuration] is up to the end-user, not the library owner.

[logging configuration]: https://www.slf4j.org/faq.html#configure_logging

When creating a Guice module for your library, you may want to avoid binding errors if the end-user
has not provided a binding for the Spectator registry. This can be done by using optional injections
inside of the module, for example:

```java
// Sample library class
public class MyLib {
  Registry registry;

  @Inject
  public MyLib(Registry registry) {
    this.registry = registry;
  }
}

// Guice module to configure the library and setup the bindings
public class MyLibModule extends AbstractModule {

  private static final Logger LOGGER = LoggerFactory.getLogger(MyLibModule.class);

  @Override
  protected void configure() {
  }

  @Provides
  private MyLib provideMyLib(OptionalInjections opts) {
    return new MyLib(opts.registry());
  }

  private static class OptionalInjections {
    @Inject(optional = true)
    private Registry registry;

    Registry registry() {
      if (registry == null) {
        LOGGER.warn("no spectator registry has been bound, so using noop implementation");
        registry = new NoopRegistry();
      }
      return registry;
    }
  }
}
```

### Applications

Applications should include a dependency on the `atlas-client` plugin:

```
netflix:atlas-client:latest.release
```

Note this is an internal-only library with configs specific to the Netflix environments. It
is assumed you are using [Nebula] so that internal Maven repositories are available for your
build. When configuring with Governator, specify the `AtlasModule`:

```java
Injector injector = LifecycleInjector.builder()
    .withModules(new AtlasModule())
    .build()
    .createInjector();
```

The [Registry] binding will then be available for injection as shown in the [libraries section].
The Insight libraries do not use any Governator or Guice specific features. It is possible to
use Guice or other dependency injection frameworks directly with the following caveats:

1. Some of the libraries use the [@PostConstruct] and [@PreDestroy] annotations for managing
lifecycle. Governator adds lifecycle management and many other features on top of Guice and is
the recommended way. For more minimalist support of just the lifecycle annotations on top of
Guice, see [iep-guice].
1. The bindings and configuration necessary to run correctly with the internal setup are only
supported as Guice modules. If you are trying to use some other dependency injection framework,
then you will be responsible for either finding a way to leverage the Guice module in that
framework or recreating those bindings and maintaining them as things change. It is not a
paved path.

[Nebula]: https://nebula-plugins.github.io/
[libraries section]: #libraries
[@PostConstruct]: http://docs.oracle.com/javaee/7/api/javax/annotation/PostConstruct.html
[@PreDestroy]: http://docs.oracle.com/javaee/7/api/javax/annotation/PreDestroy.html
[iep-guice]: https://github.com/Netflix/iep/tree/master/iep-guice#description

### Base Server

If using `base-server`, then you will get the Spectator and Atlas bindings automatically.

### Auto Plugin

!!! warning
    **Deprecated**: Use of `AutoBindSingleton` is generally discouraged. It is recommended to
    use one of the other methods.

If you are only interested in getting the GC logging, then there is a library with an auto-bind
singleton that can be used:

```
com.netflix.spectator:spectator-nflx:{{ spectator_api.java_latest }}
```

Assuming you are using karyon/base-server or Governator with `com.netflix` in the list of base
packages, then the plugin should be automatically loaded.
