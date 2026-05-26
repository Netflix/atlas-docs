# Age Gauge

An Age Gauge reports the time in seconds since some event last occurred successfully.
It is a use of a [Gauge](../core/meters/gauge.md) where the value reported is computed
as `now - lastSuccessTimestamp` on each reporting interval.

The primary use case is the **Time Since Last Success** alerting pattern: alert when a
periodic job, heartbeat, or freshness signal stops advancing.

## Implementations

For the spectatord-backed clients (C++, Go, Node.js, Python), Age Gauge is exposed as a
first-class meter type. The client records the last-success timestamp (or `now()`) and
spectatord handles the elapsed-time calculation on each reporting interval, continuing to
report for as long as the spectatord process runs.

For Java, there is no dedicated Age Gauge meter. The equivalent is a polled gauge that
computes the age on each poll — see [Polled Meter](polled-meter.md):

```java
AtomicLong lastSuccess = new AtomicLong(System.currentTimeMillis() / 1000);
PolledMeter.using(registry)
    .withName("time.sinceLastSuccess")
    .monitorValue(lastSuccess, ts -> (System.currentTimeMillis() / 1000) - ts.get());

// On successful event:
lastSuccess.set(System.currentTimeMillis() / 1000);
```

## Lifecycle (spectatord-backed clients)

Age Gauges are long-lived in the spectatord process — once set they continue reporting
indefinitely. To prevent leaks, spectatord enforces a per-process limit (default `1000`,
tunable via `--age_gauge_limit`). If you need to remove or replace one, use the
[SpectatorD admin server](../agent/usage.md#admin-server).

## Languages

* [C++](../lang/cpp/meters/age-gauge.md)
* [Go](../lang/go/meters/age-gauge.md)
* [Java](../lang/java/meters/age-gauge.md) (no dedicated meter; uses [Polled Meter](polled-meter.md))
* [Node.js](../lang/nodejs/meters/age-gauge.md)
* [Python](../lang/py/meters/age-gauge.md)
