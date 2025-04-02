A Monotonic Counter (float) is used to measure the rate at which an event is occurring, when the
source data is a monotonically increasing number. A minimum of two samples must be sent, in order to
calculate a delta value and report it to the backend as a rate-per-second. A variety of networking
metrics may be reported monotonically, and this metric type provides a convenient means of recording
these values, at the expense of a slower time-to-first metric.

Call `set()` when an event occurs:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.monotonic_counter("iface.bytes").set(10);

const iface_bytes = registry.new_id("iface.bytes");
void registry.monotonic_counter_with_id(iface_bytes).set(10)
```
