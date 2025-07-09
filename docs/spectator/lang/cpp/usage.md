# spectator-cpp Usage

CPP thin-client [metrics library] for use with [Atlas] and [SpectatorD].

[metrics library]: https://github.com/Netflix/spectator-cpp
[Atlas]: ../../../overview.md
[SpectatorD]: ../../agent/usage.md

## Supported CPP Versions

This library currently utilzes C++ 20.

## Installing & Building

If your project utilizes CMake you can incorporate this project by simply calling add_subdirectory(spectator-cpp).
If you wish to simply build the Spectator-CPP thin client you can utilize the Docker containter instructions found 
here https://github.com/Netflix/spectator-cpp/tree/main/Dockerfiles. The container installs a minimal set of depencies 
to build the project in the container, such as g++-13, python3, and conan. The project only has 3 external dependencies 
spdlog, gtest and boost. These dependencies are managed through conan.

## Instrumenting Code

```cpp
#include <registry.h>

int main()
{
    // Create common tags to be applied to all metrics sent to Atlas
    std::unordered_map<std::string, std::string> commonTags{{"platform", "my-platform"}, {"process", "my-process"}};

    // Create a config which defines the way you send metrics to SpectatorD
    auto config = Config(WriterConfig(WriterTypes::Memory), commonTags);
    
    // Initialize the Registry with the Config (Always required before sending metrics)
    auto r = Registry(config);

    // Create some meters
    auto threadGauge = r.gauge("threads");
    auto queueGauge = r.gauge("queue-size", {{"my-tags", "bar"}});

    auto memoryWriter = static_cast<MemoryWriter*>(WriterTestHelper::GetImpl());
    EXPECT_TRUE(memoryWriter->IsEmpty());

    threadGauge.Set(GetNumThreads()); // Metric sent to SpectatorD: "g:threads,platform=my-platform,process=my-process:5.000000\n"
    queueGauge.Set(GetQueueSize()); // Metric sent to SpectatorD: "g:queue-size,my-tags=bar,platform=my-platform,process=my-process:10.000000\n"
}
```

## Logging

Logging is implemented with spdlog and the default location is standard output. The default log level is spdlog::level::info. The Logger class is a singleton
and provides a function Logger::GetLogger(). You can change the logger level by simply calling Logger::GetLogger()->set_level(spdlog::level::debug); as long as
the logger has been created successfully

## Runtime Metrics

Coming Soon


## Working with MeterId Objects

Each metric stored in Atlas is uniquely identified by the combination of the name and the tags
associated with it. In `spectator-cpp`, this data is represented with `Id` objects, created
by the `Registry`. The `NewId()` method returns new `Id` objects, which have extra common
tags applied, and which can be further customized by calling the `WithTag()` and `WithTags()`
methods. Each `Id` will create and store a validated subset of the `spectatord` protocol line
to be written for each `Meter`, when it is instantiated. `Id` objects can be passed around and
used concurrently. Manipulating the tags with the provided methods will create new `Id` objects.

Note that **all tag keys and values must be strings.** For example, if you want to keep track of the
number of successful requests, then you must cast integers to strings. The `Id` class will
validate these values, dropping or changing any that are not valid, and reporting a warning log.

```cpp
#include <registry.h>

int main()
{
    std::unordered_map<std::string, std::string> commonTags{{"platform", "my-platform"}, {"process", "my-process"}};

    auto config = Config(WriterConfig(WriterTypes::Memory), commonTags);
    auto registry = Registry(config);

    registry.counter("server.requests", {{"statusCode", std::to_string(200)}}).Increment();

    // Option 1: Using the registry to create a MeterId
    auto numRequestsId = registry.new_id("server.numRequests", {{"statusCode", std::to_string(200)}});
    // Creating the counter with the MeterId and Incrementing it
    registry.counter_with_id(numRequestsId).Increment();

    // Option 2: Directly creating a Counter
    auto numRequestsCounter = registry.counter("server.numRequests", {{"statusCode", std::to_string(200)}});
    numRequestsCounter.Increment();
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

`spectator.Registry` now supports three different writers. The writer types are Memory Writer, UDP Writer,
and a UDS (Unix Domain Socket) Writer

Possible values are:

* `""`     - Empty string will default to `udp`, with the `LineBuffer` disabled by default.
* `none`   - A no-op writer that does nothing. Used to disable metrics collection.
* `memory` - Write to memory. Useful for testing.
* `stderr` - Write to standard error for the process.
* `stdout` - Write to standard output for the process.
* `udp`    - Write to the default UDP port for `spectatord`. This is the default location.
* `unix`   - Write to the default Unix Domain Socket for `spectatord`. Useful for high-volume scenarios.
* `file:///path/to/file`   - Write to a custom file (e.g. `file:///tmp/foo/bar`).
* `udp://host:port`        - Write to a custom UDP socket (e.g. `udp://127.0.0.1:1235`).
* `unix:///path/to/socket` - Write to a custom Unix domain socket (e.g. `unix:///tmp/some.socket`).

Location can also be set through the environment variable `SPECTATOR_OUTPUT_LOCATION`. If both are set,
the environment variable takes precedence over the passed config. If either values provided to the WriterConfig are
invalid a runtime exception will be thrown.

## Line Buffer

The `NewConfigWithBuffer` factory function takes a `bufferSize` parameter that configures an optional
`LineBuffer`, which caches protocol lines locally, before flushing them to `spectatord`. Flushes occur
under two conditions: (1) the buffer size is exceeded, or (2) five seconds has elapsed. The buffer is
available for the `UdpWriter` and the `UnixgramWriter`, where performance matters most. The `LineBuffer`
is disabled by default (with size zero) in the standard `NewConfig` factory function, to ensure that the
default operation of the library works under most circumstances. For high-performance scenarios, a 60KB
buffer size is recommended. The maximum buffer size for udp sockets and unix domain sockets on Linux is
64KB, so stay under this limit.

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
  "github.com/Netflix/spectator-go/v2/spectator"
  "github.com/Netflix/spectator-go/v2/spectator/writer"
  "testing"
  "time"
)

func TestRegistryWithMemoryWriter_Counter(t *testing.T) {
  config, _ := spectator.NewConfig("memory", nil, nil)
  registry, _ = spectator.NewRegistry(config)
  mw := registry.GetWriter().(*writer.MemoryWriter)

  counter := registry.Counter("test_counter", nil)
  counter.Increment()

  expected := "c:test_counter:1"
  if len(mw.Lines()) != 1 || mw.Lines()[0] != expected {
    t.Errorf("Expected '%s', got '%s'", expected, mw.Lines()[0])
  }
}
```

### Protocol Parser

A [SpectatorD] line protocol parser is available, which can be used for validating the results
captured by a `MemoryWriter`.

```golang
import (
  "github.com/Netflix/spectator-go/v2/spectator"
  "testing"
)

func TestParseProtocolLineWithValidInput(t *testing.T) {
  line := "c:name,tag1=value1,tag2=value2:50"
  meterType, meterId, value, err := spectator.ParseProtocolLine(line)

  if err != nil {
    t.Errorf("Unexpected error: %v", err)
  }

  if meterType != "c" {
    t.Errorf("Unexpected meter type: %v", meterType)
  }

  if meterId.Name() != "name" || meterId.Tags()["tag1"] != "value1" || meterId.Tags()["tag2"] != "value2" {
    t.Errorf("Unexpected meter id: %v", meterId)
  }

  if value != "50" {
    t.Errorf("Unexpected value: %v", value)
  }
}
```

[SpectatorD]: ../../agent/usage.md

## Performance

On an `m5d.2xlarge` EC2 instance, with `Go 1.24.3` and `github.com/Netflix/spectator-go/v2 v2.0.13`, we
have observed the following single-threaded performance numbers across a two-minute test window:

* 135,771 requests/second over `udp`
* 206,641 requests/second over `unix`

The benchmark incremented a single counter with two tags in a tight loop, to simulate real-world tag
usage, and the rate-per-second observed on the corresponding Atlas graph matched. The protocol line
was `74` characters in length.

The Go process CPU usage was ~112% and the `spectatord` process CPU usage was ~62% on this 8 vCPU
system, for `udp`. It was ~113% and ~85%, respectively, for `unix`.
