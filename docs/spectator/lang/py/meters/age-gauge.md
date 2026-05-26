# Age Gauge

See [Age Gauge](../../../patterns/age-gauge.md) for the concept.

To set a specific time as the last success:

```python
from spectator import Registry

registry = Registry()
registry.age_gauge("time.sinceLastSuccess").set(1611081000)

last_success = registry.new_id("time.sinceLastSuccess")
registry.age_gauge_with_id(last_success).set(1611081000)
```

To set `now()` as the last success:

```python
from spectator import Registry

registry = Registry()
registry.age_gauge("time.sinceLastSuccess").now()

last_success = registry.new_id("time.sinceLastSuccess")
registry.age_gauge_with_id(last_success).now()
```

