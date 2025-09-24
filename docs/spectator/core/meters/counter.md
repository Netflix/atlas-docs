# Counter

A Counter is used to measure the rate at which some event is occurring. Considering a simple
queue, Counters could be used to measure things like the rate at which items are being inserted
and removed.

Counters are reported to the backend as a rate-per-second. This makes it much easier
to reason about the measurement and allows for aggregating the counter across instances.

In Atlas, the `:per-step` operator can be used to convert them back into a count-per-step on a
graph.

!!! Note
    For high performance code, such as incrementing in a tight loop that lasts less than a
    reporting interval, increment a local variable and add the final value to the counter after
    the loop has completed.

## Languages

### First-Class Support

* [C++](../../lang/cpp/usage.md)
* [Go](../../lang/go/usage.md)
* [Java](../../lang/java/meters/counter.md)
* [Node.js](../../lang/nodejs/meters/counter.md)
* [Python](../../lang/py/meters/counter.md)

### Best-Effort Support

* Rust (internal library)
