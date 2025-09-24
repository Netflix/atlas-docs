@@@ atlas-signature
value: String
key: String
-->
(key == value): Query
@@@

Select time series that have a specified value for a key. This is the most common operator for
filtering time series data and forms the foundation of most queries. The comparison is case-sensitive
and requires an exact string match.

## Parameters

* **key**: The tag key to match against (e.g., `name`, `nf.app`, `status`)
* **value**: The exact value that the key must equal for a time series to be included

## Examples

Select all time series where the name tag equals "ssCpuUser":

@@@ atlas-stacklang { hilite=:eq }
/api/v1/graph?q=name,ssCpuUser,:eq
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
  </tr><tr>
    <td>ssCpuSystem</td>
    <td>alerttest</td>
    <td>i-0123</td>
  </tr><tr class="atlas-hilite">
    <td><strong>ssCpuUser</strong></td>
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
    <td><strong>ssCpuUser</strong></td>
    <td>api</td>
    <td>i-0456</td>
  </tr>
  </tbody>
</table>

## Related Operations

* [:and](and.md) - Combine multiple query conditions
* [:or](or.md) - Match any of multiple query conditions
* [:re](re.md) - Match using regular expressions (case-sensitive)
* [:in](in.md) - Match against a list of possible values
* [:has](has.md) - Check if a tag key exists regardless of value