@@@ atlas-signature
...
second: Any
bottom: Any
-->
bottom: Any
...
second: Any
@@@

Rotate the stack so that the item at the bottom is moved to the top of the stack, and all other items
move down one position. This is the opposite of [:-rot](-rot.md).

## Parameters

* **bottom**: The item currently at the bottom of the stack that will be moved to the top
* **second**: The item in the second-to-bottom position that will become the new bottom item
* **...**: Any additional items on the stack that will each move down one position

## Examples

This example shows how the stack is rotated with four items:

@@@ atlas-stacklang
/api/v1/graph?q=a,b,c,d,:rot
@@@

<table><thead><th>Pos</th><th>Input</th><th>Output</th></thead><tbody><tr>
<td>0</td>
<td>d</td>
<td>a</td>
</tr><tr>
<td>1</td>
<td>c</td>
<td>d</td>
</tr><tr>
<td>2</td>
<td>b</td>
<td>c</td>
</tr><tr>
<td>3</td>
<td>a</td>
<td>b</td>
</tr></tbody></table>

## Related Operations

* [:-rot](-rot.md) - Rotate in the opposite direction (top to bottom)
* [:swap](swap.md) - Exchange the top two stack items
* [:over](over.md) - Copy the second item to the top