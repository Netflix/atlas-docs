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

Logging is implemented with the standard Golang [slog package](https://pkg.go.dev/log/slog). The logger defines interfaces
for [Debugf, Infof, and Errorf]. There are useful messages implemented at the Debug level which can
help diagnose the metric publishing workflow. The logger can be overridden by providing one as the
third parameter of the `Config` constructor.

[Debugf, Infof, and Errorf]: https://github.com/Netflix/spectator-go/blob/main/spectator/logger/logger.go

## Runtime Metrics

Use [spectator-go-runtime-metrics](https://github.com/Netflix/spectator-go-runtime-metrics). Follow instructions
in the [README](https://github.com/Netflix/spectator-go-runtime-metrics) to enable collection.
