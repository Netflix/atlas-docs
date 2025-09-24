@@@ atlas-signature
top: Any
second: Any
...
-->
second: Any
...
top: Any
@@@

Rotate the stack so that the item at the top is moved to the bottom of the stack, and all other items
move up one position.

## Parameters

* **top**: The item currently at the top of the stack that will be moved to the bottom
* **second**: The item in the second position that will become the new top item
* **...**: Any additional items on the stack that will each move up one position

## Examples

This example shows how the stack is rotated with four items:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,d,:-rot
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>d</td>
<td>c</td>
</tr><tr>
<td>1</td>
<td>c</td>
<td>b</td>
</tr><tr>
<td>2</td>
<td>b</td>
<td>a</td>
</tr><tr>
<td>3</td>
<td>a</td>
<td>d</td>
</tr></tbody></table>

## Related Operations

* [:rot](rot.md) - Rotate in the opposite direction (bottom to top)
* [:swap](swap.md) - Exchange the top two stack items
* [:over](over.md) - Copy the second item to the top