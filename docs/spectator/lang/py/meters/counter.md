# Counter

See [Counter](../../../core/meters/counter.md) for the concept.

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