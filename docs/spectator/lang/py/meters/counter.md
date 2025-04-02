A Counter is used to measure the rate at which an event is occurring. Considering an API endpoint,
a Counter could be used to measure the rate at which it is being accessed.

Counters are reported to the backend as a rate-per-second. In Atlas, the `:per-step` operator can
be used to convert them back into a value-per-step on a graph.

Call `increment()` when an event occurs:

```python
from spectator import Registry

registry = Registry()
registry.counter("server.numRequests").increment()

num_requests = registry.new_id("server.numRequests")
registry.counter_with_id(num_requests).increment()
```

You can also pass a value to `increment()`. This is useful when a collection of events happens
together:

```python
from spectator import Registry

registry = Registry()
registry.counter("queue.itemsAdded").increment(10)

num_requests = registry.new_id("server.numRequests")
registry.counter_with_id(num_requests).increment(10)
```
