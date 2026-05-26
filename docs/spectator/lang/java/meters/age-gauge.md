# Age Gauge

See [Age Gauge](../../../patterns/age-gauge.md) for the concept.

Java does not have a dedicated Age Gauge meter. The equivalent is a [Polled Meter](../../../patterns/polled-meter.md)
that computes `now - lastSuccessTimestamp` on each poll:

```java
public class Job {

  private final AtomicLong lastSuccess;

  @Inject
  public Job(Registry registry) {
    lastSuccess = PolledMeter.using(registry)
        .withName("job.timeSinceLastSuccess")
        .monitorValue(
            new AtomicLong(registry.clock().wallTime() / 1000),
            ts -> (registry.clock().wallTime() / 1000) - ts.get());
  }

  public void onSuccess() {
    lastSuccess.set(registry.clock().wallTime() / 1000);
  }
}
```

This reports the seconds elapsed since the last successful run, which is the basis for the
Time Since Last Success alerting pattern.
