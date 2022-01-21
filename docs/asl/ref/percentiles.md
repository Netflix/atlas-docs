@@@ atlas-signature
percentiles: List
Query
-->
TimeSeriesExpr
@@@

Estimate percentiles for a timer or distribution summary. The data must have been
published appropriately to allow the approximation. If using
[spectator], then see [PercentileTimer] and [PercentileDistributionSummary] helper classes.

[spectator]: ../../spectator/index.md
[PercentileTimer]: https://www.javadoc.io/doc/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/histogram/PercentileTimer.html
[PercentileDistributionSummary]: https://www.javadoc.io/doc/com.netflix.spectator/spectator-api/latest/com/netflix/spectator/api/histogram/PercentileDistributionSummary.html

The percentile values can be shown in the legend using `$percentile`.

Since: 1.5.0 (first in 1.5.0-rc.4)

@@@ atlas-example { hilite=:percentiles }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq,(,25,50,90,),:percentiles
@@@