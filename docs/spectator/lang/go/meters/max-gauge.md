The value is a number that is sampled at a point in time, but it is reported as a maximum Gauge
value to the backend. This ensures that only the maximum value observed during a reporting interval
is sent to the backend, thus over-riding the last-write-wins semantics of standard Gauges. Unlike
standard Gauges, Max Gauges do not continue to report to the backend, and there is no TTL.

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
