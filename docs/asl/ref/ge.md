
Greater than or equal operator. There are two variants of the `:ge` operator.

## Choosing

@@@ atlas-signature
value: String
key: String
-->
(key >= value): Query
@@@

This first variant is used for [choosing](../tutorial.md#choosing) the set of time series to
operate on. It selects time series that have a value for a key that is greater than or equal
to a specified value.

### Parameters

* **key**: The tag key to compare (e.g., `name`, `nf.app`)
* **value**: The value to compare against (comparison is lexicographic for strings)

### Examples

Select time series where the name is lexicographically greater than or equal to "ssCpuSystem":

For example, consider the following query:

@@@ atlas-stacklang { hilite=:ge }
/api/v1/graph?q=name,ssCpuSystem,:ge
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
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuSystem</strong></td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuSystem</strong></td>
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
(ts1 >= ts2): TimeSeriesExpr
@@@

Compute a new time series where each interval has the value `(a >= b)` where `a`
and `b` are the corresponding intervals in the input time series.

### Parameters

* **ts1**: First time series expression (left operand)
* **ts2**: Second time series expression (right operand)

### Examples

Numerical comparison of time series values:

| **Time** | **a** | **b** | **a >= b** |
|----------|-------|-------|-------------|
|  00:01   | 0.0   |  0.0  |  0.0        |
|  00:01   | 0.0   |  1.0  |  0.0        |
|  00:02   | 1.0   |  0.0  |  1.0        |
|  00:03   | 1.0   |  1.0  |  1.0        |
|  00:04   | 0.5   |  1.7  |  0.0        |

The result will be a [signal time series](../alerting-expressions.md#signal-line) that will
be `1.0` for intervals where the condition is true and `0.0` for intervals where it is false.

!!! info
    Note: The data points have floating point values. It is advisable to avoid relying on
    exact equality matches due to floating point precision issues.

Comparing time expressions (minute of hour vs hour of day):

@@@ atlas-example { hilite=:ge }
Before: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfHour,:time,hourOfDay,:time
After: /api/v1/graph?w=200&h=125&no_legend=1&s=e-3h&e=2012-01-01T07:00&tz=UTC&l=0&q=minuteOfHour,:time,hourOfDay,:time,:ge
@@@

## Related Operations

* [:gt](gt.md) - Greater than comparison
* [:lt](lt.md) - Less than comparison
* [:le](le.md) - Less than or equal comparison
* [:eq](eq.md) - Equality comparison for exact matches
* [:and](and.md), [:or](or.md) - Combine multiple comparison conditions

