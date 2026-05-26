# Monotonic Counter (uint64)

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept (uint64 variant).

Call `Set()` when an event occurs:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create a Monotonic Counter uint64_t
    auto interfaceBytes = r.CreateMonotonicCounterUint("iface.bytes");
    interfaceBytes.Set(10);

    // Option 2: Create a Monotonic Counter uint64_t from a MeterID
    auto interfaceBytesMeter = r.CreateNewId("iface.bytes");
    r.CreateMonotonicCounterUint(interfaceBytesMeter).Set(10);
}
```
