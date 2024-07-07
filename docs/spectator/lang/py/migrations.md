## Migrating from 0.1.X to 0.2.X

* This library no longer publishes directly to the Atlas backends. It now publishes to the
[SpectatorD] sidecar which is bundled with all standard AMIs and containers. If you must
have the previous direct publishing behavior, because SpectatorD is not yet available on the
platform where your code runs, then you can pin to version `0.1.18`.
* The internal Netflix configuration companion library is no longer required and this dependency
may be dropped from your project.
* The API surface area remains unchanged to avoid breaking library consumers, and standard uses of
`GlobalRegistry` helper methods for publishing metrics continue to work as expected. Several helper
methods on meter classes are now no-ops, always returning values such as `0` or `nan`. If you want
to write tests to validate metrics publication, take a look at the tests in this library for a few
examples of how that can be done. The core idea is to capture the lines which will be written out
to SpectatorD.
* Replace uses of `PercentileDistributionSummary` with direct use of the Registry
`pct_distribution_summary` method.

    ```
    # before
    from spectator import GlobalRegistry
    from spectator.histogram import PercentileDistributionSummary
    
    d = PercentileDistributionSummary(GlobalRegistry, "server.requestSize")
    d.record(10)
    ```

    ```
    # after
    from spectator import GlobalRegistry
    
    GlobalRegistry.pct_distribution_summary("server.requestSize").record(10)
    ```

* Replace uses of `PercentileTimer` with direct use of the Registry `pct_timer` method.

    ```
    # before
    from spectator import GlobalRegistry
    from spectator.histogram import PercentileTimer
    
    t = PercentileTimer(GlobalRegistry, "server.requestSize")
    t.record(0.01)
    ```
    
    ```
    # after
    from spectator import GlobalRegistry
    
    GlobalRegistry.pct_timer("server.requestSize").record(0.1)
    ```

* Implemented new meter types supported by [SpectatorD]: `age_gauge`, `max_gauge` and
`monotonic_counter`. See the SpectatorD documentation or the class docstrings for
more details.
