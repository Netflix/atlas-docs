The value is the number of seconds that have elapsed for an event, with percentile estimates.

This metric type will track the data distribution by maintaining a set of Counters. The
distribution can then be used on the server side to estimate percentiles, while still
allowing for arbitrary slicing and dicing based on dimensions.

In order to maintain the data distribution, they have a higher storage cost, with a worst-case of
up to 300X that of a standard Timer. Be diligent about any additional dimensions added to Percentile
Timers and ensure that they have a small bounded cardinality.

Call `Record()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto r = Registry(config);

    // Option 1: Directly create a Percentile Timer
    auto serverLatency = r.pct_timer("server.requestLatency");
    serverLatency.Record(10);

    // Option 2: Create a Percentile Timer from a MeterID
    auto requestLatencyMeter = r.new_id("server.requestLatency");
    r.pct_timer_with_id(requestLatencyMeter).Record(10);
}
```