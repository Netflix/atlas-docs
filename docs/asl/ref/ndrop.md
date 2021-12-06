@@@ atlas-signature
aN
...
a0
N
-->
aN
@@@

Remove the top N items on the stack.

Example:

@@@ atlas-stacklang
/api/v1/graph?q=a,0,:ndrop
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td></td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,2,:ndrop
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>2</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>c</td>
<td></td>
</tr><tr>
<td>2</td>
<td>b</td>
<td></td>
</tr><tr>
<td>3</td>
<td>a</td>
<td></td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,4,:ndrop
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>4</td>
<td></td>
</tr><tr>
<td>1</td>
<td>c</td>
<td></td>
</tr><tr>
<td>2</td>
<td>b</td>
<td></td>
</tr><tr>
<td>3</td>
<td>a</td>
<td></td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=,:ndrop
@@@

!!! Warning
    Throws an exception due to missing the `N` param.