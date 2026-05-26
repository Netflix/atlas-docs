# Age Gauge

See [Age Gauge](../../../patterns/age-gauge.md) for the concept.

Java does not have a dedicated Age Gauge meter. Use a [Polled Meter](../patterns/polled-meter.md)
together with the [`Functions.AGE`](https://www.javadoc.io/static/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/Functions.html#AGE)
helper, which computes the age in seconds from a wall-time millis timestamp stored in an
`AtomicLong`:

```java
public class Job {

  private final AtomicLong lastSuccess;

  @Inject
  public Job(Registry registry) {
    lastSuccess = PolledMeter.using(registry)
        .withName("job.timeSinceLastSuccess")
        .monitorValue(new AtomicLong(System.currentTimeMillis()), Functions.AGE);
  }

  public void onSuccess() {
    lastSuccess.set(System.currentTimeMillis());
  }
}
```

This reports the seconds elapsed since the last successful run, which is the basis for the
Time Since Last Success alerting pattern.

For tests that need to control time, use [`Functions.age(Clock)`](https://www.javadoc.io/static/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/Functions.html#age-com.netflix.spectator.api.Clock-)
with a `ManualClock` (typically the same clock used by the test `Registry`):

```java
ManualClock clock = new ManualClock();
Registry registry = new DefaultRegistry(clock);

PolledMeter.using(registry)
    .withName("job.timeSinceLastSuccess")
    .monitorValue(new AtomicLong(clock.wallTime()), Functions.age(clock));
```
