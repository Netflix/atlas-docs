## Summary

1. Names
    * Describe the measurement being collected
    * Use short prefixes for categorization (max 2 levels)
    * Use camelCase
    * Static - no dynamic content
    * Succinct - avoid long names
2. Tags
    * Should be used for dimensional filtering
    * Be careful about combinatorial explosion and cardinality
    * Tag combinations should be stable over time
    * Tag keys should be static
    * Use `id` to distinguish between instances
3. Query Design
    * Avoid the need for regex and expensive pattern matching
    * Design for simple queries with incremental drill-down
    * Support exact matches and simple filters
4. Use Base Units

## Names

### Describe the Measurement

Names should clearly describe what is being measured. A good name allows someone to understand the
metric without needing additional context.

### Use Short Prefixes for Categorization

Common names should use short prefixes to broadly categorize metrics, for example `ipc.server.call`
or `jvm.gc.pause`. The prefix should generally have no more than 2 levels to keep names succinct.
This is not a package hierarchy like in Java - it's simply a way to group related metrics.

Examples of good prefixes:

* `ipc.*` for inter-process communication metrics
* `jvm.*` for Java Virtual Machine metrics
* `db.*` for database metrics

The prefix provides just enough context to understand the broad category and perhaps a sub-category,
while the rest of the name specifies the actual measurement. Remember that metrics will already be
scoped by other dimensions like application name, instance, etc., so the name itself should focus
on describing the measurement rather than providing extensive context. Avoid unnecessary boiler
plate like `com.netflix.*`.

### Use camelCase

For segments within a name, use camel case to distinguish words if needed. For example
`jvm.gc.concurrentPhaseTime`.

The exception to this rule is where there is an established common case. For example, with Amazon
regions, it is preferred to use `us-east-1` rather than `usEast1` as it is the more common form.

### Static

There should not be any dynamic content in a metric name, such as `requests.$APP_NAME`. Metric names
and tag keys are how users interact with the data, and dynamic values make them difficult to use.
Dynamic information is better suited for tag values.

### Succinct

Long names should be avoided. In many cases, long names are the result of combining many pieces of
information together into a single string. In this case, consider either discarding information
that is not useful or encoding the information in tag values. Shorter names are easier to read,
type, and view when working with the data.

## Tags

Tags should be used for dimensional filtering - they allow data to be filtered into subsets by
values of interest. Using tags as a namespace mechanism is discouraged.

As a general rule, it should be possible to use the name as a pivot. If only the name is selected,
then the user should be able to use other dimensions to filter the data and successfully reason
about the aggregate value being shown.

### Cardinality Considerations

**Keep combinatorial complexity in mind.** The full combination of tags creates unique time series,
and each combination consumes storage and processing resources. Tag combinations should be stable
over time to avoid constantly creating new time series.

Consider the cardinality impact:

* A metric with 3 tag keys, each with 10 possible values = 1,000 potential time series
* A metric with 5 tag keys, each with 10 possible values = 100,000 potential time series

Guidelines for managing cardinality:

* **Limit high-cardinality dimensions.** Avoid tags with unbounded or very large value sets
* **Use stable identifiers.** Tag values should remain consistent over time

### Design for Simple Queries

**Avoid regex and expensive pattern matching.** Design metric names and tag structures so they can
be queried simply and allow users to incrementally drill into the data. This improves both query
performance and user experience.

Good query patterns:

* `name,threadpool.size,:eq` - exact match on name
* `name,threadpool.size,:eq,id,server-requests,:eq,:and` - add exact tag filter
* `name,threadpool.*,:re` - simple prefix pattern (use sparingly)

Avoid patterns that require expensive operations:

* Complex regex patterns that must scan many metric names
* Queries that require examining all tag combinations to find matches
* Dynamic name construction that makes direct queries impossible

Design principle: Users should be able to start with a broad query and progressively add filters
to narrow down to the specific data they need.

As a concrete example, suppose we have two metrics:

1. The number of threads currently in a thread pool.
2. The number of rows in a database table.

#### Discouraged Approach

```java
Id poolSize = registry.createId("size")
  .withTag("class", "ThreadPool")
  .withTag("id", "server-requests");

Id poolSize = registry.createId("size")
  .withTag("class", "Database")
  .withTag("table", "users");
```

In this approach, if you select the name `size`, then it will match both the `ThreadPool` and
`Database` classes. This results in a value that is an aggregate of the number of threads and the
number of items in a database, which has no meaning.

#### Recommended Approach

```java
Id poolSize = registry.createId("threadpool.size")
  .withTag("id", "server-requests");

Id poolSize = registry.createId("db.size")
  .withTag("table", "users");
```

This variation provides enough context in the name so that the meaning is more apparent and you can
successfully reason about the values. For example, if you select `threadpool.size`, then you can
see the total number of threads in all pools. You can then group by or select an `id` to further
filter the data to a subset in which you have an interest.

This approach also supports simple queries without regex patterns:

* `name,threadpool.size,:eq` gives you all thread pool sizes
* `name,db.size,:eq` gives you all database sizes
* `name,threadpool.size,:eq,id,server-requests,:eq,:and` drills down to a specific pool

## Use Base Units

**Keep measurements in base units, whenever and wherever possible.**

It is best to have timers in `seconds`, disk sizes in `bytes`, and network rates in `bytes/second`.
This allows any International System of Units (SI) prefixes applied to [tick labels] on a graph to
have an obvious meaning, such as:

* `1 m` meaning `1 millisecond`, as opposed to `1 milli-millisecond`, for timers.
* `1 k` meaning `1 kilobyte`, as opposed to `1 kilo-megabyte`, for disk sizes.
* `1 M` meaning `1 megabyte/second`, as opposed to `1 mega-kilobyte`, for network rates.

Atlas automatically applies tick labels to the Y-axis of the graph, in order to accurately report the
magnitude of values, while keeping them within the view window.

Some meters in some clients, such as [Java Timers], will automatically constrain values to base units
in their implementations.

[tick labels]: ../api/graph/tick.md
[Java Timers]: ../spectator/lang/java/meters/timer.md#units
