# Monotonic Counter

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept.

Call `set()` when an event occurs:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.monotonic_counter("iface.bytes").set(10);

const iface_bytes = registry.new_id("iface.bytes");
void registry.monotonic_counter_with_id(iface_bytes).set(10)
```
