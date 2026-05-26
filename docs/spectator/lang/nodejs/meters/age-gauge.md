# Age Gauge

See [Age Gauge](../../../patterns/age-gauge.md) for the concept.

To set a specific time as the last success:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.age_gauge("time.sinceLastSuccess").set(1611081000);

const last_success = registry.new_id("time.sinceLastSuccess");
void registry.age_gauge_with_id(last_success).set(1611081000);
```

To set `now()` as the last success:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.age_gauge("time.sinceLastSuccess").now();

const last_success = registry.new_id("time.sinceLastSuccess");
void registry.age_gauge_with_id(last_success).now();
```

