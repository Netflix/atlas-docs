# Monotonic Counter (uint64)

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept (uint64 variant).

Call `set()` when an event occurs:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.monotonic_counter_uint("iface.bytes").set(BigInt(1));

const iface_bytes = registry.new_id("iface.bytes");
void registry.monotonic_counter_uint_with_id(iface_bytes).set(BigInt(1));
```
