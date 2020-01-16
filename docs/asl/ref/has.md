@@@ atlas-signature
k: String
-->
Query
@@@

Select time series that have a specified key. For example, consider the following
query:

@@@ atlas-stacklang { hilite=:eq }
/api/v1/graph?q=nf.node,:has
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the result set:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td>ssCpuUser</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td>ssCpuSystem</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td>ssCpuUser</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td>ssCpuSystem</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr>
    <td>numRequests</td>
    <td>nccp</td>
    <td>&nbsp;</td>
  </tr><tr class="atlas-hilite">
    <td>ssCpuUser</td>
    <td>api</td>
    <td>i-0456</td>
  </tr>
  </tbody>
</table>
