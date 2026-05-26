# Gauge

See [Gauge](../../../core/meters/gauge.md) for the concept.

Call `set()` with a value:

```python
from spectator import Registry

registry = Registry()
registry.gauge("server.queueSize").set(10)

queue_size = registry.new_id("server.queueSize")
registry.gauge_with_id(queue_size).set(10)
```

Gauges will report the last set value for 15 minutes. This done so that updates to the values do
not need to be collected on a tight 1-minute schedule to ensure that Atlas shows unbroken lines in
graphs. A custom TTL may be configured for gauges. SpectatorD enforces a minimum TTL of 5 seconds.

```python
from spectator import Registry

registry = Registry()
registry.gauge("server.queueSize", ttl_seconds=120).set(10)

queue_size = registry.new_id("server.queueSize")
registry.gauge_with_id(queue_size, ttl_seconds=120).set(10)
```