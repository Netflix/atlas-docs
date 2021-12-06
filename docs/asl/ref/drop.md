@@@ atlas-signature
a
-->
<empty>
@@@

Remove the item on the top of the stack. 

Example:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,:drop
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>c</td>
<td>b</td>
</tr><tr>
<td>1</td>
<td>b</td>
<td>a</td>
</tr><tr>
<td>2</td>
<td>a</td>
<td></td>
</tr></tbody></table>

@@@ atlas-stacklang
/api/v1/graph?q=:drop
@@@

!!! Warning
    Throws an exception due to an empty stack.
