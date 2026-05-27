# Monotonic Counter

A Monotonic Counter is a use of a [Counter](../core/meters/counter.md) where the source
data is a **cumulative** value that only increases (e.g. bytes-sent on a network interface,
total tasks completed by a thread pool). The library samples successive absolute values and
computes the delta itself, reporting the per-second rate to the backend.

Use this when the underlying source is naturally monotonic and you don't have a hook to
increment a regular counter on each event. Common sources: OS counters, JMX counters, thread
pool stats, network interface counters.

A minimum of **two samples** is required before the first metric is reported, so there is a
slower time-to-first-data point than a standard counter.

## Numeric variants

* **Signed / double** — the default. Suitable when the source fits in a signed 64-bit
  integer or double and is not expected to overflow.
* **uint64** — required when reading from a source that uses unsigned 64-bit semantics
  (most OS-level interface counters), so that a wrap past `2^64 - 1` back to `0` is
  reported correctly as a positive delta rather than appearing as a backward jump.

Java is long-based and does not need a separate uint variant.

## Counter resets and wraparounds

When the polled value goes **down** between samples, the library cannot tell whether the
source was reset (e.g. process restart, JMX counter cleared) or wrapped past its numeric
limit. Behavior depends on the variant:

* **Signed / double** — drops the sample for that interval and uses the new value as the
  baseline for the next delta. The decrease itself is not reported; one interval's worth
  of activity is lost, then reporting resumes normally.
* **uint64** — computes the wrap delta `(2^64 - previous) + current` and reports that.
  spectatord additionally caps this: if the computed delta exceeds `2^63`, it is treated
  as an unexpected rollover (e.g. a real reset masquerading as a wrap) and `0` is
  reported instead.

If your source can legitimately reset, prefer a regular [Counter](../core/meters/counter.md)
with explicit `increment()` calls so each event is recorded individually.

## Languages

* C++: [signed](../lang/cpp/meters/monotonic-counter.md), [uint64](../lang/cpp/meters/monotonic-counter-uint.md)
* Go: [signed](../lang/go/meters/monotonic-counter.md), [uint64](../lang/go/meters/monotonic-counter-uint.md)
* [Java](../lang/java/meters/monotonic-counter.md)
* Node.js: [signed](../lang/nodejs/meters/monotonic-counter.md), [uint64](../lang/nodejs/meters/monotonic-counter-uint.md)
* Python: [signed](../lang/py/meters/monotonic-counter.md), [uint64](../lang/py/meters/monotonic-counter-uint.md)
