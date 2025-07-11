A Monotonic Counter (uint64) is used to measure the rate at which an event is occurring, when the
source data is a monotonically increasing number. A minimum of two samples must be sent, in order to
calculate a delta value and report it to the backend as a rate-per-second. A variety of networking
metrics may be reported monotonically, and this metric type provides a convenient means of recording
these values, at the expense of a slower time-to-first metric.

Call `Set()` when an event occurs:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto r = Registry(config);

    // Option 1: Directly create a Monotonic Counter uint64_t
    auto interfaceBytes = r.CreateMonotonicCounterUint("iface.bytes");
    interfaceBytes.Set(10);

    // Option 2: Create a Monotonic Counter uint64_t from a MeterID
    auto interfaceBytesMeter = r.CreateNewId("iface.bytes");
    r.CreateMonotonicCounterUint(interfaceBytesMeter).Set(10);
}
```
