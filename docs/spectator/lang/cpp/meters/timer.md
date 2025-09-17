## Timer

A Timer is used to measure how long (in seconds) some event is taking.

Call `Record()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Timer
    auto serverLatency = r.CreateTimer("server.requestLatency");
    serverLatency.Record(10);

    // Option 2: Create a Timer from a MeterID
    auto requestLatencyMeter = r.CreateNewId("server.requestLatency");
    r.CreateTimer(requestLatencyMeter).Record(10);
}
```

## Units

Ensure that you always report values in seconds (see [Use Base Units]). The API does not offer any
guarantees that the value will be in seconds.

[Use Base Units]: ../../../../concepts/naming.md#use-base-units
