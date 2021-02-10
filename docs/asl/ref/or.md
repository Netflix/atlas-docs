
There are two variants of the `:or` operator.

## Choosing

@@@ atlas-signature
q2: Query
q1: Query
-->
(q1 OR q2): Query
@@@

This first variant is used for [choosing](../tutorial.md#choosing) the set of time series to
operate on. It is a binary operator that matches if either of the sub-queries match. For example,
consider the following query:

@@@ atlas-stacklang { hilite=:or }
/api/v1/graph?q=nf.app,alerttest,:eq,name,ssCpuUser,:eq,:or
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the result set:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td><strong>alerttest</strong></td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td>ssCpuSystem</td>
    <td><strong>alerttest</strong></td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr>
    <td>ssCpuSystem</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr>
    <td>numRequests</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
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
(ts1 OR ts2): TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a OR b)` where `a`
and `b` are the corresponding intervals in the input time series. For example:

| **Time** | **a** | **b** | **a OR b** |
|----------|-------|-------|-------------|
|  00:01   | 0.0   |  0.0  |  0.0        |
|  00:01   | 0.0   |  1.0  |  1.0        |
|  00:02   | 1.0   |  0.0  |  1.0        |
|  00:03   | 1.0   |  1.0  |  1.0        |
|  00:04   | 0.5   |  1.7  |  1.0        |

The result will be a [signal time series](../alerting-expressions.md#signal-line) that will
be `1.0` for all intervals where the corresponding values of `a` or `b` are non-zero.
Example:

@@@ atlas-example { hilite=:or }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfDay,:time,:dup,300,:gt,:swap,290,:lt
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfDay,:time,:dup,300,:gt,:swap,290,:lt,:or
@@@
