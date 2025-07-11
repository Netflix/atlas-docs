# spectator-cpp Usage

CPP thin-client [metrics library] for use with [Atlas] and [SpectatorD].

[metrics library]: https://github.com/Netflix/spectator-cpp
[Atlas]: ../../../overview.md
[SpectatorD]: ../../agent/usage.md

## Supported CPP Versions

This library currently utilzes C++ 20.

## Installing & Building

If your project utilizes CMake you can incorporate this project by simply calling CMake's add_subdirectory() command on the root folder of the project.
If you wish to simply build the Spectator-CPP thin client you can utilize the Docker containter instructions found 
here https://github.com/Netflix/spectator-cpp/tree/main/Dockerfiles. The container installs a minimal set of depencies 
to build the project in the container, such as g++-13, python3, and conan. The project only has 3 external dependencies 
spdlog, gtest and boost. These dependencies are managed through conan.

## Instrumenting Code

{% raw %}

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
    auto threadGauge = r.CreateGauge("threads");
    auto queueGauge = r.CreateGauge("queue-size", {{"my-tags", "bar"}});

    auto memoryWriter = static_cast<MemoryWriter*>(WriterTestHelper::GetImpl());
    EXPECT_TRUE(memoryWriter->IsEmpty());

    threadGauge.Set(GetNumThreads()); // Metric sent to SpectatorD: "g:threads,platform=my-platform,process=my-process:5.000000\n"
    queueGauge.Set(GetQueueSize());   // Metric sent to SpectatorD: "g:queue-size,my-tags=bar,platform=my-platform,process=my-process:10.000000\n"
}
```

{% endraw %}

## Logging

Logging is implemented with spdlog and the default location is standard output. The default log level is spdlog::level::info. The Logger class is a singleton
and provides a function Logger::GetLogger(). You can change the logger level by simply calling Logger::GetLogger()->set_level(spdlog::level::debug); as long as
the logger has been created successfully

## Runtime Metrics

Coming Soon


## Working with MeterId Objects

Each metric stored in Atlas is uniquely identified by the combination of the name and the tags
associated with it. In `spectator-cpp`, this data is represented with `MeterId` objects, created
by the `Registry`. The `CreateNewId()` method returns new a `MeterId` object, which have extra common
tags applied, and which can be further customized by calling the `WithTag()` and `WithTags()`
methods. Each `MeterId` will create and store a validated subset of the `spectatord` protocol line
to be written for each `Meter`, when it is instantiated. Manipulating the tags with the provided methods
 will create new `MeterId` objects.

Note that **all tag keys and values must be strings.** For example, if you want to keep track of the
number of successful requests, then you must cast integers to strings. The `Id` class will
validate these values, dropping or changing any that are not valid, and reporting a warning log.

{% raw %}

```cpp
#include <registry.h>

int main()
{
    // Create common tags
    std::unordered_map<std::string, std::string> commonTags{{"platform", "my-platform"}, {"process", "my-process"}};

    // Initialize the Registry
    auto config = Config(WriterConfig(WriterTypes::Memory), commonTags);
    auto registry = Registry(config);


    // Option 1: Using the registry to create a MeterId & creating a Counter from the MeterId
    auto numRequestsId = registry.CreateNewId("server.numRequests", {{"statusCode", std::to_string(200)}});
    registry.CreateCounter(numRequestsId).Increment();

    // Option 2: Directly creating a Counter
    auto numRequestsCounter = registry.CreateCounter("server.numRequests2", {{"statusCode", std::to_string(200)}});
    numRequestsCounter.Increment();

}
```

{% endraw %}

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
and a UDS (Unix Domain Socket) Writer. In order to define the writer type you must initialize the Registry 
with a Config object. A Config Object takes a required WriterConfig object and optional extra tags. A WriterConfig object
takes a location and an optional buffering parameter. Buffering is allowed for all writer types.

```cpp
// Writer Config Constructors

// Option 1: Define a location and no buffering
WriterConfig(const std::string& type)

// Option 2: Define a location with buffering
WriterConfig(const std::string& type, unsigned int bufferSize);


// Config Constructor
// Required WriterConfig with optional extraTags to be applied to all metrics
Config(const WriterConfig& writerConfig, const std::unordered_map<std::string, std::string>& extraTags = {});
```

{% raw %}

```cpp
// Default Writer Config Examples
WriterConfig wConfig(WriterTypes::Memory); // write metrics to memory for testing
WriterConfig wConfig(WriterTypes::UDP); // the default UDP address for `spectatord`.
WriterConfig wConfig(WriterTypes::Unix, 4096); // the default unix address for spectatord with buffering

// Custom Writer Config Location Examples
const std::string udpUrl = std::string(WriterTypes::UDPURL) + "192.168.1.100:8125";
const WriterConfig wConfig(udpUrl);

const std::string unixUrl = std::string(WriterTypes::UnixURL) + "/var/run/custom/socket.sock";
const WriterConfig wConfig(unixUrl, 4096);

// Config Examples
Config config = Config(WriterConfig(WriterTypes::Memory));

std::unordered_map<std::string, std::string> commonTags{{"platform", "my-platform"}, {"process", "my-process"}};
Config config = Config(WriterConfig(WriterTypes::Memory), commonTags);

// Registry Initialization
WriterConfig wConfig(WriterTypes::Memory); // write metrics to memory for testing
Config config = Config(wConfig);
Registry registry(config);
```
{% endraw %}

Location can also be set through the environment variable `SPECTATOR_OUTPUT_LOCATION`. If both are set,
the environment variable takes precedence over the value passed to the WriterConfig. If either values provided to the WriterConfig are
invalid a runtime exception will be thrown.

## Line Buffer

The WriterConfig has an optional to set a default `bufferSize` parameter. If this parameter is not set each time 
a meter is recorded, that meter will send the metric to spectatord using the writer type defined in your WriterConfig.
If the meter is set the buffer will cache protocol lines locally before flushing them to `spectatord`. Flushes occur only 
under one condition that the buffer size has been exceeded.or high-performance scenarios, a 60KB
buffer size is recommended. The maximum buffer size for udp sockets and unix domain sockets on Linux is
64KB, so stay under this limit.


## Batch Usage

When using `spectator-cpp` to report metrics from a batch job, ensure that the batch job runs for at
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
which stores all updates in an `Vector`. Maintain a handle to the `MemoryWriter`, then inspect the
`Lines()` to verify your metrics updates. See the source code for more testing examples.

{% raw %}

```cpp
int main()
{
    // Initialize Registry
    auto config = Config(WriterConfig(WriterTypes::Memory));
    auto registry = Registry(config);

    // Directly create a Counter
    auto numRequestsCounter = registry.CreateCounter("server.numRequests2", {{"statusCode", std::to_string(200)}});

    // Create a handle to the Writer
    auto memoryWriter = static_cast<MemoryWriter*>(WriterTestHelper::GetImpl());


    numRequestsCounter.Increment();

    auto messages = memoryWriter->GetMessages();
    for (const auto& message : messages)
    {
        std::cout << message; // Print all messages sent to SpectatorD
    }
}
```
{% endraw %}

## Performance

On an `m5d.2xlarge` EC2 instance, with `spectator-cpp-2.0` and `github.com/Netflix/spectator-cpp/v2 v2.0.13`, we
have observed the following single-threaded performance numbers across a two-minute test window:

*  requests/second over `udp`
*  requests/second over `unix`

The benchmark incremented a single counter with two tags in a tight loop, to simulate real-world tag
usage, and the rate-per-second observed on the corresponding Atlas graph matched. The protocol line
was `74` characters in length.

The Go process CPU usage was ~112% and the `spectatord` process CPU usage was ~62% on this 8 vCPU
system, for `udp`. It was ~113% and ~85%, respectively, for `unix`.
