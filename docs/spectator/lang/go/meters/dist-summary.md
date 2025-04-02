A Distribution Summary is used to track the distribution of events. It is similar to a Timer, but
more general, in that the size does not have to be a period of time. For example, a Distribution
Summary could be used to measure the payload sizes of requests hitting a server.

Always use base units when recording data, to ensure that the tick labels presented on Atlas graphs
are readable. If you are measuring payload size, then use bytes, not kilobytes (or some other unit).
This means that a `4K` tick label will represent 4 kilobytes, rather than 4 kilo-kilobytes.

Call `Record()` with a value:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.DistributionSummary("server.requestSize", nil).Record(10)

	requestSize := registry.NewId("server.requestSize", nil)
	registry.DistributionSummaryWothId(requestSize).Record(10)
}
```
