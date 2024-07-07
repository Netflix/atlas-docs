Simple library for instrumenting code to record dimensional time series data.

At a minimum, you need to:

1. Understand core concepts.

    * [Time Series](../concepts/time-series.md)
    * [Normalization](../concepts/normalization.md)
    * [Naming](../concepts/naming.md)
    * [Clock](core/clock.md)

1. Install the metrics agent.

    * [SpectatorD](agent/usage.md)

1. Install the language-specific library and configuration bindings, where available.

    * Support Class Descriptions
        * [Language Overview](lang/overview.md)
    * First-Class Support
        * [C++](lang/cpp/usage.md)
        * [Go](lang/go/usage.md)
        * [Java](lang/java/usage.md)
        * [Node.js](lang/nodejs/usage.md)
        * [Python](lang/py/usage.md)
    * Best-Effort Support
        * Rust (internal library)   

1. Instrument some code, referring to the core usage guides on the following meter types:

    * [Counters](core/meters/counter.md)
    * [Distribution Summaries](core/meters/dist-summary.md)
    * [Gauges](core/meters/gauge.md)
    * [Percentile Timers](patterns/percentile-timer.md)
    * [Timers](core/meters/timer.md)

After you are more familiar with the library and need assistance with more advanced topics,
see the Patterns section on the left.
