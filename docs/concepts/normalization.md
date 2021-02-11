# Normalization

In Atlas, this usually refers to normalizing [data points](time-series.md#data-point) to step
boundaries. Suppose that values are actually getting reported at 30 seconds after the minute,
instead of exactly on the minute. The values will get normalized to the minute boundary, so
that all time series in the system are consistent.

How a normalized value is computed depends on the data source type. Atlas supports three types
indicated by the value of the `atlas.dstype` tag. In general, you should not need to worry about
that, client libraries like [Spectator](../spectator/index.md) will automatically handle tagging based on
the data source type.

It is recommended to at least skim through the normalization for [gauges](#gauge) and
[rates](#rates) to better understand how the values you see actually relate to measured
data.

## Gauge

A value that is sampled from some source and the value is used as is. The last value received will
be the value used for the interval. For example:

```
                ┌─────────┐                                    ┌─────────┐
                │    8    │                                    │    8    │
                │         ├───────                             │         │
                │         │    6                               │         │
──────┐         │         │                ┌─────────┐         │         │
 4    │         │         │                │    4    │         │         │
      ├─────────┤         │           to   │         ├─────────┤         │
      │    2    │         │                │         │    2    │         │
 ├─────────┼─────────┼─────────┤           ├─────────┼─────────┼─────────┤
1:00      1:01      1:02      1:03        1:00      1:01      1:02      1:03
```

## Rate

A rate is a value representing the rate per second since the last reported value. Rate values
are normalized using a weighted average. For example:

```
                ┌─────────┐
                │    8    │                                    ┌─────────┐
                │         ├───────                             │    7    │
                │         │    6                     ┌─────────┤         │
──────┐         │         │                          │    5    │         │
 4    │         │         │                ┌─────────┤         │         │
      ├─────────┤         │           to   │    3    │         │         │
      │    2    │         │                │         │         │         │
 ├─────────┼─────────┼─────────┤           ├─────────┼─────────┼─────────┤
1:00      1:01      1:02      1:03        1:00      1:01      1:02      1:03
```

Here, the data is reported at exactly 30s after the minute boundary. So each value represents the
average rate per second for 50% of the minute.

| Time | Value                         |
|------|-------------------------------|
| 1:01 | 4 * 0.5 + 2 * 0.5 = 2 + 1 = 3 |
| 1:02 | 2 * 0.5 + 8 * 0.5 = 1 + 4 = 5 |
| 1:03 | 8 * 0.5 + 6 * 0.5 = 4 + 3 = 7 |

If many samples are received for a given interval, then they will each be weighted based on the
fraction of the interval they represent. When no previous sample exists, the value will be treated
as the average rate per second over the previous step. This behavior is important to avoid
under-counting the contribution from a previous interval. The example below shows what happens
if there is no previous or next sample:

```
                ┌─────────┐
                │    8    │
                │         │
                │         │                          ┌─────────┐
                │         │                          │    5    ├─────────┐
                │         │                          │         │    4    │
      ┌─────────┤         │           to        1    │         │         │
      │    2    │         │                ┌─────────┤         │         │
 ├─────────┼─────────┼─────────┤           ├─────────┼─────────┼─────────┤
1:00      1:01      1:02      1:03        1:00      1:01      1:02      1:03
```

Why perform weighted averaging for rates instead of the simpler last value approach used with
gauges? Because it gives us a better summary of what we actually know from the measurements
received. In practical terms:

* **Avoids dropping information if samples are more frequent than the step.** Suppose we have
  a 1 minute step, but data is actually getting reported every 10s. For this example, assume
  we get 1, 5, 90, 5, 4, and 2. The last value normalization used with Gauges would end up
  with a value of 2. The rate normalization will give 17.833. Each value is a rate per second,
  so if you take the `(1 + 5 + 90 + 5 + 4 + 2) * 10 = 1070` actual events measured during the
  interval. That is equivalent to `17.833 * 60` indicating we have an accurate average rate
  for the step size.
* **Avoids skewing the data causing misleading spikes or drops in the aggregates.** Using Atlas
  you will typically be looking at an aggregate of time series rather than an individual time
  series that was reported. With last value it can have the effect of skewing samples to a later
  interval. Suppose the client is reporting once a minute at 5s after the minute. That value
  indicates more about the previous interval than it does the current one. During traffic
  transitions, such as moving traffic over to a new cluster or even some auto-scaling events,
  differences in this skew can result in the appearance of a drop because there will be many
  new time series getting reported with a delayed start. For existing time series it is still
  skewed, but tends to be less noticeable. The weighted averaging avoids these problems for
  the most part.

## Counter

Counter is similar to rate, except that the value reported is monotonically increasing and will
be converted to a rate by the backend. The conversion is done by computing the delta between the
current sample and the previous sample and dividing by the time between the samples. After that
it is the same as a [rate](#rate).

Note, that unless the input is a montonically increasing counter it is generally better to have
the client perform rate conversion. Since, the starting value is unknown, at least two samples
must be received before the first delta can be computed. This means that new time series relying
on counter type will be delayed by one interval.
