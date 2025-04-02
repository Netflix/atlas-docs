A Monotonic Counter (float) is used to measure the rate at which an event is occurring, when the
source data is a monotonically increasing number. A minimum of two samples must be sent, in order to
calculate a delta value and report it to the backend as a rate-per-second. A variety of networking
metrics may be reported monotonically, and this metric type provides a convenient means of recording
these values, at the expense of a slower time-to-first metric.

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
