The following tick label modes are supported:

* [decimal](#decimal)
* [binary](#binary)
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

## Off

For presentations or sharing it is sometimes useful to [anonymize](anonymization.md) the chart. One
way of doing that is to disable the Y-axis labels by setting the tick label mode to `off`.

@@@ atlas-uri { hilite=tick_labels }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=off
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T00:00&q=name,sps,:eq,(,nf.cluster,),:by&s=e-1w&tick_labels=off
@@@
