# Gauge

See [Gauge](../../../core/meters/gauge.md) for the concept.

Call `Set()` with a value:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.Gauge("server.queueSize", nil).Set(10)

	queueSize := registry.NewId("server.queueSize", nil)
	registry.GaugeWithId(queueSize).Set(10)
}
```

Gauges will report the last set value for 15 minutes. This done so that updates to the values do
not need to be collected on a tight 1-minute schedule to ensure that Atlas shows unbroken lines in
graphs. A custom TTL may be configured for gauges. SpectatorD enforces a minimum TTL of 5 seconds.

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
	"time"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.GaugeWithTTL("server.queueSize", nil, 120 * time.Second).Set(10)

	queueSize := registry.NewId("server.queueSize", nil)
	registry.GaugeWithIdWithTTL(queueSize, 120 * time.Second).Set(10)
}
```