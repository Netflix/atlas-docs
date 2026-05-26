# Max Gauge

See [Max Gauge](../../../core/meters/max-gauge.md) for the concept.

Call `set()` with a value:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.max_gauge("server.queueSize").set(10);

const queue_size = registry.new_id("server.queueSize");
void registry.max_gauge_with_id(queue_size).set(10);
```
