@@@ atlas-signature
?
-->
List(?)
@@@

Pop all items off the stack and push them as a list.

Example:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:list
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>List(b, a)</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td></td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=,:list
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td></td>
<td>List()</td>
</tr></tbody></table>
