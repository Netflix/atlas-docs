# Distribution Summary

See [Distribution Summary](../../../core/meters/dist-summary.md) for the concept.

Call `Record()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Distribution Summary
    auto serverRequestSize = r.CreateDistributionSummary("server.requestSize");
    serverRequestSize.Record(42);

    // Option 2: Create a Distribution Summary from a MeterID
    auto serverRequestMeter = r.CreateNewId("server.requestSize");
    r.CreateDistributionSummary(serverRequestMeter).Record(42);
}
```