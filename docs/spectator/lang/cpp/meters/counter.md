A Counter is used to measure the rate at which an event is occurring. Considering an API endpoint,
a Counter could be used to measure the rate at which it is being accessed.

Counters are reported to the backend as a rate-per-second. In Atlas, the `:per-step` operator can
be used to convert them back into a value-per-step on a graph.

Call `Increment()` when an event occurs:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto r = Registry(config);

    // Option 1: Directly create a Counter
    auto serverRequestCounter = r.counter("server.numRequests");
    serverRequestCounter.Increment();

    // Option 2: Create a Counter from a MeterID
    auto serverRequestMeter = r.new_id("server.numRequests");
    r.counter_with_id(serverRequestMeter).Increment();
}
```

You can also pass a value to `Increment()`. This is useful when a collection of events happens
together:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto r = Registry(config);

    // Option 1: Directly create a Counter
    auto serverRequestCounter = r.counter("server.numRequests");
    serverRequestCounter.Increment(10);

    // Option 2: Create a Counter from a MeterID
    auto serverRequestMeter = r.new_id("server.numRequests");
    r.counter_with_id(serverRequestMeter).Increment(10);
}
```
