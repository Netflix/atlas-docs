@@@ atlas-signature
v: String
k: String
-->
Query
@@@

Select time series where the value for a key has the specified suffix. For example, consider
the following query:

@@@ atlas-stacklang { hilite=:ends }
/api/v1/graph?q=name,ssCpuUser,:ends
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the result set:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td>ssCpu<strong>User</strong></td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr>
    <td>ssCpuSystem</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td>ssCpu<strong>User</strong></td>
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
    <td>ssCpu<strong>User</strong></td>
    <td>api</td>
    <td>i-0456</td>
  </tr>
  </tbody>
</table>