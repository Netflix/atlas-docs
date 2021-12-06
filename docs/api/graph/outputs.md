The following output formats are supported by default for [graphing](Graph):

* [png](#png)
* [csv](#csv)
* [txt](#txt)
* [json](#json)
* [std.json](#stdjson)
* [stats.json](#statsjson)

## png

This is the default and creates a PNG image for the graph. The mime type is `image/png`.

@@@ atlas-uri { hilite=format%3Dpng }
/api/v1/graph?e=2012-01-01T09:00&format=png&q=hourOfDay,:time,minuteOfHour,:time,NaN&s=e-3m&tz=UTC
@@@

@@@ atlas-graph { show-expr=false }
/api/v1/graph?e=2012-01-01T09:00&format=png&q=hourOfDay,:time,minuteOfHour,:time,NaN&s=e-3m&tz=UTC
@@@

## csv

Comma separated value output. The mime type is `text/csv`.

@@@ atlas-uri { hilite=format%3Dcsv }
/api/v1/graph?e=2012-01-01T09:00&format=csv&q=hourOfDay,:time,minuteOfHour,:time,NaN&s=e-5m&tz=UTC
@@@

```
"timestamp","hourOfDay","minuteOfHour","NaN"
2012-01-01T08:56:00Z,8.000000,56.000000,NaN
2012-01-01T08:57:00Z,8.000000,57.000000,NaN
2012-01-01T08:58:00Z,8.000000,58.000000,NaN
2012-01-01T08:59:00Z,8.000000,59.000000,NaN
2012-01-01T09:00:00Z,9.000000,0.000000,NaN

```

## txt

Same as [csv](#csv) except that the separator is a tab character instead of a comma. The mime
type will be `text/plain` so it is more likely to render directly in the browser rather than
trigger a download.

@@@ atlas-uri { hilite=format%3Dtxt }
/api/v1/graph?e=2012-01-01T09:00&format=txt&q=hourOfDay,:time,minuteOfHour,:time,NaN&s=e-5m&tz=UTC
@@@

```
"timestamp"	"hourOfDay"	"minuteOfHour"	"NaN"
2012-01-01T08:56:00Z	8.000000	56.000000	NaN
2012-01-01T08:57:00Z	8.000000	57.000000	NaN
2012-01-01T08:58:00Z	8.000000	58.000000	NaN
2012-01-01T08:59:00Z	8.000000	59.000000	NaN
2012-01-01T09:00:00Z	9.000000	0.000000	NaN

```

## json

JSON output representing the data. Note that it is not [standard json](http://json.org) as numeric
values like `NaN` will not get quoted.

@@@ atlas-uri { hilite=format%3Djson }
/api/v1/graph?e=2012-01-01T09:00&format=json&q=hourOfDay,:time,minuteOfHour,:time,NaN&s=e-5m&tz=UTC
@@@

```
{
  "start" : 1325408160000,
  "step" : 60000,
  "legend" : [ "hourOfDay", "minuteOfHour", "NaN" ],
  "metrics" : [ {
    "atlas.offset" : "0w",
    "name" : "hourOfDay"
  }, {
    "atlas.offset" : "0w",
    "name" : "minuteOfHour"
  }, {
    "atlas.offset" : "0w",
    "name" : "NaN"
  } ],
  "values" : [ [ 8.0, 56.0, NaN ], [ 8.0, 57.0, NaN ], [ 8.0, 58.0, NaN ], [ 8.0, 59.0, NaN ], [ 9.0, 0.0, NaN ] ],
  "notices" : [ ]
}
```

## std.json

Same as [json](#json) except that numeric values which are not recognized by
[standard json](http://json.org) will be quoted. The mime type is `application/json`.

@@@ atlas-uri { hilite=format%3Dstd.json }
/api/v1/graph?e=2012-01-01T09:00&format=std.json&q=hourOfDay,:time,minuteOfHour,:time,NaN&s=e-5m&tz=UTC
@@@

```
{
  "start" : 1325408160000,
  "step" : 60000,
  "legend" : [ "hourOfDay", "minuteOfHour", "NaN" ],
  "metrics" : [ {
    "atlas.offset" : "0w",
    "name" : "hourOfDay"
  }, {
    "atlas.offset" : "0w",
    "name" : "minuteOfHour"
  }, {
    "atlas.offset" : "0w",
    "name" : "NaN"
  } ],
  "values" : [ [ 8.0, 56.0, "NaN" ], [ 8.0, 57.0, "NaN" ], [ 8.0, 58.0, "NaN" ], [ 8.0, 59.0, "NaN" ], [ 9.0, 0.0, "NaN" ] ],
  "notices" : [ ]
}
```

## stats.json

Provides the summary stats for each line, but not all of the data points. The mime type is
`application/json`.

@@@ atlas-uri { hilite=format%3Dstats.json }
/api/v1/graph?e=2012-01-01T09:00&format=stats.json&q=hourOfDay,:time,minuteOfHour,:time,NaN&s=e-5m&tz=UTC
@@@

```
{
  "start" : 1325408160000,
  "end" : 1325408460000,
  "step" : 60000,
  "legend" : [ "hourOfDay", "minuteOfHour", "NaN" ],
  "metrics" : [ {
    "atlas.offset" : "0w",
    "name" : "hourOfDay"
  }, {
    "atlas.offset" : "0w",
    "name" : "minuteOfHour"
  }, {
    "atlas.offset" : "0w",
    "name" : "NaN"
  } ],
  "stats" : [ {
    "count" : 5,
    "avg" : 8.2,
    "total" : 41.0,
    "max" : 9.0,
    "min" : 8.0,
    "last" : 9.0
  }, {
    "count" : 5,
    "avg" : 46.0,
    "total" : 230.0,
    "max" : 59.0,
    "min" : 0.0,
    "last" : 0.0
  }, {
    "count" : 0,
    "avg" : NaN,
    "total" : NaN,
    "max" : NaN,
    "min" : NaN,
    "last" : NaN
  } ],
  "notices" : [ ]
}
```
