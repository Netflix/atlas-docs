
Less than or equal operator. There are two variants of the `:le` operator.

## Choosing

@@@ atlas-signature
v: String
k: String
-->
(k <= v): Query
@@@

This first variant is used for [choosing](../tutorial.md#choosing) the set of time series to
operate on. It selects time series that have a value for a key that is less than or equal
to a specified value. For example, consider the following query:

@@@ atlas-stacklang { hilite=:le }
/api/v1/graph?q=name,ssCpuSystem,:le
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the result set:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th>
  </thead>
  <tbody>
  <tr>
    <td>ssCpuUser</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuSystem</strong></td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr>
    <td>ssCpuUser</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuSystem</strong></td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td><strong>numRequests</strong></td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr>
    <td>ssCpuUser</td>
    <td>api</td>
    <td>i-0456</td>
  </tr>
  </tbody>
</table>

## Math

@@@ atlas-signature
ts2: TimeSeriesExpr
ts1: TimeSeriesExpr
-->
(ts1 <= ts2): TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a <= b)` where `a`
and `b` are the corresponding intervals in the input time series. For example:

| **Time** | **a** | **b** | **a <= b** |
|----------|-------|-------|-------------|
|  00:01   | 0.0   |  0.0  |  1.0        |
|  00:01   | 0.0   |  1.0  |  1.0        |
|  00:02   | 1.0   |  0.0  |  0.0        |
|  00:03   | 1.0   |  1.0  |  1.0        |
|  00:04   | 0.5   |  1.7  |  1.0        |

The result will be a [signal time series](../alerting-expressions.md#signal-line) that will
be `1.0` for intervals where the condition is true and `0.0` for intervals where it is false.

Example:

@@@ atlas-example { hilite=:le }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfHour,:time,hourOfDay,:time
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfHour,:time,hourOfDay,:time,:le
@@@

