## Percentile Timer

The value is the number of seconds that have elapsed for an event, with percentile estimates.

This metric type will track the data distribution by maintaining a set of Counters. The
distribution can then be used on the server side to estimate percentiles, while still
allowing for arbitrary slicing and dicing based on dimensions.

In order to maintain the data distribution, they have a higher storage cost, with a worst-case of
up to 300X that of a standard Timer. Be diligent about any additional dimensions added to Percentile
Timers and ensure that they have a small bounded cardinality.

Call `record()` with a value:

```python
from spectator import Registry

registry = Registry()
registry.pct_timer("server.requestLatency").record(0.01)

request_latency = registry.new_id("server.requestLatency")
registry.pct_timer_with_id(request_latency).record(0.01)
```

A `StopWatch` class is available, which may be used as a [Context Manager] to automatically record
the number of seconds that have elapsed while executing a block of code:

```python
import time
from spectator import Registry, StopWatch

registry = Registry()
thread_sleep = registry.pct_timer("thread.sleep")

with StopWatch(thread_sleep):
    time.sleep(5)
```

[Context Manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

## Units

See [Timer Units](timer.md#units) for an explanation.
