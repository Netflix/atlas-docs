## Migrating from 0.2 to 1.0

Version 1.0 consists of a major rewrite that cleans up and simplifies the `spectator-py` thin client
API. It is designed to send metrics through [spectatord](https://github.com/Netflix-Skunkworks/spectatord).
As a result, some functionality has been moved to other modules, or removed.

### New

#### Config

* Replace the `SidecarConfig` with `Config`, and simplify usage.
* The `location` configuration is clarified, with a default set to the `spectatord` UDP port, and a
new option for picking the default Unix Domain Socket for `spectatord`.
* The `extra_common_tags` concept is clarified. Any extra common tags provided through the `Config`
object are merged with two process-specific tags that may be present in environment variables.
* Any `MeterId` or `Meter` objects created through `Registry` methods will contain these extra tags.

#### Meters

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

* Separate classes for each `Meter` type. Relocated to a new module, `spectator.meter`.

#### StopWatch

* The `StopWatch` context manager is no longer part of the `Timer` class; it is now a standalone
class. It has been preserved, because it continues to fulfill the purpose of simplifying how `Timer`
and `PercentileTimer` meters record their values after exiting a block of code, and there are a few
uses of this class across the organization.

**Before:**

```python
import time
from spectator import GlobalRegistry

server_latency = GlobalRegistry.pct_timer("serverLatency")

with server_latency.stopwatch():
    time.sleep(5)
```

**After:**

```python
import time
from spectator.registry import Registry
from spectator.stopwatch import StopWatch

registry = Registry()
server_latency = registry.pct_timer("serverLatency")

with StopWatch(server_latency):
    time.sleep(5)
```

#### Writers

* Separate classes for each `Writer` type. Relocated to a new module, `spectator.writer`.

### Removed

* All remnants of the previous thick-client API.

### Deprecated

* The `GlobalRegistry` is a hold-over from the thick-client version of this library, but it has been
maintained to help minimize the amount of code change that application owners need to implement
when adopting the thin-client version of the library. Replace with direct use of `Registry`.
* There are no plans to remove the `GlobalRegistry`, until we know that all uses have been removed.

**Before:**

```python
from spectator import GlobalRegistry

GlobalRegistry.gauge("server.queueSize", ttl_seconds=120).set(10)
```

**After:**

```python
from spectator.registry import Registry

registry = Registry()
registry.gauge("server.queueSize", ttl_seconds=120).set(10)
```

## Migrating from 0.1 to 0.2

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
