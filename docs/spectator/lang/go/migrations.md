## Migrating from 0.X to 2.X

Version 2.X consists of a major rewrite that turns spectator-go into a thin client designed to send metrics through
[spectatord](https://github.com/Netflix-Skunkworks/spectatord). As a result some functionality has been moved to other
packages or removed.

### New

#### Writers

`spectator.Registry` now supports different writers. The default writer is `writer.UdpWriter` which sends metrics
to [spectatord](https://github.com/Netflix-Skunkworks/spectatord) through UDP.

Writers can be configured through `spectator.Config.Location`.

Possible values are:

- `none`: Configures a no-op writer that does nothing. Can be used to disable metrics collection.
- `stdout`: Writes metrics to stdout.
- `stderr`: Writes metrics to stderr.
- `memory`: Writes metrics to memory. Useful for testing.
- `file:///path/to/file`: Writes metrics to a file.
- `unix:///path/to/socket`: Writes metrics to a Unix domain socket.
- `udp://host:port`: Writes metrics to a UDP socket.

Location can also be set through the environment variable `SPECTATOR_OUTPUT_LOCATION`. If both are set, the environment
variable takes precedence over the passed config. 

The environment variable `SPECTATOR_OUTPUT_LOCATION` can be set to `none` to disable metrics collection.

#### Meters

The following new Meters have been added:

- `meter.MaxGauge`
- `meter.Gauge` with TTL

#### Common Tags

Common tags are now automatically added to all Meters. Their values are read from the environment variables.

| Tag          | Environment Variable |
|--------------|----------------------|
| nf.container | TITUS_CONTAINER_NAME |
| nf.process   | NETFLIX_PROCESS_NAME |

Tags from environment variables take precedence over tags passed on code when creating the `Config`.

Note that common tags sourced by [spectatord](https://github.com/Netflix-Skunkworks/spectatord) can't be overwritten.

#### Config

- `Config` is now created through a constructor which throws error if the passed in parameters are not valid.
- `Config` members are now private.

### Moved

- Runtime metrics collection has been moved
  to [spectator-go-runtime-metrics](https://github.com/Netflix/spectator-go-runtime-metrics). Follow instructions in
  the [README](https://github.com/Netflix/spectator-go-runtime-metrics) to enable collection.
- Some types have been moved to different packages. For example, `spectator.Counter` is now in `meter.Counter`.

### Removed

- `spectator.HttpClient` has been removed. Use the standard `http.Client` instead.
- `spectator.Meter`s no longer has a `Measure() []Measurement` function. Meters are now stateless and do not store
  measurements.
- `spectator.Clock` has been removed. Use the standard `time` package instead.
- `spectator.Config` has been greatly simplified.
- `spectator.Registry` no longer has a `Start()` function. The `Registry` is now effectively stateless and there is
  nothing to start other than opening the output location.
- `spectator.Registry` no longer has a `Stop()` function. Instead, use `Close()` to close the registry. Once the
  registry is closed, it can't be started again.
- `spectator.Config.IpcTimerRecord` has been removed. Use a `meter.Timer` instead to record Ipc metrics.
- `spectator.MeterFactoryFun` has been removed. If you need to create a custom meter you can do so by wrapping one of
  the meters returned by `spectator.Registry`.
- `spectator.Registry` no longer reports `spectator.measurements` metrics. Instead, you can use spectatord metrics to
  troubleshoot.
- `spectator.Registry` no longer keep track of the Meters it creates. This means that you can't get a list of all Meters
  from the Registry. If you need to keep track of Meters, you can do so in your application code.
- `Percentile*` meters no longer support defining min/max values.
- `spectator.Registry` no longer allows setting a different logger after creation. A custom logger can be set in the
  `spectator.Config` before creating the Registry.
- File-based configuration is no longer supported.

### Migration Steps

1. Make sure you're not relying on any of the [removed functionality](#removed).
2. Update imports to use `meters` package instead of `spectator` for Meters.
3. If you want to collect runtime metrics
   pull [spectator-go-runtime-metrics](https://github.com/Netflix/spectator-go-runtime-metrics) and follow the
   instructions in the [README](https://github.com/Netflix/spectator-go-runtime-metrics).
4. If you use `PercentileDistributionSummary` or `PercentileTimer`, then  you need to update your code to use the
   respective functions provided by the `Registry` to initialize these meters.
5. Remove dependency on Spectator Go Internal configuration library. Such dependency is no longer required.
6. There is no longer an option to start or stop the registry at runtime. If you need to configure a `Registry` that
   doesn't emit metrics, for testing purposes, you can use the `spectator.Config.Location` option with `none` to
   configure a no-op writer.

### Writing Tests

To write tests against this library, instantiate a test instance of the `Registry` and configure it to use the
[MemoryWriter](https://github.com/Netflix/spectator-go/blob/main/spectator/writer/writer.go#L18-L21), which stores
all updates in an `Array`. Maintain a handle to the `MemoryWriter`, then inspect the `Lines()` to verify your metrics
updates. See the source code for more testing examples.

```golang
package app

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
