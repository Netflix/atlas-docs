# Percentile Timer

See [Percentile Timer](../../../patterns/percentile-timer.md) for the concept.

Call `Record()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Percentile Timer
    auto serverLatency = r.CreatePercentTimer("server.requestLatency");
    serverLatency.Record(10);

    // Option 2: Create a Percentile Timer from a MeterID
    auto requestLatencyMeter = r.CreateNewId("server.requestLatency");
    r.CreatePercentTimer(requestLatencyMeter).Record(10);
}
```

## Units

See [Timer Units](timer.md#units) for an explanation.
