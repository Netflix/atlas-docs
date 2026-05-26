# Monotonic Counter

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept.

Call `Set()` when an event occurs:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.MonotonicCounter("iface.bytes", nil).Set(10)

	ifaceBytes := registry.NewId("iface.bytes", nil)
	registry.MonotonicCounterWithId(ifaceBytes).Set(10)
}
```
