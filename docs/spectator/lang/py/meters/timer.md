A Timer is used to measure how long (in seconds) some event is taking.

Call `record()` with a value:

```python
from spectator import Registry

registry = Registry()
registry.timer("server.requestLatency").record(0.01)

request_latency = registry.new_id("server.requestLatency")
registry.timer_with_id(request_latency).record(0.01)
```

A `StopWatch` class is available, which may be used as a [Context Manager] to automatically record
the number of seconds that have elapsed while executing a block of code:

```python
import time
from spectator import Registry, StopWatch

registry = Registry()
thread_sleep = registry.timer("thread.sleep")

with StopWatch(thread_sleep):
    time.sleep(5)
```

[Context Manager]: https://docs.python.org/3/reference/datamodel.html#context-managers
