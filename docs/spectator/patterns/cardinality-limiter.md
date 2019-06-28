# Cardinality Limiter

Helper functions to help manage the cardinality of tag values. This should be used anywhere you
cannot guarantee that the tag values being used are strictly bounded. There is support for two
different modes: (1) selecting the first N values that are seen, or (2) selecting the most
frequent N values that are seen.

Example usage:

```java
class WebServer {

  // Limiter instance, should be shared for all uses of that tag value
  private final Function&lt;String, String&gt; pathLimiter =
    CardinalityLimiters.mostFrequent(10);

  private final Registry registry;
  private final Id baseId;

  public WebServer(Registry registry) {
    this.registry = registry;
    this.baseId = registry.createId("server.requestCount");
  }

  public Response handleRequest(Request req) {
    Response res = doSomething(req);

    // Update metrics, use limiter to restrict the set of values for the
    // path and avoid an explosion
    String pathValue = pathLimiter.apply(req.getPath());
    Id id = baseId
      .withTag("path", pathValue)
      .withTag("status", res.getStatus());
    registry.counter(id).increment();
  }
}
```
