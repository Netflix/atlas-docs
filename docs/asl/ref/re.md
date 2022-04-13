@@@ atlas-signature
v: String
k: String
-->
(k=~/^v/): Query
@@@

!!! warning
    Regular expressions can be expensive to check and should be avoided if possible. When
    designing data to publish ensure that common query patterns would not need the use of
    regular expressions.

Select time series where the value for a key matches the specified regular expression.
For example, consider the following query:

@@@ atlas-stacklang { hilite=:re }
/api/v1/graph?q=name,ssCpu,:re
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

The regular expression value will be automatically anchored at the start and the matching is
case sensitive. Always try to have a simple prefix on the expression to allow for more efficient
matching of the expression. For more information on supported patterns, see the
[Java regular expressions] documentation.

[Java regular expressions]: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html
