# Distinct Count Sketch

`DistinctCountSketch` estimates the number of distinct values seen during a reporting interval,
for example unique users, device ids, or source ips. Counting distinct values exactly means
remembering every value seen, which does not fit in a metric, so the sketch trades exactness for
a fixed cost: recording a value is constant time and allocation free, and the metric costs the
same whether there are ten distinct values or ten million.

Example:

```java
public class WebServer {

  private final DistinctCountSketch uniqueUsers;

  @Inject
  public WebServer(Registry registry) {
    uniqueUsers = DistinctCountSketch.get(registry, registry.createId("server.uniqueUsers"));
  }

  public Response handleRequest(Request req) {
    uniqueUsers.record(req.getUserId());
    return doSomething(req);
  }
}
```

Then query the number of distinct users active in each interval:

```
name,server.uniqueUsers,:eq,:approx-distinct
```

The estimate covers everything the query matches, so a user active on several instances counts
once rather than once per instance. Nothing needs to be done at record time to make that work.

## Recording Values

There are overloads for the common shapes of an id:

```java
sketch.record(userId);          // long, such as a numeric id
sketch.record(sessionId);       // CharSequence, such as a string id or ip address
sketch.record(rawBytes);        // byte[]
```

The values themselves are never published, only what is needed to estimate how many of them were
distinct. Equal values have to be recorded the same way to be counted once, so normalize the
input consistently at every call site: record either the raw ip string or the parsed bytes, not
a mix of the two.

## Additional Dimensions

Use the builder to add tags, including ones that vary at the call site:

```java
DistinctCountSketch.builder(registry)
  .withName("server.uniqueUsers")
  .withTag("device", device)
  .build()
  .record(userId);
```

The estimate can then be broken out by that dimension at query time:

```
name,server.uniqueUsers,:eq,(,device,),:by,:approx-distinct
```

The grouped estimates only total the ungrouped estimate when a value can belong to just one
group. A user active on both a phone and a TV counts once overall, but once in each of those
groups.

## Cost

**A distinct count sketch is much more expensive than a plain counter.** One sketch costs 64
time series per instance, and that is multiplied by every other tag on the id. Be as diligent
about the dimensions on a sketch as for a percentile timer, and use a
[cardinality limiter](cardinality-limiter.md) for any tag value that is not strictly bounded.

## Accuracy

The result is an estimate, not an exact count. The relative standard error is roughly 13%, so
the value moves around a little from interval to interval even when the true count is steady, and
the precision is fixed rather than something to tune. Use it for the magnitude and the shape of a
trend, not to read off an exact number.

`sketch.cardinality()` estimates the distinct count for what was recorded into that instance,
which is useful in tests and local debugging. It says nothing about the fleet-wide count, which
is computed across all sources at query time.

## Querying

* [:approx-distinct] - distinct values in each interval
* [:approx-distinct-cumulative] - running count of the distinct values seen so far

[:approx-distinct]: ../../../../asl/ref/approx-distinct.md
[:approx-distinct-cumulative]: ../../../../asl/ref/approx-distinct-cumulative.md
