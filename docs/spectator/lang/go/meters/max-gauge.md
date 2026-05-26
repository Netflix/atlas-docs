# Max Gauge

See [Max Gauge](../../../core/meters/max-gauge.md) for the concept.

Call `Set()` with a value:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.MaxGauge("server.queueSize", nil).Set(10)

	queueSize := registry.NewId("server.queueSize", nil)
	registry.MaxGaugeWithId(queueSize).Set(10)
}
```
