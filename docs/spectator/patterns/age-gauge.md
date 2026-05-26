# Age Gauge

An Age Gauge reports the time in seconds since some event last occurred successfully.
It is a use of a [Gauge](../core/meters/gauge.md) where the value reported is computed
as `now - lastSuccessTimestamp` on each reporting interval.

The primary use case is the **Time Since Last Success** alerting pattern: alert when a
periodic job, heartbeat, or freshness signal stops advancing.

## Lifecycle

Age Gauges are long-lived — once set they continue reporting indefinitely until the
process is restarted or the gauge is explicitly removed. For spectatord-backed clients,
spectatord enforces a per-process limit (default `1000`, tunable via `--age_gauge_limit`)
to prevent leaks. To remove or replace one, use the
[SpectatorD admin server](../agent/usage.md#admin-server).

## Languages

* [C++](../lang/cpp/meters/age-gauge.md)
* [Go](../lang/go/meters/age-gauge.md)
* [Java](../lang/java/meters/age-gauge.md)
* [Node.js](../lang/nodejs/meters/age-gauge.md)
* [Python](../lang/py/meters/age-gauge.md)
