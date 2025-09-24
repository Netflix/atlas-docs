@@@ atlas-signature
value: String
key: String
-->
(key=~/^value/i): Query
@@@

!!! warning
    Case-insensitive matching requires a full scan of all time series for the specified key,
    which can be significantly slower than exact matches. Use this operator sparingly and only
    when case-insensitive matching is genuinely required. For case-sensitive regex matching,
    use [:re](re.md) instead.

Select time series where the value for a key matches the specified regular expression with
case insensitive matching. The regular expression value will be automatically anchored at the start.
For more information on supported patterns, see the [Java regular expressions] documentation.

## Parameters

* **key**: The tag key to match against (e.g., `name`, `nf.app`)
* **value**: A regular expression pattern to match against the key's value (case-insensitive)

## Examples

Case-insensitive matching where query casing doesn't match the data:

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

Notice that the casing for the query (`ssCPU`) does not match the data (`ssCpu`), but the
case-insensitive matching still finds the correct time series.

## Related Operations

* [:re](re.md) - Case-sensitive regular expression matching (much faster)
* [:eq](eq.md) - Exact string matching (fastest option)
* [:in](in.md) - Match against multiple exact values
* [:has](has.md) - Check if a tag key exists

[Java regular expressions]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html
