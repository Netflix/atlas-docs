A Counter is used to measure the rate at which an event is occurring. Considering an API endpoint,
a Counter could be used to measure the rate at which it is being accessed.

Counters are reported to the backend as a rate-per-second. In Atlas, the `:per-step` operator can
be used to convert them back into a value-per-step on a graph.

Call `Increment()` when an event occurs:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.Counter("server.numRequests", nil).Increment()

	numRequests := registry.NewId("server.numRequests", nil)
	registry.CounterWithId(numRequests).Increment()
}
```

You can also pass a value to `Add(int64)`, or `AddFloat(float64)`. This is useful when a collection
of events happens together:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.Counter("queue.itemsAdded", nil).Add(10)

	numRequests := registry.NewId("server.numRequests", nil)
	registry.CounterWithId(numRequests).Add(10)
}
```
