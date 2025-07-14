A Distribution Summary is used to track the distribution of events. It is similar to a Timer, but
more general, in that the size does not have to be a period of time. For example, a Distribution
Summary could be used to measure the payload sizes of requests hitting a server. Note that the C++
implementation of Distribution Summary allows for the recording of floating point values, which the
other thin clients do not allow.

Always use base units when recording data, to ensure that the tick labels presented on Atlas graphs
are readable. If you are measuring payload size, then use bytes, not kilobytes (or some other unit).
This means that a `4K` tick label will represent 4 kilobytes, rather than 4 kilo-kilobytes.

Call `Record()` with a value:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto r = Registry(config);

    // Option 1: Directly create a Distribution Summary
    auto serverRequestSize = r.CreateDistributionSummary("server.requestSize");
    serverRequestSize.Record(42);

    // Option 2: Create a Distribution Summary from a MeterID
    auto serverRequestMeter = r.CreateNewId("server.requestSize");
    r.CreateDistributionSummary(serverRequestMeter).Record(42);
}
```
