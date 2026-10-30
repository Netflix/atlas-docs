# Distinct Count Sketch

A distinct count sketch estimates the number of distinct values seen during a reporting interval,
for example unique users, device ids, or source ips. The values themselves are never published,
only what is needed to estimate how many of them were distinct, and the metric costs the same
whether there are ten distinct values or ten million.

Call `record()` with a value, which may be an `int`, `str`, `bytes`, or `bytearray`:

```python
from spectator import Registry

registry = Registry()
registry.distinct_count_sketch("server.uniqueUsers").record(user_id)

unique_users = registry.new_id("server.uniqueUsers")
registry.distinct_count_sketch_with_id(unique_users).record(user_id)
```

Then query the number of distinct users active in each interval with
[:approx-distinct](../../../../asl/ref/approx-distinct.md):

```
name,server.uniqueUsers,:eq,:approx-distinct
```

The estimate covers everything the query matches, so a user active on several instances counts
once rather than once per instance. Sketches recorded by the Python, Go, and Java clients merge
correctly, so the same metric can be published from services written in different languages.

## Recording Values

Equal values have to be recorded the same way to be counted once, so normalize the input
consistently at every call site: record either the raw ip string or the parsed bytes, not a mix
of the two.

Unsupported types, including `bool`, and integers that do not fit in 64 bits are logged and
skipped rather than raising an exception.

This meter requires a version of [SpectatorD](../../../agent/usage.md) with support for the
distinct count sketch. Older versions silently drop the values.

## Cost

**A distinct count sketch is much more expensive than a plain counter.** One sketch costs 64
time series per instance, and that is multiplied by every other tag on the id. Be as diligent
about the dimensions on a sketch as for a percentile timer, and ensure that they have a small
bounded cardinality.

## Accuracy

The result is an estimate, not an exact count. The relative standard error is roughly 13%, so
the value moves around a little from interval to interval even when the true count is steady.
Use it for the magnitude and the shape of a trend, not to read off an exact number.

## Querying

* [:approx-distinct] - distinct values in each interval
* [:approx-distinct-rolling] - distinct values over a trailing window
* [:approx-distinct-cumulative] - running count of the distinct values seen so far

[:approx-distinct]: ../../../../asl/ref/approx-distinct.md
[:approx-distinct-rolling]: ../../../../asl/ref/approx-distinct-rolling.md
[:approx-distinct-cumulative]: ../../../../asl/ref/approx-distinct-cumulative.md
