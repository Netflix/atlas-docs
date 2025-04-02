# spectator-js Usage

[![npm version](https://badge.fury.io/js/nflx-spectator.svg)](https://badge.fury.io/js/nflx-spectator)

TypeScript thin-client metrics library compiled to JavaScript for use with [Atlas] and [SpectatorD].

Intended for use with [Node.js] applications.

[Atlas]: https://netflix.github.io/atlas-docs/overview/
[SpectatorD]: https://netflix.github.io/atlas-docs/spectator/agent/usage/
[Node.js]: https://nodejs.org

## Supported Node.js Versions

This library currently targets Node.js >= 18. Supports both `commonjs` and `module` formats.

## Installing

Install this library and the runtime metrics library for your project as follows:

```shell
npm install nflx-spectator --save
npm install nflx-spectator-nodejsmetrics --save
```

## Instrumenting Code

### Simple Example

#### CommonJS

```javascript
const express = require("express");
const app = express();
const port = 3000;

const spectator = require("nflx-spectator");
const registry = new spectator.Registry();

app.get("/", (req, res) => {
    res.send("Usage: /api/v1/play?country=foo&title=bar")
});

app.get("/api/v1/play", (req, res) => {
    const country = req.query.country || "unknown";
    const title = req.query.title || "unknown";

    let status, message;
    if (!req.query.country || !req.query.title) {
        status = 404;
        message = `invalid play request for country=${country} title=${title}`;
    } else {
        status = 200;
        message = `requested play for country=${country} title=${title}`;
    }

    const tags = {"path": "v1_play", "country": country, "title": title, "status": status.toString()};
    void registry.counter("server.requestCount", tags).increment();

    res.status(status).send(message);
});

app.listen(port, () => {
    console.log(`server listening on ${port}`)
});
```

Save this snippet as `app.js`, then `node app.js`.

#### Module

```javascript
import express from "express";
import {Registry} from "nflx-spectator";

const app = express();
const port = 3000;

const registry = new Registry();

app.get("/", (req, res) => {
    res.send("Usage: /api/v1/play?country=foo&title=bar")
});

app.get("/api/v1/play", (req, res) => {
    const country = req.query.country || "unknown";
    const title = req.query.title || "unknown";

    let status, message;
    if (!req.query.country || !req.query.title) {
        status = 404;
        message = `invalid play request for country=${country} title=${title}`;
    } else {
        status = 200;
        message = `requested play for country=${country} title=${title}`;
    }

    const tags = {"path": "v1_play", "country": country, "title": title, "status": status.toString()};
    void registry.counter("server.requestCount", tags).increment();

    res.status(status).send(message);
});

app.listen(port, () => {
    console.log(`server listening on ${port}`)
});
```

Save this snippet as `app.js`, then `node app.js`.

### Complex Example

#### CommonJS

```javascript
const express = require("express");
const app = express();
const port = 3000;

const spectator = require("nflx-spectator");
const config = new spectator.Config("udp", {"platform": "express-demo"});
const registry = new spectator.Registry(config);

const nodejsMetrics = require("nflx-spectator-nodejsmetrics");
const runtimeMetrics = new nodejsMetrics.RuntimeMetrics(registry);
runtimeMetrics.start();

const requestCountId = registry.new_id("server.requestCountId", {"path": "v1_play"});
const requestLatency = registry.timer("server.requestLatency", {"path": "v1_play"});
const responseSize = registry.distribution_summary("server.responseSize", {"path": "v1_play"});

app.get("/", (req, res) => {
    res.send("Usage: /api/v1/play?country=foo&title=bar")
});

app.get("/api/v1/play", (req, res) => {
    const start = process.hrtime();
    const country = req.query.country || "unknown";
    const title = req.query.title || "unknown";

    let status, message;
    if (!req.query.country || !req.query.title) {
        status = 404;
        message = `invalid play request for country=${country} title=${title}`;
    } else {
        status = 200;
        message = `requested play for country=${country} title=${title}`;
    }

    const tags = {"country": country, "title": title, "status": status.toString()};
    const requestCount = registry.counter_with_id(requestCountId.with_tags(tags));

    void requestCount.increment();
    void responseSize.record(message.length);
    void requestLatency.record(process.hrtime(start));

    res.status(status).send(message);
});

const server = app.listen(port, () => {
    console.log(`server listening on ${port}`)
});

const shutdown = function () {
    console.log("server shutdown");
    server.close();
    runtimeMetrics.stop();
    process.exit(0);
};

process.on("SIGINT", shutdown);
process.on("SIGTERM", shutdown);
```

Save this snippet as `app.js`, then `node app.js`.

#### Module

```javascript
import express from "express";
import {Config, Registry} from "nflx-spectator";
import {RuntimeMetrics} from "nflx-spectator-nodejsmetrics";

const app = express();
const port = 3000;

const config = new Config("udp", {"platform": "express-demo"});
const registry = new Registry(config);
const runtimeMetrics = new RuntimeMetrics(registry);

runtimeMetrics.start();

const requestCountId = registry.new_id("server.requestCountId", {"path": "v1_play"});
const requestLatency = registry.timer("server.requestLatency", {"path": "v1_play"});
const responseSize = registry.distribution_summary("server.responseSize", {"path": "v1_play"});

app.get("/", (req, res) => {
    res.send("Usage: /api/v1/play?country=foo&title=bar")
});

app.get("/api/v1/play", (req, res) => {
    const start = process.hrtime();
    const country = req.query.country || "unknown";
    const title = req.query.title || "unknown";

    let status, message;
    if (!req.query.country || !req.query.title) {
        status = 404;
        message = `invalid play request for country=${country} title=${title}`;
    } else {
        status = 200;
        message = `requested play for country=${country} title=${title}`;
    }

    const tags = {"country": country, "title": title, "status": status.toString()};
    const requestCount = registry.counter_with_id(requestCountId.with_tags(tags));

    void requestCount.increment();
    void responseSize.record(message.length);
    void requestLatency.record(process.hrtime(start));

    res.status(status).send(message);
});

const server = app.listen(port, () => {
    console.log(`server listening on ${port}`)
});

const shutdown = function () {
    console.log("server shutdown");
    server.close();
    runtimeMetrics.stop();
    process.exit(0);
};

process.on("SIGINT", shutdown);
process.on("SIGTERM", shutdown);
```

Save this snippet as `app.js`, then `node app.js`.

## Override Logger

You can override the logger used by the Spectator registry by setting the logger parameter in the
`Config` object. The specified logger should provide `debug`, `info`, and `error` methods. By
default, `spectator-js` logs to stdout.

```javascript
const logger = require('pino')();
const spectator = require("nflx-spectator");
const config = new spectator.Config("udp", {}, logger);
const registry = new spectator.Registry(config);
```

## Runtime Metrics

Use [spectator-js-nodejsmetrics](https://github.com/Netflix-Skunkworks/spectator-js-nodejsmetrics).

The [Instrumenting Code](#complex-example) examples show how to use this library.

## Working with Id Objects

Each metric stored in Atlas is uniquely identified by the combination of the name and the tags
associated with it. In `spectator-js`, this data is represented with `Id` objects, created
by the `Registry`. The `new_id()` method returns new `Id` objects, which have extra common
tags applied, and which can be further customized by calling the `with_tag()` and `with_tags()`
methods. Each `Id` will create and store a validated subset of the `spectatord` protocol line
to be written for each `Meter`, when it is instantiated. `Id` objects can be passed around and
used concurrently. Manipulating the tags with the provided methods will create new `Id` objects.

Note that **all tag keys and values must be strings.** For example, if you want to keep track of
the number of successful requests, then you must cast integers to strings. The `Id` class will
validate these values, dropping or changing any that are not valid, and reporting a warning log.

```javascript
import {Registry} from "nflx-spectator";

const registry = new Registry();
void registry.counter("server.numRequests", {"statusCode": str(200)}).increment();

const num_requests_id = registry.new_id("server.numRequests", {"statusCode": str(200)});
void registry.counter_with_id(num_requests_id).increment();
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

    ```javascript
    import {Config, Registry} from "nflx-spectator";
    
    const config = new Config("udp://[::1]:1234");
    const registry = new Registry(config);
    void registry.counter("server.numRequests").increment();
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

When using `spectator-js` to report metrics from a batch job, ensure that the batch job runs for at
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
`spectator-js` and `spectatord` low (around 1% or less), as compared to up to 40% for high-volume
scenarios.

## Writing Tests

To write tests against this library, instantiate an instance of the `Registry` and provide a `Config`
that selects the [MemoryWriter](https://github.com/Netflix/spectator-js/blob/main/src/writer/memory_writer.ts).
This `Writer` stores all updates in a `string[]`. Use the `writer()` method on the `Registry` to
access the writer, then inspect the `last_line()` or `get()` all messages to verify your metrics
updates.

```typescript
import {assert} from "chai";
import {Counter, Id, MemoryWriter} from "../../src/index.js";
import {describe, it} from "node:test";

describe("Metrics Test", (): void => {

    it("increment", (): void => {
        const r = new Registry(new Config("memory"));
        const writer = r.writer() as MemoryWriter;

        const c: Counter = r.counter("counter");
        assert.isTrue(writer.is_empty());

        void c.increment();
        assert.equal("c:counter:1", writer.last_line());
    });
});
```

### Protocol Parser

A [SpectatorD] line protocol parser is available, which ca be used for validating the results
captured by a `MemoryWriter`.

```typescript
import {assert} from "chai";
import {Id, parse_protocol_line} from "../src/index.js";
import {describe, it} from "node:test";

describe("Protocol Parser Tests", (): void => {
    it("parse counter with multiple tags", (): void => {
        const [symbol, id, value] = parse_protocol_line("c:counter,foo=bar,baz=quux:1");
        assert.equal("c", symbol);
        assert.equal("counter", id.name());
        assert.deepEqual({"foo": "bar", "baz": "quux"}, id.tags());
        assert.equal("1", value);
    });
});
```

[SpectatorD]: ../../agent/usage.md
