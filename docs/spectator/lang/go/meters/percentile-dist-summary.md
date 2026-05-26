# Percentile Distribution Summary

See [Percentile Distribution Summary](../../../patterns/percentile-dist-summary.md) for the concept.

Call `Record()` with a value:

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.PercentileDistributionSummary("server.requestSize", nil).Record(10)

	requestSize := registry.NewId("server.requestSize", nil)
	registry.PercentileDistributionSummaryWothId(requestSize).Record(10)
}
```
