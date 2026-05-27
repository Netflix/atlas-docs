# Performance Tips

A few patterns are worth keeping in mind when instrumenting hot paths. These apply across
all Spectator client libraries; language-specific helpers are noted where they exist.

## Cache the meter reference

`registry.counter("server.numRequests")` (and equivalents for timer, gauge, etc.) performs
a lookup in the registry on every call. For meters that don't have dynamic tag values,
look the meter up once and reuse the reference:

```java
// Good: lookup happens once.
private final Counter requests = registry.counter("server.numRequests");

public void handle() {
    requests.increment();
}
```

```java
// Avoid in hot paths: lookup on every call.
public void handle() {
    registry.counter("server.numRequests").increment();
}
```

For meters where some tag values are dynamic (e.g. a status code), cache the base `Id` and
derive per-request meters with `with_tag` / `withTag`:

```java
private final Id requestsId = registry.createId("server.numRequests");

public void handle(Response res) {
    registry.counter(requestsId.withTag("status", res.statusCode())).increment();
}
```

## Avoid instrumentation in tight loops

If you need to update a meter inside a tight loop where each iteration is cheap, the
instrumentation overhead can dominate. Accumulate locally and apply the delta once:

```java
long localCount = 0;
for (Item item : items) {
    if (item.isFoo()) localCount++;
}
requests.increment(localCount);
```

Java's [BatchUpdater](#java-batchupdater) automates this pattern for `Counter`,
`Timer`, and `DistributionSummary`.

## Prefer basic meters over percentile variants

[Percentile Timer](meters/timer.md#percentile-timer) and
[Percentile Distribution Summary](meters/dist-summary.md#percentile-distribution-summary)
maintain a set of bucket counters. Storage cost is up to ~300x that of the basic Timer or
Distribution Summary. Use them only for one or two key indicators per application, set an
appropriate range, and keep tag cardinality bounded.

## Thread Safety

Meter instances returned by a `Registry` are safe to use concurrently from multiple threads
in every Spectator client library. Holding a counter (or timer, etc.) in a shared field and
calling `increment()` / `record()` from many threads is the intended pattern.

A few exceptions to keep in mind:

* **Java `BatchUpdater`** — the updater returned by `Counter.batchUpdater(...)` (and the
  timer/dist-summary equivalents) is **single-thread only**. Give each thread its own
  updater, or fall back to direct meter calls for multi-threaded code paths. See
  [Batch Updates](../lang/java/meters/counter.md#batch-updates).
* **Polled gauges** — the value source you hand to a polled gauge (for example, the
  `AtomicLong` passed to `PolledMeter.monitorValue` in Java) must itself be thread-safe.
  Spectator polls the source from a background thread; if your code mutates it from
  another thread, use an atomic or synchronize externally.
* **Python multiprocessing** — see the
  [caveats](../lang/py/usage.md#caveats-multiprocessing) for fork-based workers that
  don't share thread-level state.

## Keep tag cardinality bounded

Every distinct combination of tag values produces a new time series. Avoid putting
high-cardinality values in tags — user IDs, request IDs, raw paths, etc. Use the
[Cardinality Limiter](../lang/java/patterns/cardinality-limiter.md) (Java) or apply a
similar mapping in other languages to cap the value set for any tag that could grow
unbounded.

## Java: BatchUpdater

For very high-volume updates within a single thread, `Counter`, `Timer`, and
`DistributionSummary` expose a `batchUpdater(batchSize)` method that buffers updates and
flushes them as a single operation. Trade-off: updates are delayed by up to `batchSize`
events before they appear on the underlying meter.

```java
try (Counter.BatchUpdater updater = requests.batchUpdater(1000)) {
    for (Item item : items) {
        process(item);
        updater.increment();
    }
}
```

The updater is `AutoCloseable`; the try-with-resources block guarantees a final flush. See
the [Counter](../lang/java/meters/counter.md), [Timer](../lang/java/meters/timer.md), and
[Distribution Summary](../lang/java/meters/dist-summary.md) pages for the per-meter
signatures.

The spectatord-backed clients (C++, Go, Node.js, Python) do not need an equivalent helper:
they buffer protocol lines client-side, and spectatord aggregates updates from many sources
before flushing to Atlas. Each language's usage page has a Line Buffer or Buffers section
for the relevant tuning knobs.
