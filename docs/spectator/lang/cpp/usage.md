# spectator-cpp Usage

CPP thin-client [metrics library] for use with [Atlas] and [SpectatorD].

[metrics library]: https://github.com/Netflix/spectator-cpp
[Atlas]: ../../../overview.md
[SpectatorD]: ../../agent/usage.md

## Supported CPP Versions

This library currently utilzes C++ 20.

## Installing & Building

If your project uses CMake, you can easily integrate this library by calling `add_subdirectory()`
on the root folder. To build the Spectator-CPP thin client independently, follow the Docker
container instructions at [Dockerfiles](https://github.com/Netflix/spectator-cpp/tree/main/Dockerfiles).
The container provides a minimal build environment with g++-13, python3, and conan. Spectator-CPP
relies on just three external dependencies—spdlog, gtest, and boost—which are managed automatically
via conan.

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

    threadGauge.Set(GetNumThreads());
    queueGauge.Set(GetQueueSize());

    /* Metrics Sent: 
        "g:threads,platform=my-platform,process=my-process:5.000000\n"
        "g:queue-size,my-tags=bar,platform=my-platform,process=my-process:10.000000\n"
    */
}
```

{% endraw %}

## Logging

Logging uses the `spdlog` library and outputs to standard output by default, with a default log
level of `spdlog::level::info`. The `Logger` class is a singleton and provides the
`Logger::GetLogger()` function to access the logger instance. To change the log level, call
`Logger::GetLogger()->set_level(spdlog::level::debug);` after the logger has been successfully created.

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

## Output Locations

`spectator.Registry` supports three output writer types: Memory Writer, UDP Writer, and Unix Domain
Socket (UDS) Writer. To specify the writer type, initialize the Registry with a `Config` object. A
`Config` requires a `WriterConfig` (which defines the writer type and location) and can optionally
include extra tags to be applied to all metrics.  The `WriterConfig` also accepts an optional
buffer size parameter, enabling buffering for all writer types.

### Writer Config Constructors

```cpp
// Constructor 1: Define a location and no buffering
WriterConfig(const std::string& type)

// Constructor 2: Define a location with buffering
WriterConfig(const std::string& type, unsigned int bufferSize);
```

### Writer Config Examples

{% raw %}

```cpp
/* Default Writer Config Examples */

// Write metrics to memory for testing
WriterConfig wConfig(WriterTypes::Memory); 

// Default UDP address for spectatord
WriterConfig wConfig(WriterTypes::UDP); 

// Default UDS address for spectatord with buffering
WriterConfig wConfig(WriterTypes::Unix, 4096); 

/* Custom Writer Config Location Examples */

// Custom UDP writer location
std::string udpUrl = std::string(WriterTypes::UDPURL) + "192.168.1.100:8125";
WriterConfig wConfig(udpUrl);

// Custom UDS writer location
std::string unixUrl = std::string(WriterTypes::UnixURL) + "/var/run/custom/socket.sock";
WriterConfig wConfig(unixUrl, 4096);
```

{% endraw %}

### Config Constructor

```cpp
// Constructor: WriterConfig & optional extraTags for all metrics
Config(const WriterConfig& writerConfig, const std::unordered_map<std::string, std::string>& extraTags = {});
```

### Config Examples

{% raw %}

```cpp
/* Config Examples */

// Config with a WriterConfig & no extra tags
Config config = Config(WriterConfig(WriterTypes::Memory));

// Config with a WriterConfig & extra tags
std::unordered_map<std::string, std::string> commonTags{{"platform", "my-platform"}, {"process", "my-process"}};
Config config = Config(WriterConfig(WriterTypes::Memory), commonTags);

/* Registry Initialization */
WriterConfig wConfig(WriterTypes::Memory);
Config config = Config(wConfig);
Registry registry(config);
```

{% endraw %}

Location can also be set through the environment variable `SPECTATOR_OUTPUT_LOCATION`. If both are
set, the environment variable takes precedence over the value passed to the WriterConfig. If either
values provided to the WriterConfig are invalid a runtime exception will be thrown.

## Line Buffer

The `WriterConfig` allows you to set an optional `bufferSize` parameter. If `bufferSize` is not
set, each metric is sent immediately to `spectatord` using the configured writer type. If
`bufferSize` is set, metrics are buffered locally and only flushed to `spectatord` when the buffer
exceeds the specified size. For high-performance scenarios, a buffer size of 60KB is recommended.
The maximum buffer size for UDP and Unix Domain Socket writers on Linux is 64KB, so ensure your
buffer size does not exceed this limit.

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
to use the `MemoryWriter`, which stores all updates in a `Vector`. Maintain a handle to the
`MemoryWriter`, then inspect the protocol lines with `GetMessages()` to verify your metric updates.
See the source code for more testing examples.

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
    for (const auto& message : messages) {
        std::cout << message; // Print all messages sent to SpectatorD
    }
}
```

{% endraw %}

## Performance

On an `m5d.2xlarge` EC2 instance, with `spectator-cpp-2.0` and
`github.com/Netflix/spectator-cpp/v2 v2.0.13`, we have observed the following single-threaded
performance numbers across a two-minute test window:

* requests/second over `udp`
* requests/second over `unix`

The benchmark incremented a single counter with two tags in a tight loop, to simulate real-world
tag usage, and the rate-per-second observed on the corresponding Atlas graph matched. The protocol 
line was `74` characters in length.

The Go process CPU usage was ~112% and the `spectatord` process CPU usage was ~62% on this 8 vCPU system, for `udp`. It was ~113% and ~85%, respectively, for `unix`.
