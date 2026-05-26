# Percentile Distribution Summary

See [Percentile Distribution Summary](../../../patterns/percentile-dist-summary.md) for the concept.

Call `Record()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Percentile Distribution Summary
    auto serverSize = r.CreatePercentDistributionSummary("server.requestSize");
    serverSize.Record(10);

    // Option 2: Create a Percentile Distribution Summary from a MeterID
    auto requestSizeMeter = r.CreateNewId("server.requestSize");
    r.CreatePercentDistributionSummary(requestSizeMeter).Record(10);
}
```
