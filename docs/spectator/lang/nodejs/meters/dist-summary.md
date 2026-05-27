# Distribution Summary

See [Distribution Summary](../../../core/meters/dist-summary.md) for the concept.

Call `record()` with a value:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.distribution_summary("server.requestSize").record(10);

const request_size = registry.new_id("server.requestSize");
void registry.distribution_summary_with_id(request_size).record(10);
```

## Percentile Distribution Summary

Call `record()` with a value:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.pct_distribution_summary("server.requestSize").record(10);

const request_size = registry.new_id("server.requestSize");
void registry.pct_distribution_summary_with_id(request_size).record(10);
```
