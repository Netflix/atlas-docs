## Migrating to 2.X

Version 2.X consists of a major rewrite that turns spectator-go into a thin client designed to send
metrics through [spectatord](https://github.com/Netflix-Skunkworks/spectatord). As a result some
functionality has been moved to other packages or removed.

### New

#### Writers

`spectator.Registry` now supports different writers. The default writer is `writer.UdpWriter` which
sends metrics to [spectatord](https://github.com/Netflix-Skunkworks/spectatord) through UDP.

See [Usage > Output Location](usage.md#output-location) for more details.

#### Meters

The following new Meters have been added:

* `meter.MaxGauge`
* `meter.Gauge` with TTL

#### Common Tags

A few local environment common tags are now automatically added to all Meters. Their values are read
from the environment variables.

| Tag          | Environment Variable |
|--------------|----------------------|
| nf.container | TITUS_CONTAINER_NAME |
| nf.process   | NETFLIX_PROCESS_NAME |

Tags from environment variables take precedence over tags passed on code when creating the `Config`.

Note that common tags sourced by [spectatord](https://github.com/Netflix-Skunkworks/spectatord) can't be overwritten.

#### Config

* `Config` is now created through a constructor which throws error if the passed in parameters are not valid.
* `Config` members are now private.

### Moved

* Runtime metrics collection has been moved
  to [spectator-go-runtime-metrics](https://github.com/Netflix/spectator-go-runtime-metrics). Follow instructions in
  the [README](https://github.com/Netflix/spectator-go-runtime-metrics) to enable collection.
* Some types have been moved to different packages. For example, `spectator.Counter` is now in `meter.Counter`.

### Removed

* `spectator.HttpClient` has been removed. Use the standard `http.Client` instead.
* `spectator.Meter`s no longer have a `Measure() []Measurement` function. Meters are now stateless and do not store
  measurements.
* `spectator.Clock` has been removed. Use the standard `time` package instead.
* `spectator.Config` is simplified and local to this library. There is no longer a need to import the internal
  configuration library.
* `spectator.Registry` no longer has a `Start()` function. The `Registry` is now effectively stateless and there is
  nothing to start other than opening the output location.
* `spectator.Registry` no longer has a `Stop()` function. Instead, use `Close()` to close the registry. Once the
  registry is closed, it can't be started again. This is intended for final clean up of sockets or file handles.
* `spectator.Config.IpcTimerRecord` has been removed. Use a `meter.Timer` instead to record Ipc metrics.
* `spectator.MeterFactoryFun` has been removed. If you need to create a custom meter you can do so by wrapping one of
  the meters returned by `spectator.Registry`.
* `spectator.Registry` no longer reports `spectator.measurements` metrics. Instead, you can use similar metrics from
  `spectatord` for visibility.
* `spectator.Registry` no longer keeps track of the Meters it creates. This means that you can't get a list of all Meters
  from the Registry. If you need to keep track of Meters, you can do so in your application code.
* `Percentile*` meters no longer support defining min/max values.
* `spectator.Registry` no longer allows setting a different logger after creation. A custom logger can be set in the
  `spectator.Config` before creating the Registry.
* File-based configuration is no longer supported.

### Migration Steps

1. Make sure you're not relying on any of the [removed functionality](#removed).
2. Update imports for `Config` and `Registry`, and use the `meters` package instead of `spectator` for Meters.
3. If you want to collect runtime metrics, add the [spectator-go-runtime-metrics](https://github.com/Netflix/spectator-go-runtime-metrics)
   library, and follow the instructions in the README.
4. If you use `PercentileDistributionSummary` or `PercentileTimer`, then  you need to update your code to use the
   respective functions provided by the `Registry` to initialize these meters.
5. Remove the dependency on the `spectator-go` internal configuration library - it is no longer required.
6. There is no longer an option to `start()` or `stop()` the registry at runtime. If you need to configure a `Registry`
   that doesn't emit metrics, for testing purposes, you can use the `spectator.Config.Location` option with `none` to
   configure a no-op writer.
