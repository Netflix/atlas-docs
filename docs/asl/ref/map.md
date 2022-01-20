@@@ atlas-signature
function: List
items: List
-->
List(function(items[0], ..., items[N-1])
@@@

Create a new list by applying a function to all elements of a list. 

Example:

@@@ atlas-stacklang
/api/v1/graph?q=(,a%s,b%s,),(,(,.netflix.com,),:format,),:map
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>List((, .netflix.com, ), :format)</td>
<td>List(a.netflix.com, b.netflix.com)</td>
</tr><tr>
<td>1</td>
<td>List(a%s, b%s)</td>
<td></td>
</tr></tbody></table>