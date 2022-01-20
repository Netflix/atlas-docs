@@@ atlas-signature
...
-->
Int
...
@@@

Push the depth of the stack.

Since: 1.5.0 

Examples:

@@@ atlas-stacklang
/api/v1/graph?q=,:depth
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td></td>
<td>0</td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=a,:depth
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>a</td>
<td>1</td>
</tr><tr>
<td>1</td>
<td></td>
<td>a</td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:depth
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>2</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td></td>
<td>a</td>
</tr></tbody></table>