A Timer is used to measure how long (in seconds) some event is taking.

Call `record()` with a value:

```python
from spectator import GlobalRegistry

GlobalRegistry.timer("server.requestLatency").record(0.01)
```

A `stopwatch()` method is available which may be used as a [Context Manager] to automatically record
the number of seconds that have elapsed while executing a block of code:

```python
import time
from spectator import GlobalRegistry

t = GlobalRegistry.timer("thread.sleep")

with t.stopwatch():
    time.sleep(5)
```

Internally, Timers will keep track of the following statistics as they are used:

* `count`
* `totalTime`
* `totalOfSquares`
* `max`

[Context Manager]: https://docs.python.org/3/reference/datamodel.html#context-managers
