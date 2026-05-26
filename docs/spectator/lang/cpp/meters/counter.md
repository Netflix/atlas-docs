# Counter

See [Counter](../../../core/meters/counter.md) for the concept.

Call `Increment()` when an event occurs:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Counter
    auto serverRequestCounter = r.CreateCounter("server.numRequests");
    serverRequestCounter.Increment();

    // Option 2: Create a Counter from a MeterID
    auto serverRequestMeter = r.CreateNewId("server.numRequests");
    r.CreateCounter(serverRequestMeter).Increment();
}
```

You can also pass a value to `Increment()`. This is useful when a collection of events happens
together:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Counter
    auto serverRequestCounter = r.CreateCounter("server.numRequests");
    serverRequestCounter.Increment(10);

    // Option 2: Create a Counter from a MeterID
    auto serverRequestMeter = r.CreateNewId("server.numRequests");
    r.CreateCounter(serverRequestMeter).Increment(10);
}
```