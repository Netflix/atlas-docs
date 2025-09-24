@@@ atlas-signature
key: String
-->
Query
@@@

Select time series that have a specified tag key, regardless of the key's value. This is useful
for filtering based on the presence of optional tags or finding time series that have been
tagged with specific dimensions.

## Parameters

* **key**: The tag key name to check for existence (e.g., `nf.node`, `status`, `env`)

## Examples

Select all time series that have a node identifier:

@@@ atlas-stacklang { hilite=:has }
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

Notice that only time series with a value in the `nf.node` column are highlighted, while
`numRequests` which has no `nf.node` tag is not selected.

## Related Operations

* [:eq](eq.md) - Check if a key has a specific value
* [:re](re.md) - Check if a key matches a regular expression pattern
* [:in](in.md) - Check if a key's value is in a list of options
* [:not](not.md) - Invert the query condition (e.g., select series that DON'T have a key)
