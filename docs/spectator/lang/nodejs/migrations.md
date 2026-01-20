## Migrating to 3.X

Version 3.X consists of a major rewrite that turns spectator-js into a thin client designed to send
metrics through [spectatord](https://github.com/Netflix-Skunkworks/spectatord). As a result some
functionality has been moved to other packages or removed.

The library is now written in TypeScript, with support for both `commonjs` and `module` formats, so
types are readily available, and it will work in most contexts.

### New

#### Writers

The `Registry` now supports different Writers. The default writer is `UdpWriter`, which sends metrics
to [spectatord](https://github.com/Netflix-Skunkworks/spectatord) through UDP - these writers are configured through the `Config` object `location`
parameter.

See [Usage > Output Location](usage.md#output-location) for more details.

#### Meters

The following new `Meter`s have been added:

* `AgeGauge`
* `MaxGauge`
* `MonotonicCounter`
* `MonotonicCounterUint`
* `Gauge` with TTL

See [Usage > Meter Types](usage.md#meter-types) for more details.

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

* `Config` is now created through a constructor which provides default values for `undefined`, and
throws an error, if the passed in parameters are not valid.

### Moved

* Runtime metrics collection remains available in [spectator-js-nodejsmetrics](https://github.com/Netflix-Skunkworks/spectator-js-nodejsmetrics),
which has been updated to use this thin client library to report metrics. Follow instructions in the README to enable collection.
* Some types have been moved to different packages. For example, `Counter` is now in `./meter/counter.js`, but it is also
exported in the top-level index.

### Removed

For the removed Meter classes, we observed little to no direct uses of them. They either represent advanced functionality
which was not used or their capabilities are replicated in the currently available set of Meters.

* `BucketCounter` has been removed. This is a pattern on top of the `Counter`, which maps the value to a bucket dimension.
   If this was used properly, then create your own bucket function, add the dimension, and then use the underlying type.
   Alternatively, consider `Counter`.
* `BucketDistributionSummary` has been removed. This is a pattern on top of the `DistributionSummary`, which maps the
   value to a bucket dimension. If this aws used properly, then create your own bucket function, add the dimension, and
   then use the underlying type. Alternatively, consider `DistributionSummary` or `PercentileDistriution` summary.
* `BucketFunctions` has been removed. There should not have been direct uses of this class - it was a support class for
  `BucketCounter`, `BucketDistributionSummary`, and `BucketTimer`. It may be used as a [model](https://github.com/Netflix/spectator-js/blob/v2.0.1/src/bucket_functions.js)
   for recreating bucket functions locally.
* `BucketTimer` has been removed. This is a pattern on top of the `Timer`, which maps the value to a bucket dimension.
   If this was used properly, then create your own bucket function, add the dimension, and then use the underlying type.
   Alternatively, consider `Timer` or `PercentileTimer`.
* `IntervalCounter` has been removed. This is a composite type that has a `Counter` and a duration that measures the age
   since the last increment. Create a `Counter` and an `AgeGauge` that is set to `now()` after each increment, with the
   same name and tags applied.
* `LongTaskTimer` has been removed. This is like an `AgeGauge`, except that it measures the time while executing some
   task. For example, if you have a 4-hour job that runs once a day, you could start it when the task starts and end it
   when the task ends. During the operating window, it would show how long the task has been running. Outside of that,
   interval it would show 0. Implement a `setInterval` to track job status while it remains active, and update a `Gauge`
   metric with the total number of seconds elapsed.
* `PolledMeter` has been removed. Implement a `setInterval` to track the value of interest at a 1-minute interval, and
   update a `Gauge` metric with the value. Alternatively, consider a `Gauge` with a TTL, or an `AgeGauge`.
* `HttpClient` has been removed, and it was never exported. Use the standard `https` client, or another library, instead.
* `Meter`s no longer have a `measure()` method. Meters are now stateless and do not store measurements.
* `Registry` no longer has a `start()` function. The `Registry` is now effectively stateless and there is
  nothing to start other than opening the output location.
* `Registry` no longer has a `stop()` function. Instead, use `close()` to close the registry. Once the
  registry is closed, it can't be started again. This is intended for final clean up of sockets or file handles.
* `Registry` no longer reports `spectator.measurements` metrics. Instead, you can use similar metrics from
  `spectatord` for visibility.
* `Registry` no longer keeps track of the Meters it creates. This means that you can't get a list of all Meters
  from the Registry. If you need to keep track of Meters, you can do so in your application code.
* `Percentile*` Meters no longer support defining min/max values.
* `Registry` no longer allows setting a different logger after creation. A custom logger can be set in the
  `Config` before creating the Registry.

### Migration Steps

1. Make sure you're not relying on any of the [removed functionality](#removed).
2. Update imports for `Config`, `Registry`, and any `Meter`s and `Writer`s that are used for testing.
3. If you used one of the advanced meter types, such as `BucketCounter`, `BucketDistributionSummary`, `BucketTimer`,
   `IntervalCounter`, `LongTaskTimer`, or `PolledMeter`, then choose a replacement implementation as suggested in the
   [removed functionality](#removed) section. Our internal code searches indicate that it was rare for any of these
   to be used, so you are most likely not affected by this change.
4. If you want to collect runtime metrics, then add the [spectator-js-nodejsmetrics](https://github.com/Netflix-Skunkworks/spectator-js-nodejsmetrics)
   library, and follow the instructions in the README.
5. If you use meters such as `PercentileDistributionSummary`, `PercentileTimer`, or `DistributionSummary` then you need to 
   update your code to use the respective functions provided by the `Registry` to initialize these meters. The new functions use
   underscores: `pct_distribution_summary`, `pct_timer`, and `distribution_summary`, respectively.
6. The default `Registry` provided functions no longer accept an `id` as an input. If you previously called `counter`, `timer` 
   or any other meter with an `id`, you must change the input to be a metric `name`, or change the call to use `counter_with_id`, `timer_with_id`, etc.
7. Remove the dependency on the `spectator-js` internal configuration library - it is no longer required.
8. There is no longer an option to `start()` or `stop()` the `Registry` at runtime. If you need to configure a `Registry`
   that doesn't emit metrics, for testing purposes, you can set the `Config` object `location` parameter to `none` to
   configure a no-op writer.
