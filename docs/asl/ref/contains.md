@@@ atlas-signature
value: String
key: String
-->
Query
@@@

Select time series where the value for a tag key contains the specified substring anywhere
within the value. This provides a more efficient alternative to regular expressions when you
only need simple substring matching. It performs exact substring matching and is case-sensitive.

## Parameters

* **key**: The tag key to check (e.g., `name`, `nf.app`)
* **value**: The substring that must appear anywhere within tag values

## Examples

Find all metrics whose name contains "Cpu":

@@@ atlas-stacklang { hilite=:contains }
/api/v1/graph?q=name,Cpu,:contains
@@@

When matching against sample data, the highlighted time series would be included:

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

## Related Operations

* [:starts](starts.md) - Match by prefix only
* [:ends](ends.md) - Match by suffix only
* [:eq](eq.md) - Exact string matching
* [:re](re.md) - Full regular expression matching (more powerful but slower)
* [:and](and.md) / [:or](or.md) - Combine with other query conditions