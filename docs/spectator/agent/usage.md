[![Build](https://github.com/Netflix-Skunkworks/spectatord/actions/workflows/build.yml/badge.svg)](https://github.com/Netflix-Skunkworks/spectatord/actions/workflows/build.yml)

# SpectatorD Introduction

[SpectatorD] is a high-performance telemetry agent that listens for metrics specified by a
text-based protocol and publishes updates periodically to an [Atlas] aggregator service. It
consolidates the logic required to apply common tagging to all metrics received, maintain
metric lifetimes, and route metrics to the correct backend.

The preferred method of using `spectatord` is to use one of the thin-client implementations,
however, the text-based protocol was designed to make it easy for community-supported clients
to be developed. It is also easy to use in shell scripts with common command line tools.  

[SpectatorD]: https://github.com/Netflix-Skunkworks/spectatord
[Atlas]: https://github.com/Netflix/atlas

## Command Line Configuration Flags

```shell
spectatord --help
spectatord: A daemon that listens for metrics and reports them to Atlas.

    --admin_port (Port number for the admin server.); default: 1234;
    --age_gauge_limit (The maximum number of age gauges that may be reported by
      this process.); default: 1000;
    --common_tags (Common tags: nf.app=app,nf.cluster=cluster. Override the
      default common tags. If empty, then spectatord will use the default set.
      This flag should only be used by experts who understand the risks.);
      default: "";
    --debug (Debug spectatord. All values will be sent to a dev aggregator and
      dropped.); default: false;
    --enable_external (Enable external publishing.); default: false;
    --enable_socket (Enable UNIX domain socket support. Default is true on Linux
      and false on MacOS.); default: true;
    --enable_statsd (Enable statsd support.); default: false;
    --ipv4_only (Enable IPv4-only UDP listeners. This option should only be used
      in environments where it is impossible to run IPv6.); default: false;
    --metatron_dir (Path to the Metatron certificates, which are used for
      external publishing. A number of well-known directories are searched by
      default. This option is only necessary if your certificates are in an
      unusual location.); default: "";
    --meter_ttl (Meter TTL: expire meters after this period of inactivity.);
      default: 15m;
    --no_common_tags (No common tags will be provided for metrics. Since no
      common tags are available, no internal status metrics will be recorded.
      Only use this feature for special cases where it is absolutely necessary
      to override common tags such as nf.app, and only use it with a secondary
      spectatord process.); default: false;
    --port (Port number for the UDP socket.); default: 1234;
    --socket_path (Path to the UNIX domain socket.);
      default: "/run/spectatord/spectatord.unix";
    --statsd_port (Port number for the statsd socket.); default: 8125;
    --uri (Optional override URI for the aggregator.); default: "";
    --verbose (Use verbose logging.); default: false;
    --verbose_http (Output debug info for HTTP requests.); default: false;

Try --helpfull to get a list of all flags or --help=substring shows help for
flags which include specified substring in either in the name, or description or
path.
```

## Endpoints

By default, the daemon will listen on the following endpoints:

* Metrics Message Protocol
  * `1234/udp` *(~430K reqs/sec with 16MB buffers)*
  * `/run/spectatord/spectatord.unix` Domain Socket *(~1M reqs/sec with batching)*
* Admin Server: `1234/tcp`

The choice of which endpoint to use is determined by your performance and access requirements;
the Unix domain socket offers higher performance, but requires filesystem access, which may not
be tenable under some container configurations. See [Performance Numbers](#performance-numbers)
for more details.

## Usage Examples

> :warning: In container environments, the `-w0` option may not work and `-w1` should be
used instead.

```
echo "c:server.numRequests,id=failed:1" | nc -u -w0 localhost 1234
echo "t:server.requestLatency:0.042" | nc -u -w0 localhost 1234
echo "d:server.responseSizes:1024" | nc -w0 -uU /run/spectatord/spectatord.unix
echo "g:someGauge:60" | nc -w0 -uU /run/spectatord/spectatord.unix
echo "g,300:anotherGauge:60" | nc -w0 -uU /run/spectatord/spectatord.unix
echo "X,1543160297100:monotonic.Source:42" | nc -w0 -uU /run/spectatord/spectatord.unix
echo "X,1543160298100:monotonic.Source:43" | nc -w0 -uU /run/spectatord/spectatord.unix
echo "A:age.gauge:0" | nc -u -w0 localhost 1234
```

## Message Format

The message sent to the server has the following format, where the `,options` and `,tags` portions
are optional:

```
metric-type,options:name,tags:value
```

Multiple lines may be sent in the same packet, separated by newlines (`\n`):

```
echo -e "t:server.requestLatency:0.042\nd:server.responseSizes:1024" | nc -u -w0 localhost 1234
```

### Metric Types

| Metric Type                                            | Symbol | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Age Gauge                                              | `A`    | The value is the time in seconds since the epoch at which an event has successfully occurred, or `0` to use the current time in epoch seconds. After an Age Gauge has been set, it will continue reporting the number of seconds since the last time recorded, for as long as the spectatord process runs. The purpose of this metric type is to enable users to more easily implement the Time Since Last Success alerting pattern. <br><br> To set a specific time as the last success: `A:time.sinceLastSuccess:1611081000`. <br><br> To set `now()` as the last success: `A:time.sinceLastSuccess:0`. <br><br> By default, a maximum of `1000` Age Gauges are allowed per `spectatord` process, because there is no mechanism for cleaning them up. This value may be tuned with the `--age_gauge_limit` flag on the spectatord binary. |
| Counter                                                | `c`    | The value is the number of increments that have occurred since the last time it was recorded. The value will be reported to the backend as a rate-per-second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Distribution Summary                                   | `d`    | The value tracks the distribution of events. It is similar to a Timer, but more general, because the size does not have to be a period of time. <br><br> For example, it can be used to measure the payload sizes of requests hitting a server or the number of records returned from a query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Gauge                                                  | `g`    | The value is a number that was sampled at a point in time. The default time-to-live (TTL) for gauges is 900 seconds (15 minutes) - they will continue reporting the last value set for this duration of time. <br><br> Optionally, the TTL may be specified in seconds, with a minimum TTL of 5 seconds. For example, `g,120:gauge:42.0` spcifies a gauge with a 120 second (2 minute) TTL.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Max Gauge                                              | `m`    | The value is a number that was sampled at a point in time, but it is reported as a maximum gauge value to the backend.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Monotonic Counter (double)                             | `C`    | The value is a monotonically increasing number. A minimum of two samples must be received in order for `spectatord` to calculate a delta value and report it to the backend as a rate-per-second. The value is a `double` data type, and negative deltas are ignored. This data type provides flexibility for transforming values into base units with division. <br><br> Commonly used with networking metrics.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Monotonic Counter (uint64)                             | `U`    | The value is a monotonically increasing number. A minimum of two samples must be received in order for `spectatord` to calculate a delta value and report it to the backend as a rate-per-second. The value is a `uint64` data type, and it will handle rollovers. <br><br> Commonly used with networking metrics.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Monotonic Counter (double) with Millisecond Timestamps | `X`    | The value is a monotonically increasing number, sampled at a specified number of milliseconds since the epoch. A minimum of two samples must be received in order for `spectatord` to calculate a delta value and report it to the backend. The value should be a `uint64` data type, and it will handle rollovers. <br><br> This is an **experimental** metric type that can be used to track monotonic sources that were sampled in the recent past, with the value normalized over the reported time period. <br><br> The timestamp in milliseconds since the epoch when the value was sampled must be included as a metric option: `X,1543160297100:monotonic.Source:42`                                                                                                                                                                |
| Percentile Distribution Summary                        | `D`    | The value tracks the distribution of events, with percentile estimates. It is similar to a Percentile Timer, but more general, because the size does not have to be a period of time. <br><br> For example, it can be used to measure the payload sizes of requests hitting a server or the number of records returned from a query. <br><br> In order to maintain the data distribution, they have a higher storage cost, with a worst-case of up to 300X that of a standard Distribution Summary. Be diligent about any additional dimensions added to Percentile Distribution Summaries and ensure that they have a small bounded cardinality.                                                                                                                                                                                           |
| Percentile Timer                                       | `T`    | The value is the number of seconds that have elapsed for an event, with percentile estimates. <br><br> This metric type will track the data distribution by maintaining a set of Counters. The distribution can then be used on the server side to estimate percentiles, while still allowing for arbitrary slicing and dicing based on dimensions. <br><br> In order to maintain the data distribution, they have a higher storage cost, with a worst-case of up to 300X that of a standard Timer. Be diligent about any additional dimensions added to Percentile Timers and ensure that they have a small bounded cardinality.                                                                                                                                                                                                           |
| Timer                                                  | `t`    | The value is the number of seconds that have elapsed for an event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

The data type for all numbers except `U` is `double`. The `U` values are recorded as `uint64_t`, and the calculated
deltas are passed to the backend as `double`. Passing negative values for `uint64_t` data types will cause the parsed
string value to rollover.

### Metric Name and Tags

The metric name and tags must follow Atlas restrictions, which are described in the sections below.

Tags are optional. They may be specified as comma-separated `key=value` pairs after the metric name.
For example:

```
fooIsTheName,some.tag=val1,some.otherTag=val2
```

See [Atlas Naming Conventions](https://netflix.github.io/atlas-docs/concepts/naming/) for
recommendations on naming metrics.

#### Length Restrictions

| Limit            | Min | Max |
|------------------|-----|-----|
| Length of `name` |   1 | 255 |
| Tag key length   |   2 |  60 |
| Tag value length |   1 | 120 |

#### Allowed Characters

The metric name, tag keys and values may only use characters in the following set: `-._A-Za-z0-9`.

All others characters will be converted to an underscore (`_`) by the client.

To avoid issues with parsing metrics, avoid using the SpectatorD protocol delimiter characters
(`,=:`) rather than relying on the client to rewrite them to `_`.

### Metric Value

A double value, or a uint64 value for one kind of Monotonic Counters. The meaning of the value
depends on the metric type.

## Metrics

See [Metrics](./metrics.md) for a list of metrics published by this service.

## Admin Server

An administrative server is provided with SpectatorD, so that debugging information and few
data management tasks may be completed. By default, this server listens on port `1234/TCP`,
but this can be modified with the `--admin_port` flag. The endpoints which change data may
only be accessed from localhost.

* `GET /`
    * Returns a service description and list of available endpoints. 
* `GET /config`
    * Returns the current SpectatorD configuration, including the current set of common tags.
* `GET /config/common_tags`
    * Returns a description of how to use this endpoint to modify common tags.
* `POST /config/common_tags`
    * Create, modify or delete common tags from the allowed set of Mantis common tags. No other
    common tags may be modified. Create or update a tag by setting it to a string. Delete a tag
    by setting the value to an empty string.
    * Allowed tags:
        * `mantisJobId`
        * `mantisJobName`
        * `mantisUser`
        * `mantisWorkerIndex`
        * `mantisWorkerNumber`
        * `mantisWorkerStageNumber`
    * Example:
        ```
        curl -X POST \
        -d '{"mantisJobId": "foo", "mantisJobName": "bar", "mantisUser": ""}' \
        -w " %{http_code}\n" \
        http://localhost:1234/config/common_tags
        ```
* `GET /metrics`
    * Return an object containing lists of all metrics currently known to the Registry, grouped
    by type.
* `DELETE /metrics/A`
    * Delete all AgeGauge metrics from the Registry. 
* `DELETE /metrics/A/{id}`
    * Delete one AgeGauge metric from the Registry, identified by the `id`.
    * Example:
        ```
        curl -X DELETE \
        -w " %{http_code}\n" \
        http://localhost:1234/metrics/A/fooIsTheName,some.tag=val1,some.otherTag=val2
        ```
* `DELETE /metrics/g`
    * Delete all Gauge metrics from the Registry. 
* `DELETE /metrics/g/{id}`
    * Delete one Gauge metric from the Registry, identified by the `id`.
    * Example:
        ```
        curl -X DELETE \
        -w " %{http_code}\n" \
        http://localhost:1234/metrics/g/fooIsTheName,some.tag=val1,some.otherTag=val2
        ```

## Performance Numbers

A key goal of this project is to deliver high performance. This means that we need to use few
resources for the common use case, where the number of metric updates is relatively small
(< 10k reqs/sec), and it also needs to be able to handle hundreds of thousands of updates per
second when required.

Using Unix domain sockets, we can handle close to 1M metric updates per second, assuming the client
batches the updates and sends a few at a time. Sending every single metric update requires a lot of
context switching, but is something that works well for the majority of our use cases. This
simplicity means the user does not have to maintain any local state.

```
Transport          Batch Size    First 10M          Second 10M
Unix Dgram         1             22.98s (435k rps)  20.58s (486k rps)
Unix Dgram         8             11.46s (873k rps)   9.89s (1011k rps)
Unix Dgram         32            10.38s (963k rps)   8.49s (1178k rps)
```

The UDP transport is particularly sensitive the max receive buffer size (16MB on our systems). 

Our tests indicate that sending 430K rps to the UDP port did not drop packets, but if there is a
need for higher throughput, then tweaking `/proc/sys/net/unix/max_dgram_qlen` is recommended.
