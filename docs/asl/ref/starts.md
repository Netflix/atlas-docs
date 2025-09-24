@@@ atlas-signature
value: String
key: String
-->
Query
@@@

Select time series where the value for a tag key starts with the specified prefix string.
This provides a more efficient alternative to regular expressions when you only need simple
prefix matching. It performs exact prefix matching and is case-sensitive.

## Parameters

* **key**: The tag key to check (e.g., `name`, `nf.app`)
* **value**: The prefix string that tag values must start with

## Examples

Find all metrics whose name starts with "ssCpu":

@@@ atlas-stacklang { hilite=:starts }
/api/v1/graph?q=name,ssCpu,:starts
@@@

When matching against sample data, the highlighted time series would be included:

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

## Related Operations

* [:ends](ends.md) - Match by suffix instead of prefix
* [:contains](contains.md) - Match by substring anywhere in the value
* [:eq](eq.md) - Exact string matching
* [:re](re.md) - Full regular expression matching (more powerful but slower)
* [:and](and.md) / [:or](or.md) - Combine with other query conditions