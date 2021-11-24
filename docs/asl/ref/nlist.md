@@@ atlas-signature
aN
...
a0
N
-->
List(aN-1 ... a0)
@@@

Create a list with the top N items on the stack.

Since: 1.5.0

Examples:

@@@ atlas-stacklang
/api/v1/graph?q=a,0,:nlist
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>List()</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,2,:nlist
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>2</td>
<td>List(b, c)</td>
</tr><tr>
<td>1</td>
<td>c</td>
<td>a</td>
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
/api/v1/graph?q=a,b,c,4,:nlist
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>4</td>
<td>List(a, b, c)</td>
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
