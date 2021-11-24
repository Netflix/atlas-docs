@@@ atlas-signature
?
-->
?
@@@

Shorthand equivalent to writing: `:swap,:over` 

Example:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:tuck
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
</tr></tbody></table>
