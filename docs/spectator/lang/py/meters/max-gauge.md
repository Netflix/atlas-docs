# Max Gauge

See [Max Gauge](../../../core/meters/max-gauge.md) for the concept.

Call `set()` with a value:

```python
from spectator import Registry

registry = Registry()
registry.max_gauge("server.queueSize").set(10)

queue_size = registry.new_id("server.queueSize")
registry.max_gauge_with_id(queue_size).set(10)
```
