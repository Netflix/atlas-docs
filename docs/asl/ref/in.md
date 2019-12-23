<table>
  <tbody>
  <tr>
    <td>
      <strong>Input Stack:</strong>
      <table>
        <tbody>
        <tr><td>vs: List[String]</td></tr>
        <tr><td>k: String</td></tr>
        </tbody>
      </table>
    </td><td style="vertical-align: middle;">
      &#8680;
    </td><td>
      <strong>Output Stack:</strong>
      <table>
        <tbody>
        <tr><td>(k in vs): Query</td></tr>
        <tr><td>&nbsp;</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
  </tbody>
</table>

Select time series where the value for a key is in the specified set. For example, consider
the following query:

@@@ atlas-stacklang { hilite=:in }
/api/v1/graph?q=name,(,ssCpuUser,ssCpuSystem,),:in
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

