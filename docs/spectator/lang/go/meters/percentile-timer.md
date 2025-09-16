## Percentile Timer

The value is the number of seconds that have elapsed for an event, with percentile estimates.

This metric type will track the data distribution by maintaining a set of Counters. The
distribution can then be used on the server side to estimate percentiles, while still
allowing for arbitrary slicing and dicing based on dimensions.

In order to maintain the data distribution, they have a higher storage cost, with a worst-case of
up to 300X that of a standard Timer. Be diligent about any additional dimensions added to Percentile
Timers and ensure that they have a small bounded cardinality.

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
