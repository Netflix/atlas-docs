# Counter

See [Counter](../../../core/meters/counter.md) for the concept.

Call `increment()` when an event occurs:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.counter("server.numRequests").increment();

const num_requests = registry.new_id("server.numRequests");
void registry.counter_with_id(num_requests).increment();
```

You can also pass a value to `increment()`. This is useful when a collection of events happens
together:

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.counter("queue.itemsAdded").increment(10);

const num_requests = registry.new_id("server.numRequests");
void registry.counter_with_id(num_requests).increment(10);
```