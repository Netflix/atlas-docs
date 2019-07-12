# Counter

A Counter is used to measure the rate at which some event is occurring. Considering a simple 
queue, Counters could be used to measure things like the rate at which items are being inserted
and removed.

Counters are reported to the backend as a rate-per-second.

In Atlas, the `:per-step` operator can be used to convert them back into a value-per-step on a
graph.

## Languages

### First-Class Support

* [Java](../../lang/java/meters/counter.md)
* [Node.js](../../lang/nodejs/meters/counter.md)

### Experimental Support

* [C++](../../lang/cpp/meters/counter.md)
* [Go](../../lang/go/meters/counter.md)
* [Python](../../lang/py/meters/counter.md)
* [Ruby](../../lang/rb/meters/counter.md)
