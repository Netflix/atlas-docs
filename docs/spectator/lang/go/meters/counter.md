# Counter

See [Counter](../../../core/meters/counter.md) for the concept.

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