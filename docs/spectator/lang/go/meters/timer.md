## Timer

A Timer is used to measure how long (in seconds) some event is taking.

Call `record()` with a value:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
	"time"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.Timer("server.requestLatency", nil).Record(500 * time.Millisecond)

	requestLatency := registry.NewId("server.requestLatency", nil)
	registry.TimerWithId(requestLatency).Record(500 * time.Millisecond)
}
```

## Units

Go Timers always report values to backends in seconds (see [Use Base Units]). The API accepts a
[time.Duration] value, which is converted to seconds when reporting.

[Use Base Units]: ../../../../concepts/naming.md#use-base-units
[time.Duration]: https://pkg.go.dev/time#Duration
