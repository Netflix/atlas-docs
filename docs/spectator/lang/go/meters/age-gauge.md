# Age Gauge

See [Age Gauge](../../../patterns/age-gauge.md) for the concept.

To `Set()` a specific time as the last success:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.AgeGauge("time.sinceLastSuccess", nil).Set(1611081000)

	lastSuccess := registry.NewId("time.sinceLastSuccess", nil)
	registry.AgeGaugeWithId(lastSuccess).set(1611081000)
}
```

To set `Now()` as the last success:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.AgeGauge("time.sinceLastSuccess", nil).Now()

	lastSuccess := registry.NewId("time.sinceLastSuccess", nil)
	registry.AgeGaugeWithId(lastSuccess).Now()
}
```

