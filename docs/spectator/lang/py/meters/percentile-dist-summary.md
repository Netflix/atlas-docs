The value tracks the distribution of events, with percentile estimates. It is similar to a
`PercentileTimer`, but more general, because the size does not have to be a period of time.

For example, it can be used to measure the payload sizes of requests hitting a server or the
number of records returned from a query.

In order to maintain the data distribution, they have a higher storage cost, with a worst-case of
up to 300X that of a standard Distribution Summary. Be diligent about any additional dimensions
added to Percentile Distribution Summaries and ensure that they have a small bounded cardinality.

Call `record()` with a value:

```python
from spectator import Registry

registry = Registry()
registry.pct_distribution_summary("server.requestSize").record(10)

request_size = registry.new_id("server.requestSize")
registry.pct_distribution_summary_with_id(request_size).record(10)
```
