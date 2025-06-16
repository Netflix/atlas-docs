# Performance

## Test Script

Test maximum single-threaded throughput for two minutes.

```go
package main

import (
	"fmt"
	"github.com/Netflix/spectator-go/v2/spectator"
	"time"
)

func elapsed(start time.Time) float64 {
	return time.Now().Sub(start).Seconds()
}

func main() {
	location := "udp"
	// location := "unix"
	config, _ := spectator.NewConfig(location, nil, nil)
	registry, _ := spectator.NewRegistry(config)
	defer registry.Close()
	// add tags with some length, to simulate more real-world conditions
	tags := map[string]string{"location": location, "version": "correct-horse-battery-staple"}

	maxDuration := float64(2 * 60)
	start := time.Now()

	fmt.Printf("start spectator-go %s benchmark\n", location)
	iteration := 1
	for elapsed(start) < maxDuration {
		registry.Counter("spectator-go.publish", tags).Increment()
		if iteration % 500000 == 0 {
			fmt.Printf("iterations=%v elapsed=%v\n", iteration, elapsed(start))
		}
		iteration++
	}

	fmt.Printf("iterations=%v rate/sec=%v\n", iteration, float64(iteration) / elapsed(start))
}
```

## Results

See [Usage > Performance](usage.md#performance).
