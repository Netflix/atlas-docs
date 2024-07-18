# spectator-py Usage

Python thin-client [metrics library] for use with [Atlas] and [SpectatorD].

Supports Python >= 3.5. This version is chosen as the baseline, because it is the oldest system
Python available in our operating environments. 

[metrics library]: https://github.com/Netflix/spectator-py
[Atlas]: ../../../overview.md
[SpectatorD]: ../../agent/usage.md

## Installing

Install this library for your project as follows:

```shell
pip3 install netflix-spectator-py
```

Publishing metrics requires a [SpectatorD] process running on your instance.



## Importing

### Standard Usage

Importing the `GlobalRegistry` instantiates a `Registry` with a default configuration that applies
process-specific common tags based on environment variables and opens a socket to the [SpectatorD]
agent. The remainder of the instance-specific common tags are provided by [SpectatorD].

```python
from spectator import GlobalRegistry
```

Once the `GlobalRegistry` is imported, it is used to create and manage Meters.

### Logging

This package provides the following loggers:

* `spectator.MeterId`
* `spectator.SidecarWriter`

The `MeterId` logger is used to report invalid meters which have not-a-str tag keys or values.

When troubleshooting metrics collection and reporting, you should set the `SidecarWriter` logging
to the `DEBUG` level, before the first metric is recorded. For example:

```python
import logging

# record the human-readable time, name of the logger, logging level, thread id and message
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(thread)d - %(message)s'
)

logging.getLogger('spectator.SidecarWriter').setLevel(logging.DEBUG)
```

There is approximately a 10% performance penalty in UDP write performance when debug logging is
enabled. It may be more, depending on the exact logging configuration (i.e. flushing to slow disk).

## Working with IDs

The IDs used for identifying a meter in the `GlobalRegistry` consist of a name and a set of tags.
IDs will be consumed by users many times after the data has been reported, so they should be
chosen thoughtfully, while considering how they will be used. See the [naming conventions] page
for general guidelines.

IDs are immutable, so they can be freely passed around and used in a concurrent context. Tags can
be added to an ID when it is created, to track the dimensionality of the metric. **All tag keys
and values must be strings.** For example, if you want to keep track of the number of successful
requests, you must cast integers to strings.

```python
from spectator import GlobalRegistry

requests_id = GlobalRegistry.counter("server.numRequests", {"statusCode": str(200)})
requests_id.increment()
```

[naming conventions]: https://netflix.github.io/atlas-docs/concepts/naming/

## Meter Types

* [Age Gauge](./meters/age-gauge.md)
* [Counter](./meters/counter.md)
* [Distribution Summary](./meters/dist-summary.md)
* [Gauge](./meters/gauge.md)
* [Max Gauge](./meters/max-gauge.md)
* [Monotonic Counter](./meters/mono-counter.md)
* [Percentile Distribution Summary](./meters/pct-dist-summary.md)
* [Percentile Timer](./meters/pct-timer.md)
* [Timer](./meters/timer.md)

## asyncio Support

The `GlobalRegistry` provides a `UdpWriter` implementation of the `SidecarWriter` by default. UDP
is a non-blocking, unordered and connectionless protocol, which is ideal for communicating with a
local [SpectatorD] process in a variety of circumstances. The `UdpWriter` should be used in asyncio
applications.

The `PrintWriter` implementation, which can be used to communicate with the [SpectatorD] Unix domain
socket, does not offer asyncio support at this time.

## IPv6 Support

By default, [SpectatorD] will listen on `IPv6 UDP *:1234`, without setting the `v6_only(true)`
flag. On dual-stacked systems, this means that it will receive packets from both IPv4 and IPv6,
and the IPv4 addresses will show up on the server as IPv4-mapped IPv6 addresses.

By default, the `GlobalRegistry` will write UDP packets to `127.0.0.1:1234`, which will allow
for communication with [SpectatorD] on dual-stacked systems.

On IPv6-only systems, it may be necessary to change the default configuration using one of the
following methods:

* Configure the following environment variable, which will override the default configuration of
the `GlobalRegistry`:

      export SPECTATOR_OUTPUT_LOCATION="udp://[::1]:1234"

* Configure a custom Registry, instead of using the `GlobalRegistry`:

      from spectator import Registry
      from spectator.sidecarconfig import SidecarConfig
      
      r = Registry(config=SidecarConfig({"sidecar.output-location": "udp://[::1]:1234"}))
      r.counter("test").increment()

## Writing Tests

To write tests against this library, instantiate a test instance of the Registry and configure it
to use the [MemoryWriter](https://github.com/Netflix/spectator-py/blob/main/spectator/sidecarwriter.py#L63-L80),
which stores all updates in a List. Use the `writer()` method on the Registry to access the writer,
then inspect the `last_line()` or `get()` all messages to verify your metrics updates.

```python
import unittest

from spectator import Registry
from spectator.sidecarconfig import SidecarConfig

class MetricsTest(unittest.TestCase):

    def test_counter(self):
        r = Registry(config=SidecarConfig({"sidecar.output-location": "memory"}))

        c = r.counter("test")
        self.assertTrue(r.writer().is_empty())

        c.increment()
        self.assertEqual("c:test:1", r.writer().last_line())
```

If you need to override the default output location (udp) of the `GlobalRegistry`, then you can
set a `SPECTATOR_OUTPUT_LOCATION` environment variable to one of the following values supported
by the `SidecarConfig` class:

* `none` - Disable output.
* `memory` - Write to memory.
* `stdout` - Write to standard out for the process.
* `stderr` - Write to standard error for the process.
* `file://$path_to_file` - Write to a file (e.g. `file:///tmp/foo/bar`).
* `udp://$host:$port` - Write to a UDP socket.

If you want to disable metrics publishing from the `GlobalRegistry`, then you can set:

```shell
export SPECTATOR_OUTPUT_LOCATION=none
```

If you want to validate the metrics that will be published through the `GlobalRegistry`
in tests, then you can set:

```shell
export SPECTATOR_OUTPUT_LOCATION=memory
```

The `MemoryWriter` subclass offers a few methods to inspect the values that it captures:

* `clear()` - Delete the contents of the internal list.
* `get()` - Return the internal list.
* `is_empty()` - Is the internal list empty?
* `last_line()` - Return the last element of the internal list.

Lastly, a [SpectatorD] line protocol parser is available, which is intended to be used for validating
the results captured by a `MemoryWriter`. It may be used as follows:

```python
import unittest

from spectator.counter import Counter
from spectator.protocolparser import parse_protocol_line


class ProtocolParserTest(unittest.TestCase):

    def test_parse_counter_with_multiple_tags(self):
        meter_class, meter_id, value = parse_protocol_line("c:test,foo=bar,baz=quux:1")
        self.assertEqual(Counter, meter_class)
        self.assertEqual("test", meter_id.name)
        self.assertEqual({"foo": "bar", "baz": "quux"}, meter_id.tags())
        self.assertEqual("1", value)
```

[SpectatorD]: ../../agent/usage.md
