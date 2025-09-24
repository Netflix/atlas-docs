@@@ atlas-signature
values: List[String]
key: String
-->
(key in values): Query
@@@

Select time series where the value for a key matches any value in the specified list. This is
more efficient than using multiple `:eq` conditions combined with `:or` when you need to match
against several possible values for the same key.

## Parameters

* **key**: The tag key to check (e.g., `name`, `nf.app`, `status`)
* **values**: A list of possible values to match against

## Examples

Select time series where the name is either "ssCpuUser" or "ssCpuSystem":

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

This is equivalent to but more efficient than:
`name,ssCpuUser,:eq,name,ssCpuSystem,:eq,:or`

## Related Operations

* [:eq](eq.md) - Check for a single specific value
* [:re](re.md) - Match using regular expressions
* [:has](has.md) - Check if a key exists regardless of value
* [:or](or.md) - Logical OR operation

