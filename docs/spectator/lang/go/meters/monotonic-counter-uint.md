# Monotonic Counter (uint64)

See [Monotonic Counter](../../../patterns/monotonic-counter.md) for the concept (uint64 variant).

Call `Set()` when an event occurs:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.MonotonicCounterUint("iface.bytes", nil).Set(1)

	ifaceBytes := registry.NewId("iface.bytes", nil)
	registry.MonotonicCounterUintWithId(ifaceBytes).Set(1)
}
```
