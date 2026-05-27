# Distribution Summary

See [Distribution Summary](../../../core/meters/dist-summary.md) for the concept.

Distribution Summaries are created using the [Registry](../registry/overview.md), which will be
set up as part of application initialization. For example:

```java
public class Server {

  private final DistributionSummary requestSize;

  @Inject
  public Server(Registry registry) {
    requestSize = registry.distributionSummary("server.requestSize");
  }
```

Then call record when an event occurs:

```java
  public Response handle(Request request) {
    requestSize.record(request.sizeInBytes());
  }
}
```
**Note:** If the amount recorded is less than 0 the value will be dropped.

## Batch Updates

For very high-volume updates within a single thread, `DistributionSummary` exposes a
`batchUpdater` that buffers updates and flushes them as a single operation. See
[Performance Tips](../../../core/performance.md) for the cross-cutting guidance and
[`Counter.batchUpdater`](counter.md#batch-updates) for an annotated example.

## Percentile Distribution Summary

Use a regular [Distribution Summary](#distribution-summary) unless percentile estimates are
required.

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
