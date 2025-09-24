The following tick (Y axis numeric labels) modes are supported:

* [decimal](#decimal)
* [binary](#binary)
* [duration](#duration)
* [off](#off)

## Decimal

This is the default mode. Y-axis tick labels will be formatted using the
[metric prefix](https://en.wikipedia.org/wiki/Metric_prefix) to indicate the magnitude for
values that are greater than one thousand or less than one.

@@@ atlas-uri { hilite=tick_labels }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=decimal
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=decimal
@@@

Really large values will fallback to scientific notation, e.g.:

@@@ atlas-uri { hilite=tick_labels }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,1e180,:mul&s=e-1w&tick_labels=decimal
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by,1e180,:mul&s=e-1w&tick_labels=decimal
@@@

## Binary

For values such as memory sizes it is sometimes more convenient to view the label using a power
of 1024 rather than a power of 1000. If the tick label mode is set to `binary`, then the
IEC [binary prefix](https://en.wikipedia.org/wiki/Binary_prefix) will be used.

@@@ atlas-uri { hilite=tick_labels }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=binary
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=binary
@@@

## Duration

Since 1.7.1.

Useful for timers or percentiles that measure latency, provides ticks with time unit suffix.

@@@ atlas-uri { hilite=tick_labels }
/api/v1/graph?e=2012-01-01T00:00&q=name,requestLatency,:eq,nf.node,wii-node,:eq,:and&tick_labels=duration
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,requestLatency,:eq,nf.node,wii-node,:eq,:and&tick_labels=duration
@@@

## Off

For presentations or sharing it is sometimes useful to [anonymize](anonymization.md) the chart. One
way of doing that is to disable the Y-axis labels by setting the tick label mode to `off`.

@@@ atlas-uri { hilite=tick_labels }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=off
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=off
@@@

## Offset Labels

In situations where a graph has very small changes in value that generate a significant number
of digits per tick, ticks may be labeled with offsets in order to fit the labels in
the layout. A base value is displayed at the bottom of the axis and positive
or negative offsets from the base displayed next to the ticks.

For example, if the amount of disk space used varies by 1 byte occasionally, the ticks
will be labeled by in increments of `+1.0`.

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&ylabel=bytes&q=hourOfDay,:time,6e10,:const,5,:sub,:add,disk bytes used,:legend
@@@

!!! note
    It is possible for queries spanning different data sources to display offset labels due
    to differing schemes used to encode floating point values.

If offsets are not desirable, try adjusting the y [axis bounds].

[axis bounds]: axis-bounds.md