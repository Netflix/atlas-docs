@@@ atlas-signature
a
b
-->
a
b
a
@@@

Copy the item in the second position on the stack to the top. 

Example:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:over
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td></td>
<td>a</td>
</tr></tbody></table>
