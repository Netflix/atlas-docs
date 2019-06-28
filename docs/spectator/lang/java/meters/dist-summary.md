# Java Distribution Summaries

Distribution Summaries are created using the [Registry](../registry/overview.md), which will be
setup as part of application initialization. For example:

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
