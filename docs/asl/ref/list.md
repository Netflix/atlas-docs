@@@ atlas-signature
...
-->
List[?]
@@@

Pop all items currently on the stack and create a list containing them. The order in the
list preserves the stack order, with the bottom stack item becoming the first list element.

## Parameters

* **...**: All items currently on the stack (variable number of arguments)

## Examples

Creating a list from two items:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,:list
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>b</td>
<td>List(b, a)</td>
</tr><tr>
<td>1</td>
<td>a</td>
<td></td>
</tr></tbody></table>

Note that `a` was added to the stack first and appears as the first element in the list,
while `b` was added second and appears as the second element.

Creating an empty list:

@@@ atlas-stacklang
/api/v1/graph?q=,:list
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td></td>
<td>List()</td>
</tr></tbody></table>

## Related Operations

* [:each](each.md) - Execute a function for each element in a list
* [:map](map.md) - Transform each element in a list
* [:format](format.md) - Use lists as arguments for string formatting
* [:by](by.md) - Use lists to specify grouping keys