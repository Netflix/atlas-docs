Atlas has two core data types at its foundation: **rates** and **gauges**. These types determine
how data is normalized and aggregated, but end users typically work with higher-level **conceptual
types** like counters, timers, and distribution summaries that are provided by reporting libraries
like Spectator.

Understanding conceptual types is important for:

* **Querying**: Selecting time series of a specific type
* **Visualization**: Presenting data appropriately in UIs and dashboards
* **Analysis**: Applying the correct operations and aggregations

## Core vs Conceptual Types

### Core Types

Atlas's backend operates on two fundamental types:

* **Rates**: Normalized to a rate per second
* **Gauges**: Sampled values reported as-is

### Conceptual Types

Conceptual types are higher-level abstractions that map to one or more time series. They use the
`statistic` tag to differentiate between various components of the measurement. Common conceptual
types include:

* Counter
* Gauge
* Timer
* DistributionSummary
* LongTaskTimer
* IntervalCounter

## Type Mappings

### Counter

A counter tracks the rate at which events occur.

**Statistics:**

* `count`: Rate of events (events/second)

**Recommended aggregations:**

Use [:sum](ref/sum.md) for counters. Since the `count` statistic is often used for other
composite types like Timers and Distribution Summaries, it is advisable to have an explicit
restriction of `statistic,count,:eq` on the query to ensure it is only operating on the
counter aspect.

To determine the average rate per node, see [:node-avg](ref/node-avg.md) and
[:eureka-avg](ref/eureka-avg.md).

### Gauge

A gauge reports a sampled value at a specific point in time.

**Statistics:**

* `gauge`: Current value

**Recommended aggregations:**

Use [:avg](ref/avg.md) or [:max](ref/max.md) for gauges. A [:sum](ref/sum.md) aggregation is
sometimes appropriate, but depends on the value that was sampled.

### Timer

A timer measures the duration of events and provides statistics about the distribution of those
durations. All duration measurements are in seconds.

**Statistics:**

* Required
    * `totalTime`: Total time recorded (seconds/second)
    * `count`: Number of events recorded (events/second)
* Optional
    * `totalOfSquares`: Sum of squares of recorded durations (seconds²/second)
    * `max`: Maximum duration recorded in the interval (seconds)
    * `percentile`: Used for modeling the distribution to approximate percentiles

**Recommended aggregations:**

The supported aggregations depend on the available statistics. All timers must have the `totalTime`
and `count` statistics. When restricting to the `count` statistic it can be used like any other
counter. To compute the average time per recorded operation use the [:dist-avg](ref/dist-avg.md)
operator that computes `totalTime / count`.

The other statistics if present allow for additional aggregations on the data:

* `totalOfSquares`: Allows use of [:dist-stddev](ref/dist-stddev.md) to compute standard deviation
* `max`: Allows use of [:dist-max](ref/dist-max.md) to see the max recorded sample
* `percentile`: Allows use [:percentiles](ref/percentiles.md) to approximate percentiles

### Distribution Summary

A distribution summary tracks the distribution of events. It's similar to a timer but measures
arbitrary values rather than durations.

**Statistics:**

* Required
    * `totalAmount`: Total amount recorded (units/second)
    * `count`: Number of events recorded (events/second)
* Optional
    * `totalOfSquares`: Sum of squares of recorded amounts (units²/second)
    * `max`: Maximum amount recorded in the interval (units)
    * `percentile`: Used for modeling the distribution to approximate percentiles

**Recommended aggregations:**

The supported aggregations depend on the available statistics. All distribution summaries must have
the `totalAmount` and `count` statistics. When restricting to the `count` statistic it can be used
like any other counter. To compute the average amount per recorded operation use the
[:dist-avg](ref/dist-avg.md) operator that computes `totalAmount / count`.

The other statistics if present allow for additional aggregations on the data:

* `totalOfSquares`: Allows use of [:dist-stddev](ref/dist-stddev.md) to compute standard deviation
* `max`: Allows use of [:dist-max](ref/dist-max.md) to see the max recorded sample
* `percentile`: Allows use [:percentiles](ref/percentiles.md) to approximate percentiles

### Long Task Timer

A long task timer measures the duration of in-progress tasks. Unlike regular timers, it reports
the current state rather than completed events.

**Statistics:**

* `activeTasks`: Number of tasks currently running (gauge)
* `duration`: Total duration of all active tasks (gauge, seconds)

**Recommended aggregations:**

It should be used by restricting to either the `activeTasks` or `duration` statistic and using
the [:max](ref/max.md) aggregation.

### Interval Counter

An interval counter reports a count over an interval rather than a rate. It's useful for reporting
values that represent totals over a polling interval.

**Statistics:**

* `count`: Rate of events (events/second)
* `duration`: Total duration since the last increment (gauge, seconds)

**Recommended aggregations:**

It should be used as a counter by restricting to the `count` statistic, or by restricting to
the `duration` statistic and using the [:max](ref/max.md) aggregation.

## Determining Types

To determine the conceptual type, look at the available statistics:

| Statistic | Conceptual Type(s) |
|----------------|-------------------|
| `activeTasks`, `duration` | LongTaskTimer |
| `count` | Counter |
| `count`, `duration` | IntervalCounter |
| `count`, `totalAmount` | DistributionSummary |
| `count`, `totalTime` | Timer |
| `gauge` | Gauge |

For Timer and DistributionSummary, the following statistics indicate additional aggregation
capabilities:

| Statistic | Capabilities |
|----------------|-------------------|
| `totalOfSquares` | Enables [:dist-stddev](ref/dist-stddev.md) |
| `max` | Enables [:dist-max](ref/dist-max.md) |
| `percentile` | Enables [:percentiles](ref/percentiles.md) |

If a mix of these are present, then the query is too broad and is matching multiple metrics
of different types.