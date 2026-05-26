# Max Gauge

A Max Gauge is a value sampled at a point in time, but reported to the backend as the
**maximum** value observed during the reporting interval rather than the last-write-wins
behavior of a standard [Gauge](gauge.md).

This is useful when you want to make sure spikes are visible rather than missed between
samples. For example, when tracking a queue depth that fluctuates rapidly within a
reporting interval, a Max Gauge ensures the peak is preserved.

Unlike a standard Gauge, Max Gauges do **not** continue to report after the last update
and do not have a TTL. Once the reporting interval ends, the max is flushed and the next
interval starts fresh.

## Languages

### First-Class Support

* [C++](../../lang/cpp/meters/max-gauge.md)
* [Go](../../lang/go/meters/max-gauge.md)
* [Java](../../lang/java/meters/max-gauge.md)
* [Node.js](../../lang/nodejs/meters/max-gauge.md)
* [Python](../../lang/py/meters/max-gauge.md)
