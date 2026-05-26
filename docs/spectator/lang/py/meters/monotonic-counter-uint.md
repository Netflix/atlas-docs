# Monotonic Counter (uint64)

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept (uint64 variant).

Call `set()` when an event occurs:

```python
from ctypes import c_uint64
from spectator import Registry

registry = Registry()
registry.monotonic_counter_uint("iface.bytes").set(c_uint64(1))

iface_bytes = registry.new_id("iface.bytes")
registry.monotonic_counter_uint_with_id(iface_bytes).set(c_uint64(1))
```
