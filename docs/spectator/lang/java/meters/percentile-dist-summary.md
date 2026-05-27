# Percentile Distribution Summary

See [Percentile Distribution Summary](../../../patterns/percentile-dist-summary.md) for the
concept and storage-cost caveats. Use a regular [Distribution Summary](dist-summary.md) unless
percentile estimates are required.

Create one via the static builder:

```java
public class Server {

  private final PercentileDistributionSummary requestSize;

  @Inject
  public Server(Registry registry) {
    requestSize = PercentileDistributionSummary.builder(registry)
        .withId(registry.createId("server.requestSize"))
        .build();
  }

  public void onRequest(Request request) {
    requestSize.record(request.bodyBytes());
  }
}
```

The builder also accepts a range via `withRange(min, max)` to bound the bucket set and reduce
storage overhead — see the
[Javadoc](https://static.javadoc.io/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/histogram/PercentileDistributionSummary.html)
for details.
