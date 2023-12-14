@@@ atlas-signature
Duration
TimeSeriesExpr
-->
TimeSeriesExpr
@@@

!!! warning
    Note that there is a deprecated `List[Duration]` variant that only modifes the presentation
    at the end. It cannot be used along with math operations.

Shift the time frame to use when fetching the data. This is used to look at a previous
interval as a point of reference, e.g., day-over-day or week-over-week. Offset cannot be
used with streaming execution of the query, consider using the [delay](delay.md) operator
for short intervals to detect a change.

Examples:

@@@ atlas-example { hilite=:offset }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,1w,:offset
Combined: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,:dup,1w,:offset
@@@

@@@ atlas-example { hilite=:offset }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,PT1H,:offset
Combined: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=name,sps,:eq,(,name,),:by,:dup,PT1H,:offset
@@@
