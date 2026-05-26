Spectator client libraries are available in several languages. Outside of Java, the libraries are
intentionally minimal — they function as thin clients that send data to a local
[SpectatorD](../agent/usage.md) agent, which handles aggregation and reporting to Atlas. This keeps
the per-language footprint small and lets partners invested in each language drive idiomatic
implementations.

## First-Class Support

These libraries are fully-supported by the team and see wide use across Netflix. Issues are fixed
in a timely manner and updates are published regularly.

* [C++](cpp/usage.md)
* [Go](go/usage.md)
* [Java](java/usage.md)
* [Node.js](nodejs/usage.md)
* [Python](py/usage.md)

## Best-Effort Support

* Rust (internal library)

## Deprecated

* Ruby — the legacy `spectator-rb` client does not support SpectatorD and is no longer maintained.

## History

The original Spectator library was written in [Java](java/usage.md), with the first stable version
([0.35.0]) released on Jan 18, 2016. Other languages followed as the polyglot footprint at Netflix
grew.

[0.35.0]: https://github.com/Netflix/spectator/releases/tag/v0.35.0
