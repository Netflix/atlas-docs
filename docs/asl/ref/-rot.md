@@@ atlas-signature
b
a
...
-->
a
...
b
@@@

Rotate the stack so that the item at the top is now at the bottom.

Example: 

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,d,:-rot
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>d</td>
<td>c</td>
</tr><tr>
<td>1</td>
<td>c</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td>b</td>
<td>a</td>
</tr><tr>
<td>3</td>
<td>a</td>
<td>d</td>
</tr></tbody></table>