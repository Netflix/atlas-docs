# Max Gauge

See [Max Gauge](../../../core/meters/max-gauge.md) for the concept.

Call `Set()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Max Gauge
    auto serverQueueSize = r.CreateMaxGauge("server.queueSize");
    serverQueueSize.Set(10);

    // Option 2: Create a Gauge from a MeterID
    auto serverQueueMeter = r.CreateNewId("server.queueSize");
    r.CreateMaxGauge(serverQueueMeter).Set(10);
}
```
