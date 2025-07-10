The value is a number that is sampled at a point in time, but it is reported as a maximum Gauge
value to the backend. This ensures that only the maximum value observed during a reporting interval
is sent to the backend, thus over-riding the last-write-wins semantics of standard Gauges. Unlike
standard Gauges, Max Gauges do not continue to report to the backend, and there is no TTL.

Call `Set()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto r = Registry(config);

    // Option 1: Directly create a Max Gauge
    auto serverQueueSize = r.max_gauge("server.queueSize");
    serverQueueSize.Set(10);

    // Option 2: Create a Gauge from a MeterID
    auto serverQueueMeter = r.new_id("server.queueSize");
    r.max_gauge_with_id(serverQueueMeter).Set(10);
}
```
