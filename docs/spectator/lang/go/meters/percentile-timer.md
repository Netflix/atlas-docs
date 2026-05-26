# Percentile Timer

See [Percentile Timer](../../../patterns/percentile-timer.md) for the concept.

Call `Record()` with a value:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
	"time"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.PercentileTimer("server.requestLatency", nil).Record(500 * time.Millisecond)

	requestLatency := registry.NewId("server.requestLatency", nil)
	registry.PercentileTimerWithId(requestLatency).Record(500 * time.Millisecond)
}
```

## Units

See [Timer Units](timer.md#units) for an explanation.
