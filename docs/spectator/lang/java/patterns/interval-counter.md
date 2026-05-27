# Interval Counter

`IntervalCounter` is a [Counter](../meters/counter.md) that also reports the time in seconds
since the last update. Useful when you want an alert that fires if a counter stops being
incremented — the "Time Since Last Success" pattern applied to event-rate signals rather than
a separately-tracked timestamp.

Two time series are published with the same name, distinguished by the `statistic` tag:

* `statistic=count` — the underlying counter, reported as a rate-per-second.
* `statistic=duration` — a gauge of the seconds elapsed since the last `increment()` call.

Example:

```java
public class Job {

  private final IntervalCounter completions;

  @Inject
  public Job(Registry registry) {
    completions = IntervalCounter.get(registry, registry.createId("job.completions"));
  }

  public void run() {
    doWork();
    completions.increment();
  }
}
```

Then alert on the duration series rising above a threshold, e.g.
`statistic,duration,:eq,name,job.completions,:eq,:and,:max,3600,:gt`.

Implementation note: `IntervalCounter` uses [Polled Meter](polled-meter.md) with
[`Functions.age`](https://www.javadoc.io/static/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/Functions.html#age-com.netflix.spectator.api.Clock-)
under the hood. If you only need the freshness signal (without a separate counter), use a
plain polled meter directly — see [Age Gauge](../meters/age-gauge.md).
