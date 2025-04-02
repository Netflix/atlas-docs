## Migrating to 1.X

Version 1.X consists of a major rewrite that cleans up and simplifies the `spectator-py` thin client
API. It is designed to send metrics through [spectatord](https://github.com/Netflix-Skunkworks/spectatord).
As a result, some functionality has been moved to other modules, or removed. Most uses of the various
meters through the `GlobalRegistry` will continue to work as expected, although migrating to the new
`Registry` usage pattern is advised. A key addition is the ability to work directly with complex
`MeterId` objects, which offers more ways to compose tags.

### New

#### Config

* Replace the `SidecarConfig` with `Config`, and simplify usage.
* The `location` configuration is clarified, with a default set to the `spectatord` UDP port, and a
new option for picking the default Unix Domain Socket for `spectatord`.
* The `extra_common_tags` concept is clarified. Any extra common tags provided through the `Config`
object are merged with two process-specific tags that may be present in environment variables.
* Any `MeterId` or `Meter` objects created through `Registry` methods will contain these extra tags.

#### Common Tags

A few local environment common tags are now automatically added to all Meters. Their values are read
from the environment variables.

| Tag          | Environment Variable |
|--------------|----------------------|
| nf.container | TITUS_CONTAINER_NAME |
| nf.process   | NETFLIX_PROCESS_NAME |

Tags from environment variables take precedence over tags passed on code when creating the `Config`.

Note that common tags sourced by [spectatord](https://github.com/Netflix-Skunkworks/spectatord) can't be overwritten.

#### Meters

* Implemented new meter types supported by [SpectatorD]: `AgeGauge`, `MaxGauge` and `MonotonicCounter`.
See the `spectatord` documentation or the class docstrings for more details.
* The `AgeGauge` meter added a `now()` method, which sets `0` as the value, so you do not need to
remember this special value.
* Add `MonotonicCounterUint` with a `c_uint64` data type, to support `uint64` data types. These are
not commonly encountered, as they usually only show up in networking metrics, such as bytes/sec in
high-volume contexts. When you need it, you need it, else wise, it can be ignored.
* The `MonotonicCounter` with a `float` data type continues to exist, for the more common use case.
* Note that monotonic counters are convenience meter types provided by `spectatord`, because they
help you avoid the work of tracking previous values and calculating deltas.

#### Registry

* Add a `new_id()` method and `*_with_id()` methods for all meter types, to support more complex
tag operations related to `MeterId` objects. This follows the way they work in the other clients.

### Moved

#### Meters

* Separate classes for each `Meter` type. Relocated to a new module, `spectator.meter`, and exposed
through top-level imports, for convenience.
* The `MeterId` class was moved to the `spectator.meter` module and simplified.
* The `spectator.histogram` meters `PercentileTimer` and `PercentileDistribution` summary were moved
to `spectator.meter` and are now accessible from the `Registry` interface.

#### StopWatch

* The `StopWatch` context manager is no longer part of the `Timer` class; it is now a standalone
class. It has been preserved, because it continues to fulfill the purpose of simplifying how `Timer`
and `PercentileTimer` meters record their values after exiting a block of code, and there are a few
uses of this class across the organization.
* The `Clock` class continues to exist, in order to support testing the `StopWatch` deterministically.

Before:

```python
import time
from spectator import GlobalRegistry

server_latency = GlobalRegistry.pct_timer("serverLatency")

with server_latency.stopwatch():
    time.sleep(5)
```

After:

```python
import time
from spectator import Registry, StopWatch

registry = Registry()
server_latency = registry.pct_timer("serverLatency")

with StopWatch(server_latency):
    time.sleep(5)
```

#### Writers

* Separate classes for each `Writer` type. Relocated to a new module, `spectator.writer`, and exposed
through top-level imports, for convenience.

### Removed

All the removed items are from the legacy thick client.

* `spectator.http` is removed. Use the standard library HTTP client, or Requests instead.
* The `Meter` classes no longer have `_measure()` methods. Meters are now stateless and do not store
  measurements. The individual recording methods will call the writer to send the protocol line to
  `spectatord`.
* `spectator.config` is simplified and local to this library. There is no longer a need to import the internal
  configuration library.
* `spectator.registry` no longer has a `start()` method. The `Registry` is now effectively stateless and there is
  nothing to start other than opening the output location.
* `spectator.registry` no longer has a `stop()` function. Instead, use `close()` to close the Registry. Once the
  registry is closed, it can't be started again. This is intended for final clean up of sockets or file handles.
* `spectator.registry` no longer reports `spectator.measurements` metrics. Instead, you can use `spectatord` metrics to
  troubleshoot metrics delivery.
* `spectator.registry` no longer keeps track of the Meters it creates. This means that you can't get a list of all Meters
  from the Registry. If you need to keep track of Meters, you can do so in your application code.
* `spectator.histogram` meters `PercentileTimer` and `PercentileDistributionSummary` no longer support defining min/max
  values.

### Deprecated

* The `GlobalRegistry` is a hold-over from the thick-client version of this library, but it has been
maintained to help minimize the amount of code change that application owners need to implement
when adopting the thin-client version of the library. Replace with direct use of `Registry`.
* There are no plans to remove the `GlobalRegistry`, until we know that all uses have been removed.

Before:

```python
from spectator import GlobalRegistry

GlobalRegistry.gauge("server.queueSize", ttl_seconds=120).set(10)
```

After:

```python
from spectator import Registry

registry = Registry()
registry.gauge("server.queueSize", ttl_seconds=120).set(10)
```

### Migration Steps

1. Make sure you're not relying on any of the [removed functionality](#removed).
2. Update imports for `Config`, `Registry`, and any `Meter`s and `Writer`s that are used for testing.
3. If you want to collect runtime metrics, add the [spectator-py-runtime-metrics] library, and follow
   the instructions in the README.
4. If you use `PercentileDistributionSummary` or `PercentileTimer`, then update your code to use the
   respective functions provided by the `Registry` to initialize these meters.
5. Remove the dependency on the `spectator-py` internal configuration library - it is no longer required.
6. There is no longer an option to `start()` or `stop()` the Registry at runtime. If you need to
   configure a `Registry` that doesn't emit metrics for testing purposes, then create a `Config` object
   with a `location` of `none`, to configure a no-op writer, and pass it to the `Registry`.

[spectator-py-runtime-metrics]: https://github.com/Netflix/spectator-py-runtime-metrics

## Migrating to 0.2

* This library no longer publishes directly to the Atlas backends. It now publishes to the
[SpectatorD] sidecar which is bundled with all standard AMIs and containers. If you must
have the previous direct publishing behavior, because SpectatorD is not yet available on the
platform where your code runs, then you can pin to version `0.1.18`.
* The internal Netflix configuration companion library is no longer required and this dependency
may be dropped from your project.
* The API surface area remains unchanged to avoid breaking library consumers, and standard uses of
`GlobalRegistry` helper methods for publishing metrics continue to work as expected. Several helper
methods on meter classes are now no-ops, always returning values such as `0` or `nan`. If you want
to write tests to validate metrics publication, take a look at the tests in this library for a few
examples of how that can be done. The core idea is to capture the lines which will be written out
to SpectatorD.
* Replace uses of `PercentileDistributionSummary` with direct use of the Registry
`pct_distribution_summary` method.

    ```
    # before
    from spectator import GlobalRegistry
    from spectator.histogram import PercentileDistributionSummary
    
    d = PercentileDistributionSummary(GlobalRegistry, "server.requestSize")
    d.record(10)
    ```

    ```
    # after
    from spectator import GlobalRegistry
    
    GlobalRegistry.pct_distribution_summary("server.requestSize").record(10)
    ```

* Replace uses of `PercentileTimer` with direct use of the Registry `pct_timer` method.

    ```
    # before
    from spectator import GlobalRegistry
    from spectator.histogram import PercentileTimer
    
    t = PercentileTimer(GlobalRegistry, "server.requestSize")
    t.record(0.01)
    ```
    
    ```
    # after
    from spectator import GlobalRegistry
    
    GlobalRegistry.pct_timer("server.requestSize").record(0.1)
    ```

* Implemented new meter types supported by [SpectatorD]: `age_gauge`, `max_gauge` and
`monotonic_counter`. See the SpectatorD documentation or the class docstrings for
more details.

[SpectatorD]: ../../agent/usage.md
