The value is the time in seconds since the epoch at which an event has successfully occurred, or
`0` to use the current time in epoch seconds. After an Age Gauge has been set, it will continue
reporting the number of seconds since the last time recorded, for as long as the SpectatorD
process runs. The purpose of this metric type is to enable users to more easily implement the
Time Since Last Success alerting pattern.

To set a specific time as the last success:

```cpp

```

To set `now()` as the last success:

```cpp

```

By default, a maximum of `1000` Age Gauges are allowed per `spectatord` process, because there is no
mechanism for cleaning them up. This value may be tuned with the `--age_gauge_limit` flag on the
`spectatord` binary.

Since Age Gauges are long-lived entities that reside in the memory of the SpectatorD process, if
you need to delete and re-create them for any reason, then you can use the [SpectatorD admin server]
to accomplish this task. You can delete all Age Gauges or a single Age Gauge.

**Example:**

```
curl -X DELETE \
http://localhost:1234/metrics/A
```

```
curl -X DELETE \
http://localhost:1234/metrics/A/fooIsTheName,some.tag=val1,some.otherTag=val2
```

[SpectatorD admin server]: ../../../agent/usage.md#admin-server
