@@@ atlas-signature
endTime: String
startTime: String
-->
TimeSeriesExpr
@@@

Generate a signal time series that is 1 within a specified time range and 0 outside it.
This creates boolean-like indicators for specific time periods, useful for marking events,
maintenance windows, or other time-based conditions in visualizations and alerting.

## Parameters

* **startTime**: Beginning of the time span (using [time parameter](../../api/time-parameters.md) format)
* **endTime**: End of the time span (using [time parameter](../../api/time-parameters.md) format)

## Time Formats

Time parameters support both absolute and relative formats, following the same syntax as
the Graph API [time parameters](../../api/time-parameters.md). Time zone handling uses the
`tz` variable or defaults to the graph's primary time zone.

### Named Time References

| Name   | Description                                                   |
|--------|---------------------------------------------------------------|
| `gs`   | Graph start time                                              |
| `ge`   | Graph end time                                                |
| `s`    | Start time for the span (can only be used for the end time)  |
| `e`    | End time for the span (can only be used for the start time)  |
| `now`  | Current time                                                  |
| `epoch`| January 1, 1970 UTC                                          |

## Examples

Relative time span (30 minutes before graph end):

@@@ atlas-example { hilite=:time-span }
Relative: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=e-30m,ge,:time-span
@@@

Absolute time span (specific 30-minute window):

@@@ atlas-example { hilite=:time-span }
Absolute: /api/v1/graph?w=200&h=125&s=e-3h&e=2012-01-01T07:00&tz=UTC&q=2014-02-20T13:00,s%2B30m,:time-span
@@@

## Signal Output

The operator produces a signal time series where:
- **Value 1**: Time falls within the specified range [startTime, endTime]
- **Value 0**: Time falls outside the specified range
- This creates a boolean-like signal suitable for logical operations

## Related Operations

* [:vspan](vspan.md) - Visual highlighting of time periods (combines well with :time-span)

## See Also

* [Time Parameters](../../api/time-parameters.md) - Comprehensive time format documentation

Since: 1.6