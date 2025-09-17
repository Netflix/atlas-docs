## Timer

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

## Units

Ensure that you always report values in seconds (see [Use Base Units]). The API does not offer any
guarantees that the value will be in seconds.

If you use [time.perf_counter()] to measure elapsed time in a high-resolution format, then the value
returned will be in fractional seconds. As of Python 3.13, the implementation was changed to use the
same clock as [time.monotonic()]. If you choose to use [time.monotonic_ns()], to avoid the precision
loss caused by the float type, then you need to convert back to seconds.

[Use Base Units]: ../../../../concepts/naming.md#use-base-units
[time.perf_counter()]: https://docs.python.org/3/library/time.html#time.perf_counter
[time.monotonic()]: https://docs.python.org/3/library/time.html#time.monotonic
[time.monotonic_ns()]: https://docs.python.org/3/library/time.html#time.monotonic_ns
