# Time Series

A time series is a sequence of [data points](#data-point) reported at a consistent interval over
time. The time interval between successive data points is called the [step size](#step-size). In
Atlas, each time series is paired with metadata called [tags](#tags) that allow us to query and
group the data.

## Tags

A set of key value pairs associated with a [time series](#time-series). Each time series must have
at least one tag with a key of `name`. To make it more concrete, here is an example of a tag set
represented as a JSON object:

```json
{
  "name":       "server.requestCount",
  "status":     "200",
  "endpoint":   "api",
  "nf.app":     "fooserver",
  "nf.cluster": "fooserver-main",
  "nf.stack":   "main",
  "nf.region":  "us-east-1",
  "nf.zone":    "us-east-1c",
  "nf.node":    "i-12345678"
}
```

Usage of tags typically falls into two categories:

1. **Namespace.** These are tags necessary to qualify a name, so that it can be meaningfully
aggregated. Using the sample above, consider computing the sum of all metrics for application
`fooserver`. That number would be meaningless. Properly modelled data should try to make the
aggregates meaningful by selecting the `name`. The sum of all metrics with
`name = server.requestCount` is the overall request count for the service.
2. **Dimensions.** These are tags used to filter the data to a meaningful subset. They can be
used to see the number of successful requests across the cluster by querying for `status = 200`
or the number of requests for a single node by querying for `nf.node = i-12345678`. Most tags
should fall into this category.

When creating metrics, it is important to carefully think about how the data should be tagged. See
the [naming](naming.md) docs for more information.

## Metric

A metric is a specific quantity being measured, e.g., the number of requests received by a server.
In casual language about Atlas metric is often used interchangeably with
[time series](#time-series). A time series is one way to track a metric and is the method
supported by Atlas. In most cases there will be many time series for a given metric. Going back
to the example, request count would usually be tagged with additional dimensions such as status
and node. There is one time series for each distinct combination of tags, but conceptually it is
the same metric.

## Data Point

A data point is a triple consisting of tags, timestamp, and a value. It is important to understand
at a high level how data points correlate with the measurement. Consider requests hitting a
server, this would typically be measured using a
[counter](../spectator/core/meters/counter.md). Each time a request is
received the counter is incremented. There is not one data point per increment, a data point
represents the behavior over a span of time called the [step size](#step-size). The client library
will sample the counter once for each interval and report a single value.

Suppose that each circle in the diagram below represents a request:

```
1:00       1:01       1:02       1:03
 ├─●────●●●─┼──────────┼──●───────┤
```

There are 5 requests shown, 4 from 1:00 to 1:01, and 1 from 1:02 to 1:03. Assuming all requests
incremented the same time series, i.e. all other dimensions such as status code are the same, then
this would result in three data points. For counters values are always a rate per second, so for
a one minute step size the total number of requests would be divided by 60 seconds. So the values
stored would be:

| Time | Value           |
|------|-----------------|
| 1:01 | 4 / 60 = 0.0667 |
| 1:02 | 0 / 60 = 0.0000 |
| 1:03 | 1 / 60 = 0.0167 |

## Step Size

The amount of time between two successive data points in a [time series](#time-series). For Atlas
the datapoints will always be on even boundaries of the step size. If data is not reported on step
boundaries, it will get [normalized](normalization.md) to the boundary.
