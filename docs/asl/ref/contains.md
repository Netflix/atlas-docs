@@@ atlas-signature
v: String
k: String
-->
Query
@@@

Select time series where the value for a key includes the specified substring. For example,
consider the following query:

@@@ atlas-stacklang { hilite=:contains }
/api/v1/graph?q=name,Cpu,:contains
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the result set:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td>ss<strong>Cpu</strong>User</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td>ss<strong>Cpu</strong>System</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td>ss<strong>Cpu</strong>User</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td>ss<strong>Cpu</strong>System</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr>
    <td>numRequests</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td>ss<strong>Cpu</strong>User</td>
    <td>api</td>
    <td>i-0456</td>
  </tr>
  </tbody>
</table>