# spectator-py Usage

Python thin-client [metrics library] for use with [Atlas] and [SpectatorD].

[metrics library]: https://github.com/Netflix/spectator-py
[Atlas]: ../../../overview.md
[SpectatorD]: ../../agent/usage.md

## Supported Python Versions

This library currently targets the Python >= 3.8.

## Installing

Install this library for your project as follows:

```shell
pip install netflix-spectator-py
```

## Instrumenting Code

### Simple Example

```python
import logging

from flask import Flask, request, Response
from flask.logging import default_handler
from spectator.registry import Registry

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(default_handler)

registry = Registry()

app = Flask(__name__)

@app.route("/")
def root():
    return Response("Usage: /api/v1/play?country=foo&title=bar")

@app.route("/api/v1/play", methods=["GET", "POST"])
def play():
    country = request.args.get("country", default="none")
    title = request.args.get("title", default="none")
    registry.counter("server.requestCount", {"version": "v1"}).increment()
    return Response(f"requested play for country={country} title={title}")
```

Save this snippet as `app.py`, then `flask --app app run`.

### Complex Example

```python
import logging

from flask import Flask, request, Response
from flask.logging import default_handler
from spectator.config import Config
from spectator.registry import Registry
from spectator.stopwatch import StopWatch

root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)
root_logger.addHandler(default_handler)

config = Config(extra_common_tags={"nf.platform": "my_platform"})
registry = Registry(config)

request_count_id = registry.new_id("server.requestCount", {"version": "v1"})
request_latency = registry.timer("server.requestLatency")
response_size = registry.distribution_summary("server.responseSize")

app = Flask(__name__)

@app.route("/")
def root():
    return Response("Usage: /api/v1/play?country=foo&title=bar")

@app.route("/api/v1/play", methods=["GET", "POST"])
def play():
    if request.method == "GET":
        with StopWatch(request_latency):
            status_code = 200
            country = request.args.get("country", default="none")
            title = request.args.get("title", default="none")

            tags = {"country": country, "title": title, "status": str(status_code)}
            request_count_with_tags = request_count_id.with_tags(tags)
            counter = registry.counter_with_id(request_count_with_tags)
            counter.increment()

            message = f"requested play for country={country} title={title}"
            response_size.record(len(message))
            return Response(message, status=status_code)
    else:
        status_code = 405

        tags = {"status": str(status_code)}
        request_count_with_tags = request_count_id.with_tags(tags)
        counter = registry.counter_with_id(request_count_with_tags)
        counter.increment()

        return Response("unsupported request method", status=status_code)
```

Save this snippet as `app.py`, then `flask --app app run`.

## Importing

### Standard Usage

Instantiate a `Registry` object, with either a default or custom `Config`, and use it to create and
manage `MeterId` and `Meter` objects.

```python
from spectator.registry import Registry

registry = Registry()
registry.counter("server.requestCount").increment()
```

### Legacy Usage

The `GlobalRegistry` concept is a hold-over from the thick-client version of this library, but it
has been maintained to help minimize the amount of code change that application owners need to
implement when adopting the thin client version of the library. It existed as a concept in the
thick client because it was stateful, and required starting background threads. The thin client
version is stateless. 

Importing the `GlobalRegistry` instantiates a `Registry` with a default `Config` that applies
process-specific common tags based on environment variables and opens a UDP socket to the local
[SpectatorD] agent. The remainder of the instance-specific common tags are provided by [SpectatorD].
Once imported, the `GlobalRegistry` can be used to create and manage Meters.

```python
from spectator import GlobalRegistry

GlobalRegistry.counter("server.requestCount").increment()
```

### Logging

This package provides the following loggers:

* `spectator.meter.meter_id`, which reports invalid tags at WARNING level.
* `spectator.registry`, which reports Registry status messages at INFO level, and errors closing
writers at ERROR level.
* `spectator.writer`, which reports the protocol lines written at DEBUG level, and writing errors
at ERROR level.

When troubleshooting metrics collection and reporting, you should set the `spectator.meter.meter_id`
logger to `DEBUG` level, before the first metric is recorded. For example:

```python
import logging

# record the human-readable time, name of the logger, logging level, thread id and message
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(message)s'
)

logging.getLogger('spectator.meter.meter_id').setLevel(logging.DEBUG)
```

## Runtime Metrics

Use [spectator-py-runtime-metrics](https://github.com/Netflix/spectator-py-runtime-metrics). Follow
instructions in the README to enable collection.

## Working with MeterId Objects

Each metric stored in Atlas is uniquely identified by the combination of the name and the tags
associated with it. In `spectator-py`, this data is represented with `MeterId` objects, created
by the `Registry`. The `new_id()` method returns new `MeterId` objects, which have extra common
tags applied, and which can be further customized by calling the `with_tag()` and `with_tags()`
methods. Each `MeterId` will create and store a validated subset of the `spectatord` protocol line
to be written for each `Meter`, when it is instantiated. `MeterId` objects are immutable, so they
can be freely passed around and used concurrently. Manipulating the tags with the provided methods
will create new `MeterId` objects, to assist with maintaining immutability.

Note that **all tag keys and values must be strings.** For example, if you want to keep track of the
number of successful requests, then you must cast integers to strings. The `MeterId` class will
validate these values, dropping or changing any that are not valid, and reporting a warning log.

```python
from spectator.registry import Registry

registry = Registry()
registry.counter("server.numRequests", {"statusCode": str(200)}).increment()

num_requests_id = registry.new_id("server.numRequests", {"statusCode": str(200)})
registry.counter_with_id(num_requests_id).increment()
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

## asyncio Support

The `Registry` provides a `UdpWriter` by default. UDP is a non-blocking, unordered and
connectionless protocol, which is ideal for communicating with a local [SpectatorD]
process in a variety of circumstances. The `UdpWriter` should be used in asyncio
applications.

The `FileWriter` implementation, which can be used to communicate with the [SpectatorD] Unix domain
socket, for slightly higher performance, does not offer asyncio support at this time.

## IPv6 Support

By default, [SpectatorD] will listen on `IPv6 UDP *:1234`, without setting the `v6_only(true)`
flag. On dual-stacked systems, this means that it will receive packets from both IPv4 and IPv6,
and the IPv4 addresses will show up on the server as IPv4-mapped IPv6 addresses.

By default, the `UdpWriter` will send UDP packets to `127.0.0.1:1234`, which will allow for
communication with [SpectatorD] on dual-stacked systems.

On IPv6-only systems, it may be necessary to change the default configuration using one of the
following methods:

* Configure the following environment variable, which will override the default location `Config`
in the `Registry`:

```shell
export SPECTATOR_OUTPUT_LOCATION="udp://[::1]:1234"
```

* Provide a custom `Config` for the `Registry`:

```python
from spectator.config import Config
from spectator.registry import Registry

config = Config(location="udp://[::1]:1234")
registry = Registry(config)
registry.counter("server.numRequests").increment()
```

## Output Location

If you need to override the default output location (UDP) of the `Registry`, then you can set a
`Config` class location to one of the following supported values:

* `none`   - Disable output.
* `memory` - Write to memory.
* `stderr` - Write to standard error for the process.
* `stdout` - Write to standard out for the process.
* `udp`    - Write to the default UDP port for `spectatord`.
* `unix`   - Write to the default unix datagram socket for `spectatord`.
* `file://$path_to_file` - Write to a custom file (e.g. `file:///tmp/foo/bar`).
* `udp://$host:$port`    - Write to a custom UDP socket.

The `SPECTATOR_OUTPUT_LOCATION` environment variable accepts the same values, and can be used to
override the value provided to the `Config` class, which may be useful in CI/CD contexts. For
example, if you want to disable metrics publishing from the `Registry`, then you can set:

```shell
export SPECTATOR_OUTPUT_LOCATION=none
```

## Batch Usage

When using `spectator-py` to report metrics from a batch job, ensure that the batch job runs for at
least five (5), if not ten (10) seconds in duration. This is necessary in order to allow sufficient
time for `spectatord` to publish metrics to the Atlas backend; it publishes every five seconds. If
your job does not run this long, or you find you are missing metrics that were reported at the end
of your job run, then add a five-second sleep before exiting: `time.sleep(5)`. This will allow time
for the metrics to be sent.

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
`spectator-py` and `spectatord` low (around 1% or less), as compared to up to 40% for high-volume
scenarios.

## Writing Tests

To write tests against this library, instantiate an instance of the `Registry` and provide a `Config`
that selects the [MemoryWriter](https://github.com/Netflix/spectator-py/blob/main/spectator/writer/memory_writer.py).
This `Writer` stores all updates in a `List[str]`. Use the `writer()` method on the `Registry` to
access the writer, then inspect the `last_line()` or `get()` all messages to verify your metrics
updates.

```python
import unittest

from spectator.config import Config
from spectator.registry import Registry

class MetricsTest(unittest.TestCase):

    def test_counter(self):
        r = Registry(Config("memory"))

        c = r.counter("server.numRequests")
        self.assertTrue(r.writer().is_empty())

        c.increment()
        self.assertEqual("c:server.numRequests:1", r.writer().last_line())
```

### Protocol Parser

A [SpectatorD] line protocol parser is available, which ca be used for validating  the results
captured by a `MemoryWriter`.

```python
import unittest

from spectator.meter.counter import Counter
from spectator.protocol_parser import get_meter_class, parse_protocol_line

class ProtocolParserTest(unittest.TestCase):

    def test_parse_counter_with_multiple_tags(self):
        symbol, id, value = parse_protocol_line("c:counter,foo=bar,baz=quux:1")
        self.assertEqual("c", symbol)
        self.assertEqual(Counter, get_meter_class(symbol))
        self.assertEqual("counter", id.name())
        self.assertEqual({"foo": "bar", "baz": "quux"}, id.tags())
        self.assertEqual("1", value)
```

[SpectatorD]: ../../agent/usage.md
