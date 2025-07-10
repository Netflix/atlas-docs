A Timer is used to measure how long (in seconds) some event is taking.

Call `Record()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto r = Registry(config);

    // Option 1: Directly create a Timer
    auto serverLatency = r.timer("server.requestLatency");
    serverLatency.Record(10);

    // Option 2: Create a Timer from a MeterID
    auto requestLatencyMeter = r.new_id("server.requestLatency");
    r.timer_with_id(requestLatencyMeter).Record(10);
}
```
