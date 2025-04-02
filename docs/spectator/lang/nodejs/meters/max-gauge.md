The value is a number that is sampled at a point in time, but it is reported as a maximum Gauge
value to the backend. This ensures that only the maximum value observed during a reporting interval
is sent to the backend, thus over-riding the last-write-wins semantics of standard Gauges. Unlike
standard Gauges, Max Gauges do not continue to report to the backend, and there is no TTL.

Call `set()` with a value:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.max_gauge("server.queueSize").set(10);

const queue_size = registry.new_id("server.queueSize");
void registry.max_gauge_with_id(queue_size).set(10);
```
