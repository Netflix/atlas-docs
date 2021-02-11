## Summary

1. Names
    * Describe the measurement being collected
    * Use camelCase
    * Static
    * Succinct
2. Tags
    * Should be used for dimensional filtering
    * Be careful about combinatorial explosion
    * Tag keys should be static
    * Use `id` to distinguish between instances
3. Use Base Units

## Names

### Describe the Measurement

### Use camelCase

The main goal here is to promote consistency, which makes it easier for users. The choice of
style is somewhat arbitrary, but camelCase was chosen because:

* Used by SNMP
* Used by Java
* It was commonly used at Netflix when the guideline was written

The exception to this rule is where there is an established common case. For example, with
Amazon regions, it is preferred to use `us-east-1` rather than `usEast1` as it is the more
common form.

### Static

There should not be any dynamic content in a metric name, such as `requests.$APP_NAME`. Metric
names and tag keys are how users interact with the data, and dynamic values make them difficult
to use. Dynamic information is better suited for tag values, such as `nf.app` or `status`. 

### Succinct

Long names should be avoided. In many cases, long names are the result of combining many pieces
of information together into a single string. In this case, consider either discarding information
that is not useful or encoding the information in tag values.  

## Tags

Historically, tags have been used to play one of two roles:

* **Dimensions.** This is the primary use of tags and this feature allows the data to be filtered
into subsets by values of interest.
* **Namespace.** Similar to packages in Java, this allows grouping related data. This type of usage
is discouraged.

As a general rule, it should be possible to use the name as a pivot. If only the name is selected,
then the user should be able to use other dimensions to filter the data and successfully reason
about the value being shown. 

As a concrete example, suppose we have two metrics:

1. The number of threads currently in a thread pool.
2. The number of rows in a database table.

### Discouraged Approach

```java
Id poolSize = registry.createId("size")
  .withTag("class", "ThreadPool")
  .withTag("id", "server-requests");
  
Id poolSize = registry.createId("size")
  .withTag("class", "Database")
  .withTag("table", "users");  
```

In this approach, if you select the name `size`, then it will match both the `ThreadPool` and
`Database` classes. This results in a value that is the an aggregate of the number of threads
and the number of items in a database, which has no meaning. 

### Recommended Approach

```java
Id poolSize = registry.createId("threadpool.size")
  .withTag("id", "server-requests");
  
Id poolSize = registry.createId("db.size")
  .withTag("table", "users");  
```

This variation provides enough context, so that if just the name is selected, the value can be
reasoned about and is at least potentially meaningful.

This variation provides enough context in the name so that the meaning is more apparent and you
can successfully reason about the values. For example, if you select `threadpool.size`, then you
can see the total number of threads in all pools. You can then group by or select an `id` to
further filter the data to a subset in which you have an interest.

## Use Base Units

Keep measurements in base units where possible. It is better to have all timers in seconds, disk
sizes in bytes, and network rates in bytes/second. This allows any SI unit prefixes applied to
tick labels on a graph to have an obvious meaning, such as 1k meaning 1 kilobyte, as opposed to
1 kilo-megabyte.
