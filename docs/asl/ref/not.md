@@@ atlas-signature
query: Query
-->
(!query): Query
@@@

Invert a query condition, selecting time series that do NOT match the specified query. This is
the logical NOT operation for queries, allowing you to exclude time series that match certain
criteria.

## Parameters

* **query**: The query condition to invert (result will include time series that DON'T match this query)

## Examples

Select time series that do NOT have a node identifier:

@@@ atlas-stacklang { hilite=:not }
/api/v1/graph?q=nf.node,:has,:not
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
  </tr><tr>
    <td>ssCpuSystem</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr>
    <td>ssCpuUser</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr>
    <td>ssCpuSystem</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td>numRequests</td>
    <td>nccp</td>
    <td>&nbsp;</td>
  </tr><tr>
    <td>ssCpuUser</td>
    <td>api</td>
    <td>i-0456</td>
  </tr>
  </tbody>
</table>

Notice that only `numRequests` (which has no `nf.node` tag) is highlighted, while all the time
series that have node identifiers are excluded.

## Related Operations

* [:and](and.md) - Logical AND operation (can be combined with NOT for complex conditions)
* [:or](or.md) - Logical OR operation (can be combined with NOT for complex conditions)
* [:has](has.md) - Check if a key exists (commonly used with NOT)
* [:eq](eq.md) - Basic equality comparison (can be inverted with NOT)
