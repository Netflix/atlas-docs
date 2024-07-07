The value is the number of seconds that have elapsed for an event, with percentile estimates.

This metric type will track the data distribution by maintaining a set of Counters. The
distribution can then be used on the server side to estimate percentiles, while still
allowing for arbitrary slicing and dicing based on dimensions.

In order to maintain the data distribution, they have a higher storage cost, with a worst-case of
up to 300X that of a standard Timer. Be diligent about any additional dimensions added to Percentile
Timers and ensure that they have a small bounded cardinality.

Call `record()` with a value:

```python
from spectator import GlobalRegistry

GlobalRegistry.pct_timer("server.requestLatency").record(0.01)
```

A `stopwatch()` method is available which may be used as a [Context Manager](https://docs.python.org/3/reference/datamodel.html#context-managers)
to automatically record the number of seconds that have elapsed while executing a block of code:

```python
import time
from spectator import GlobalRegistry

t = GlobalRegistry.pct_timer("thread.sleep")

with t.stopwatch():
    time.sleep(5)
```
