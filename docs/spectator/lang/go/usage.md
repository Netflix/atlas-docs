# spectator-go Usage

Go thin-client [metrics library] for use with [Atlas] and [SpectatorD].

[metrics library]: https://github.com/Netflix/spectator-go
[Atlas]: ../../../overview.md
[SpectatorD]: ../../agent/usage.md

## Supported Go Versions

This library currently targets the [latest two stable versions](https://go.dev/dl/) of Go.

There is one language feature used in the project which requires at least 1.21 - the
[log/slog structured logging library](https://go.dev/blog/slog).

## Instrumenting Code

```go
package main

import (
	"github.com/Netflix/spectator-go/v2/spectator"
	"github.com/Netflix/spectator-go/v2/spectator/meter"
	"strconv"
	"time"
)

type Server struct {
	registry       spectator.Registry
	requestCountId *meter.Id
	requestLatency *meter.Timer
	responseSizes  *meter.DistributionSummary
}

type Request struct {
	country string
}

type Response struct {
	status int
	size   int64
}

func (s *Server) Handle(request *Request) (res *Response) {
	start := time.Now()

	// initialize response
	res = &Response{200, 64}

	// Update the counter with dimensions based on the request.
	tags := map[string]string{
		"country": request.country,
		"status":  strconv.Itoa(res.status),
	}
	requestCounterWithTags := s.requestCountId.WithTags(tags)
	counter := s.registry.CounterWithId(requestCounterWithTags)
	counter.Increment()

	// ...
	s.requestLatency.Record(time.Since(start))
	s.responseSizes.Record(res.size)
	return
}

func newServer(registry spectator.Registry) *Server {
	return &Server{
		registry,
		registry.NewId("server.requestCount", nil),
		registry.Timer("server.requestLatency", nil),
		registry.DistributionSummary("server.responseSizes", nil),
	}
}

func getNextRequest() *Request {
	// ...
	return &Request{"US"}
}

func main() {
	commonTags := map[string]string{"nf.platform": "my_platform", "process_name": "my_process"}
	// if desired, replace the logger with a custom one, using the third parameter here:
	config, _ := spectator.NewConfig("", commonTags, nil)

	registry, _ := spectator.NewRegistry(config)
	defer registry.Close()

	server := newServer(registry)

	for i := 1; i < 3; i++ {
		// get a request
		req := getNextRequest()
		server.Handle(req)
	}
}
```

## Logging

Logging is implemented with the standard Golang [slog package](https://pkg.go.dev/log/slog). The
logger defines interfaces for [Debugf, Infof, and Errorf]. There are useful messages implemented at
the Debug level which can help diagnose the metric publishing workflow. The logger can be overridden
by providing one as the third parameter of the `Config` constructor.

[Debugf, Infof, and Errorf]: https://github.com/Netflix/spectator-go/blob/main/spectator/logger/logger.go

## Runtime Metrics

Use [spectator-go-runtime-metrics](https://github.com/Netflix/spectator-go-runtime-metrics). Follow
instructions in the [README](https://github.com/Netflix/spectator-go-runtime-metrics) to enable
collection.

## Working with MeterId Objects

Each metric stored in Atlas is uniquely identified by the combination of the name and the tags
associated with it. In `spectator-go`, this data is represented with `Id` objects, created
by the `Registry`. The `NewId()` method returns new `Id` objects, which have extra common
tags applied, and which can be further customized by calling the `WithTag()` and `WithTags()`
methods. Each `Id` will create and store a validated subset of the `spectatord` protocol line
to be written for each `Meter`, when it is instantiated. `Id` objects can be passed around and
used concurrently. Manipulating the tags with the provided methods will create new `Id` objects.

Note that **all tag keys and values must be strings.** For example, if you want to keep track of the
number of successful requests, then you must cast integers to strings. The `Id` class will
validate these values, dropping or changing any that are not valid, and reporting a warning log.

```golang
import (
	"github.com/Netflix/spectator-go/v2/spectator"
)

func main() {
	config, _ := spectator.NewConfig("udp", nil, nil)
	registry, _ := spectator.NewRegistry(config)

	registry.Counter("server.numRequests", map[string]string{"statusCode": "200"}).Increment()

	numRequests := registry.NewId("server.numRequests", map[string]string{"statusCode": "200"})
	registry.CounterWithId(numRequests).Increment()
}
```

Atlas metrics will be consumed by users many times after the data has been reported, so they should
be chosen thoughtfully, while considering how they will be used. See the [naming conventions] page
for general guidelines on metrics naming and restrictions.

[naming conventions]: ../../../concepts/naming.md

## Meter Types

* [Age Gauge](./meters/age-gauge.md)
* [Counter](./meters/counter.md)
* [Distribution Summary](./meters/dist-summary.md)
* [Gauge](./meters/gauge.md)
* [Max Gauge](./meters/max-gauge.md)
* [Monotonic Counter](./meters/monotonic-counter.md)
* [Monotonic Counter Uint](./meters/monotonic-counter-uint.md)
* [Percentile Distribution Summary](./meters/percentile-dist-summary.md)
* [Percentile Timer](./meters/percentile-timer.md)
* [Timer](./meters/timer.md)

## Output Location

`spectator.Registry` now supports different writers. The default writer is `writer.UdpWriter` which
sends metrics to [spectatord](https://github.com/Netflix-Skunkworks/spectatord) through UDP.

Writers can be configured through `spectator.Config.Location`.

Possible values are:

* `""`: Empty string will default to `udp`.
* `none`: Configures a no-op writer that does nothing. Can be used to disable metrics collection.
* `memory`: Writes metrics to memory. Useful for testing.
* `stderr`: Writes metrics to stderr.
* `stdout`: Writes metrics to stdout.
* `udp`    - Write metrics to the default spectatord UDP port. This is the default value.
* `unix`   - Write metrics to the default spectatord Unix Domain Socket. Useful for high-volume scenarios.
* `file:///path/to/file`: Writes metrics to a file.
* `unix:///path/to/socket`: Writes metrics to a Unix domain socket.
* `udp://host:port`: Writes metrics to a UDP socket.

Location can also be set through the environment variable `SPECTATOR_OUTPUT_LOCATION`. If both are set,
the environment variable takes precedence over the passed config. 

The environment variable `SPECTATOR_OUTPUT_LOCATION` can be set to `none` to disable metrics collection.

## Batch Usage

When using `spectator-go` to report metrics from a batch job, ensure that the batch job runs for at
least five (5), if not ten (10) seconds in duration. This is necessary in order to allow sufficient
time for `spectatord` to publish metrics to the Atlas backend; it publishes every five seconds. If
your job does not run this long, or you find you are missing metrics that were reported at the end
of your job run, then add a five-second sleep before exiting. This will allow time for the metrics
to be sent.

## Debug Metrics Delivery to `spectatord`

In order to see debug log messages from `spectatord`, create an `/etc/default/spectatord` file with
the following contents:

```shell
SPECTATORD_OPTIONS="--verbose"
```

This will report all metrics that are sent to the Atlas backend in the `spectatord` logs, which will
provide an opportunity to correlate metrics publishing events from your client code.

## Design Considerations - Reporting Intervals

This client is stateless, and sends a UDP packet (or unixgram) to `spectatord` each time a meter is
updated. If you are performing high-volume operations, on the order of tens-of-thousands or millions
of operations per second, then you should pre-aggregate your metrics and report them at a cadence
closer to the `spectatord` publish interval of 5 seconds. This will keep the CPU usage related to
`spectator-go` and `spectatord` low (around 1% or less), as compared to up to 40% for high-volume
scenarios.

## Writing Tests

To write tests against this library, instantiate a test instance of the `Registry` and configure it
to use the [MemoryWriter](https://github.com/Netflix/spectator-go/blob/main/spectator/writer/writer.go#L18-L21),
which stores all updates in an `Array`. Maintain a handle to the `MemoryWriter`, then inspect the
`Lines()` to verify your metrics updates. See the source code for more testing examples.

```golang
import (
	"fmt"
	"github.com/Netflix/spectator-go/v2/spectator/logger"
	"github.com/Netflix/spectator-go/v2/spectator/writer"
	"testing"
	"time"
)

func TestRegistryWithMemoryWriter_Counter(t *testing.T) {
	mw := &writer.MemoryWriter{}
	r := NewTestRegistry(mw)

	counter := r.Counter("test_counter", nil)
	counter.Increment()
	expected := "c:test_counter:1"
	if len(mw.Lines()) != 1 || mw.Lines()[0] != expected {
		t.Errorf("Expected '%s', got '%s'", expected, mw.Lines()[0])
	}
}

func NewTestRegistry(mw *writer.MemoryWriter) Registry {
	return &spectatordRegistry{
		config: &Config{},
		writer: mw,
		logger: logger.NewDefaultLogger(),
	}
}
```

### Protocol Parser

A [SpectatorD] line protocol parser is available, which can be used for validating the results
captured by a `MemoryWriter`.

```golang
import (
	"testing"
)

func TestParseProtocolLineWithValidInput(t *testing.T) {
	line := "c:meterId,tag1=value1,tag2=value2:value"
	meterType, meterId, value, err := ParseProtocolLine(line)

	if err != nil {
		t.Errorf("Unexpected error: %v", err)
	}

	if meterType != "c" {
		t.Errorf("Expected 'c', got '%s'", meterType)
	}

	if meterId.Name() != "meterId" || meterId.Tags()["tag1"] != "value1" || meterId.Tags()["tag2"] != "value2" {
		t.Errorf("Unexpected meterId: %v", meterId)
	}

	if value != "value" {
		t.Errorf("Expected 'value', got '%s'", value)
	}
}
```

[SpectatorD]: ../../agent/usage.md
