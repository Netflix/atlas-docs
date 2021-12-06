@@@ atlas-signature
TimeSeriesExpr
percentiles: List
-->
TimeSeriesExpr
@@@

Estimate percentiles for a timer or distribution summary. The data must have been
published appropriately to allow the approximation. If using
[spectator](http://netflix.github.io/spectator/en/latest/), then see
[PercentileTimer](http://netflix.github.io/spectator/en/latest/javadoc/spectator-api/com/netflix/spectator/api/histogram/PercentileTimer.html)
and
[PercentileDistributionSummary](http://netflix.github.io/spectator/en/latest/javadoc/spectator-api/com/netflix/spectator/api/histogram/PercentileDistributionSummary.html)
helper classes.

The percentile values can be shown in the legend using `$percentile`.

Since: 1.5.0 (first in 1.5.0-rc.4)

@@@ atlas-example { hilite=:percentiles }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=name,requestLatency,:eq,(,25,50,90,),:percentiles
@@@