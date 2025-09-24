@@@ atlas-signature
ordering: String
expr: TimeSeriesExpr
-->
StyleExpr
@@@

Specify the sort order to use when [:sort](sort.md) is applied to time series results.
This controls whether series appear in ascending or descending order based on the sort
criteria. The order setting affects the visual arrangement of lines in legends and
the stacking order for area charts.

## Parameters

* **expr**: The time series expression to apply ordering to
* **ordering**: Sort direction - either `asc` (ascending, default) or `desc` (descending)

## Supported Values

* `asc` - Ascending order (smallest to largest)
* `desc` - Descending order (largest to smallest)

If no order is specified, `asc` is used by default.

## Examples

Default ascending order when sorting by max:

@@@ atlas-example { hilite=:order }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,max,:sort
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,max,:sort,asc,:order
@@@

Changing to descending order (highest values first):

@@@ atlas-example { hilite=:order }
Before: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,max,:sort
After: /api/v1/graph?w=200&h=125&s=e-3h&e=2014-02-20T15:01&tz=US/Pacific&q=name,sps,:eq,:sum,(,nf.cluster,),:by,max,:sort,desc,:order
@@@

## Related Operations

* [:sort](sort.md) - Sort time series (order specifies direction)
* [:by](by.md) - Group data for sorting
* [:limit](limit.md) - Limit results after sorting

Since: 1.5