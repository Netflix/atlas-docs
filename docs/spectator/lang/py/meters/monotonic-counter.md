# Monotonic Counter

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept.

Call `set()` when an event occurs:

```python
from spectator import Registry

registry = Registry()
registry.monotonic_counter("iface.bytes").set(10)

iface_bytes = registry.new_id("iface.bytes")
registry.monotonic_counter_with_id(iface_bytes).set(10)
```
