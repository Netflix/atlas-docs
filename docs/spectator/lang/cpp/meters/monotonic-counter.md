# Monotonic Counter

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept.

Call `Set()` when an event occurs:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Monotonic Counter
    auto interfaceBytes = r.CreateMonotonicCounter("iface.bytes");
    interfaceBytes.Set(10);

    // Option 2: Create a Monotonic Counter from a MeterID
    auto interfaceBytesMeter = r.CreateNewId("iface.bytes");
    r.CreateMonotonicCounter(interfaceBytesMeter).Set(10);
}
```
