@@@ atlas-signature
function: List
items: List
-->
function(items[N-1])
...
function(items[0])
@@@

Pops a list off the stack and executes it as a program. 

Example:

@@@ atlas-stacklang
/api/v1/graph?q=(,a,b,),(,:dup,),:each
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>List(:dup)</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>List(a, b)</td>
<td>a</td>
</tr><tr>
<td>2</td>
<td></td>
<td>b</td>
</tr><tr>
<td>3</td>
<td></td>
<td>b</td>
</tr></tbody></table>