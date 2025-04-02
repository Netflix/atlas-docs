A Timer is used to measure how long (in seconds) some event is taking.

Call `record()` with a value:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.timer("server.requestLatency").record(0.01);

const request_latency = registry.new_id("server.requestLatency");
void registry.timer_with_id(request_latency).record(0.01);

const start = process.hrtime();
// do work
void registry.timer("server.requestLatency").record(process.hrtime(start));
```

The `record()` method accepts `number[]` output from `hrtime` and converts it to seconds, as a
convenience for recording latencies.
