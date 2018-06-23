
# dist-avg

## Signature

`Query -- TimeSeriesExpr`

## Summary

Compute standard deviation for [timers](http://netflix.github.io/spectator/en/latest/intro/timer/)
and [distribution summaries](http://netflix.github.io/spectator/en/latest/intro/dist-summary/).

## Example

@@@ atlas-example
Before: /api/v1/graph?q=name,playback.startLatency,:eq
 After: /api/v1/graph?q=name,playback.startLatency,:eq,:dist-avg
@@@
