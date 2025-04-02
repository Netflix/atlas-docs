The value is the number of seconds that have elapsed for an event, with percentile estimates.

This metric type will track the data distribution by maintaining a set of Counters. The
distribution can then be used on the server side to estimate percentiles, while still
allowing for arbitrary slicing and dicing based on dimensions.

In order to maintain the data distribution, they have a higher storage cost, with a worst-case of
up to 300X that of a standard Timer. Be diligent about any additional dimensions added to Percentile
Timers and ensure that they have a small bounded cardinality.

Call `record()` with a value:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.pct_timer("server.requestLatency").record(0.01);

const request_latency = registry.new_id("server.requestLatency");
void registry.pct_timer_with_id(request_latency).record(0.01);

const start = process.hrtime();
// do work
void registry.pct_timer("server.requestLatency").record(process.hrtime(start));
```

The `record()` method accepts `number[]` output from `hrtime` and converts it to seconds, as a
convenience for recording latencies.
