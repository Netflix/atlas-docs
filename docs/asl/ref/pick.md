@@@ atlas-signature
N
a0
...
aN
-->
aN-1
a0
...
aN
@@@

Pick an item in the stack and put a copy on the top.

Since: 1.5.0

Example:

@@@ atlas-stacklang
/api/v1/graph?q=a,0,:pick
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=a,b,0,:pick
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>0</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=a,b,1,:pick
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>1</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>b</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td>a</td>
<td>a</td>
</tr></tbody></table>