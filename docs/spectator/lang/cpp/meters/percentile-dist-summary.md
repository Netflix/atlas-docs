The value tracks the distribution of events, with percentile estimates. It is similar to a
`PercentileTimer`, but more general, because the size does not have to be a period of time.

For example, it can be used to measure the payload sizes of requests hitting a server or the
number of records returned from a query. Note that the C++ implementation of Percentile Distribution
Summary allows for the recording of floating point values, which the other thin clients do not
allow.

In order to maintain the data distribution, they have a higher storage cost, with a worst-case of
up to 300X that of a standard Distribution Summary. Be diligent about any additional dimensions
added to Percentile Distribution Summaries and ensure that they have a small bounded cardinality.

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
