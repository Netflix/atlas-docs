<table>
  <tbody>
  <tr>
    <td>
      <strong>Input Stack:</strong>
      <table>
        <tbody>
        <tr><td>v: String</td></tr>
        <tr><td>k: String</td></tr>
        </tbody>
      </table>
    </td><td style="vertical-align: middle;">
      &#8680;
    </td><td>
      <strong>Output Stack:</strong>
      <table>
        <tbody>
        <tr><td>(k=~/^v/i): Query</td></tr>
        <tr><td>&nbsp;</td></tr>
        </tbody>
      </table>
    </td>
  </tr>
  </tbody>
</table>

!!! warning
    Ignoring the case will always result if a full scan for the key. This should be used
    sparingly and only for tag queries. If a case-insensitive match is not required, use
    [:re](re.md) intead.

Select time series where the value for a key matches the specified regular expression with
case insenitive matching. For example, consider the following query:

@@@ atlas-stacklang { hilite=:reic }
/api/v1/graph?q=name,ssCPU,:reic
@@@

When matching against the sample data in the table below, the highlighted time series would be
included in the result set:

<table>
  <thead>
  <th>Name</th><th>nf.app</th><th>nf.node</th>
  </thead>
  <tbody>
  <tr class="atlas-hilite">
    <td><strong>ssCpu</strong>User</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>System</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>User</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>System</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr>
    <td>numRequests</td>
    <td>nccp</td>
    <td>i-0abc</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpu</strong>User</td>
    <td>api</td>
    <td>i-0456</td>
  </tr>
  </tbody>
</table>

Notice that the casing for the query does not match the data. The regular expression value will
be automatically anchored at the start. For more information on supported patterns, see the
[Java regular expressions] documentation.

[Java regular expressions]: https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/util/regex/Pattern.html
