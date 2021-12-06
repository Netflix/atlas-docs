@@@ atlas-signature
items: List
functions: List
-->
function[0](items[0])
...
function[N](items[N])
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