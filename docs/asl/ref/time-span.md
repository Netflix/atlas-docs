@@@ atlas-signature
e: String
s: String
-->
TimeSeriesExpr
@@@

Generates a signal line based on the specified time range. The line will be 1
within the range and 0 for all other times. The format of the start and end times
is the same as the start and end [time parameters](../../api/time-parameters.md) on the Graph
API. If the time zone is not explicitly specified, then the value from the `tz`
variable will get used. The default value for the `tz` variable is the primary
time zone used for the graph.

The following named times are supported for time spans:

Name     | Description                                                 |
----------|-------------------------------------------------------------|
gs       | Graph start time.                                           |
ge       | Graph end time.                                             |
s        | Start time for the span, can only be used for the end time. |
e        | End time for the span, can only be used for the start time. |
now      | Current time.                                               |
epoch    | January 1, 1970 UTC.                                        |

Since: 1.6

Example:

@@@ atlas-example { hilite=:time-span }
Relative: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=e-30m,ge,:time-span
Absolute: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=2014-02-20T13:00,s%2B30m,:time-span
@@@