@@@ atlas-signature
value: String
key: String
-->
Query
@@@

Select time series where the value for a tag key ends with the specified suffix string.
This provides a more efficient alternative to regular expressions when you only need simple
suffix matching. It performs exact suffix matching and is case-sensitive.

## Parameters

* **key**: The tag key to check (e.g., `name`, `nf.app`)
* **value**: The suffix string that tag values must end with

## Examples

Find all metrics whose name ends with "User":

@@@ atlas-stacklang { hilite=:ends }
/api/v1/graph?q=name,User,:ends
@@@

When matching against sample data, the highlighted time series would be included:

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

## Related Operations

* [:starts](starts.md) - Match by prefix instead of suffix
* [:contains](contains.md) - Match by substring anywhere in the value
* [:eq](eq.md) - Exact string matching
* [:re](re.md) - Full regular expression matching (more powerful but slower)
* [:and](and.md) / [:or](or.md) - Combine with other query conditions