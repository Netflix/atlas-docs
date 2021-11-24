@@@ atlas-signature
a
b
-->
a
b
a
b
@@@

Shorthand equivalent to writing: `:over,:over`

Example:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:2over
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr><tr>
<td>2</td>
<td></td>
<td>b</td>
</tr><tr>
<td>3</td>
<td></td>
<td>a</td>
</tr></tbody></table>