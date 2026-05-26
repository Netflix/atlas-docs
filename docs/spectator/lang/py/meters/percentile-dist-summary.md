# Percentile Distribution Summary

See [Percentile Distribution Summary](../../../patterns/percentile-dist-summary.md) for the concept.

Call `record()` with a value:

```python
from spectator import Registry

registry = Registry()
registry.pct_distribution_summary("server.requestSize").record(10)

request_size = registry.new_id("server.requestSize")
registry.pct_distribution_summary_with_id(request_size).record(10)
```
