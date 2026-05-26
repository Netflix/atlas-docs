# Age Gauge

See [Age Gauge](../../../patterns/age-gauge.md) for the concept.

To set a specific time as the last success:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create an Age Gauge
    auto successAgeGauge = r.CreateAgeGauge("time.sinceLastSuccess");
    successAgeGauge.Set(1611081000);

    // Option 2: Create an Age Gauge from a MeterID
    auto successMeter = r.CreateNewId("time.sinceLastSuccess");
    r.CreateAgeGauge(successMeter).Set(1611081000);
}
```

To set `Now()` as the last success:

```cpp
#include <registry.h>

int main()
{
    auto config = Config(WriterConfig(WriterTypes::UDP));
    auto r = Registry(config);

    // Option 1: Directly create an Age Gauge
    auto successAgeGauge = r.CreateAgeGauge("time.sinceLastSuccess");
    successAgeGauge.Now();

    // Option 2: Create an Age Gauge from a MeterID
    auto successMeter = r.CreateNewId("time.sinceLastSuccess");
    r.CreateAgeGauge(successMeter).Now();
}
```

