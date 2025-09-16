## Timer

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

## Units

If you use [process.hrtime()] or [process.hrtime.bigint()] to calculate the elapsed time, then the
units will be converted to seconds when reporting values.

If you use a plain `number` value to record values, then ensure that you always report values in
seconds (see [Use Base Units]). No conversion assistance is provided in this case.

[process.hrtime()]: https://nodejs.org/api/process.html#processhrtimetime
[process.hrtime.bigint()]: https://nodejs.org/api/process.html#processhrtimebigint
[Use Base Units]: ../../../../concepts/naming.md#use-base-units
